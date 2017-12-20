
from mastermind.module.game.application.create_game_use_case \
    import CreateGameCommandHandler, GameCreator
from mastermind.module.game.domain.error.game_errors import GameAlreadyExists
from mastermind.module.game.domain.model.game import Game
from mastermind.module.game.test.behaviour.game_behaviour_spec \
    import GameBehaviourSpec
from mastermind.module.game.test.infrastructure.random. \
    random_create_game_command import random_create_game_command
from mastermind.module.game.test.infrastructure.random.random_game import random_game
from mastermind.module.shared.domain.model.code_peg import CodePeg
from mastermind.module.shared.domain.model.game_id import GameId


class CreateGameSpecTest(GameBehaviourSpec):

    def setUp(self):
        super().setUp()
        self.handler = CreateGameCommandHandler(
            GameCreator(self.game_repository))

    def test_should_create_game(self):
        command = random_create_game_command()

        game_id = GameId(command.game_id)
        expected_game = Game(
            game_id,
            CodePeg(command.first_code_peg),
            CodePeg(command.second_code_peg),
            CodePeg(command.third_code_peg),
            CodePeg(command.fourth_code_peg)
        )

        self.should_not_find_game(game_id)
        self.should_insert_game(expected_game)

        self.handler.handle(command)

    def test_should_fail_if_game_already_exists(self):
        command = random_create_game_command()

        game_id = GameId(command.game_id)
        self.should_find_game(game_id, random_game(game_id=game_id))

        with self.assertRaises(GameAlreadyExists) as context:
            self.handler.handle(command)
            self.assertEqual(context.exception, GameAlreadyExists(game_id))
