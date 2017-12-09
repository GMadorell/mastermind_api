from mastermind.module.game.application.create_game_use_case\
    import CreateGameCommandHandler, GameCreator
from mastermind.module.game.domain.model.code_peg import CodePeg
from mastermind.module.game.domain.model.game import Game
from mastermind.module.game.domain.model.game_id import GameId
from mastermind.module.game.test.behaviour.game_behaviour_spec\
    import GameBehaviourSpec
from mastermind.module.game.test.infrastructure.random.\
    random_create_game_command import random_create_game_command


class CreateGameSpecTest(GameBehaviourSpec):

    def setUp(self):
        super().setUp()
        self.handler = CreateGameCommandHandler(
            GameCreator(self.game_repository))

    def test_should_create_game(self):
        command = random_create_game_command()

        expected_game = Game(
            GameId(command.game_id),
            CodePeg(command.first_code_peg),
            CodePeg(command.second_code_peg),
            CodePeg(command.third_code_peg),
            CodePeg(command.fourth_code_peg))

        self.handler.handle(command)

        self.should_have_inserted_game(expected_game)
