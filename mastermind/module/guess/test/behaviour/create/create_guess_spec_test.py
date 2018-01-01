from mastermind.module.game.application.search_game_use_case \
    import SearchGameResponse, SearchGameQuery
from mastermind.module.game.test.infrastructure.random.random_game_response \
    import random_game_response
from mastermind.module.guess.application.create_guess_use_case \
    import CreateGuessCommandHandler, GuessCreator
from mastermind.module.guess.domain.error.guess_errors \
    import GameNotFound, GuessesLimitExceeded, GuessAlreadyExists
from mastermind.module.guess.domain.model.guess import Guess
from mastermind.module.guess.domain.model.guess_id import GuessId
from mastermind.module.guess.test.behaviour.guess_behaviour_spec \
    import GuessBehaviourSpec
from mastermind.module.guess.test.infrastructure.random\
    .random_create_guess_command import random_create_guess_command
from mastermind.module.guess.test.infrastructure.random.random_guess \
    import random_guess
from mastermind.module.shared.domain.model.code_peg import CodePeg
from mastermind.module.shared.domain.model.game_id import GameId


class CreateGuessSpecTest(GuessBehaviourSpec):
    def setUp(self):
        super().setUp()
        self.handler = CreateGuessCommandHandler(
            GuessCreator(self.guess_repository, self.query_bus))

    def test_should_create_guess(self):
        command = random_create_guess_command()

        game_id = GameId(command.game_id)
        guess_id = GuessId(command.guess_id)
        search_game_response = SearchGameResponse(
            random_game_response(game_id=game_id.game_id))
        guess = Guess(
            guess_id=guess_id,
            game_id=game_id,
            first_peg=CodePeg(command.first_code_peg),
            second_peg=CodePeg(command.second_code_peg),
            third_peg=CodePeg(command.third_code_peg),
            fourth_peg=CodePeg(command.fourth_code_peg)
        )

        self.should_ask_query(SearchGameQuery(
            command.game_id), search_game_response)
        self.should_find_guesses_by_game_id(game_id, [])
        self.should_not_find_guess(guess_id)
        self.should_insert_guess(guess)

        self.handler.handle(command)

    def test_should_fail_if_game_does_not_exist(self):
        command = random_create_guess_command()

        self.should_ask_query(SearchGameQuery(
            command.game_id), SearchGameResponse(None))

        with self.assertRaises(GameNotFound) as context:
            self.handler.handle(command)
            self.assertEqual(context.exception,
                             GameNotFound(GameId(command.game_id)))

    def test_should_fail_if_guess_does_already_exist(self):
        command = random_create_guess_command()

        game_id = GameId(command.game_id)
        guess_id = GuessId(command.guess_id)
        existing_guess = random_guess(guess_id=guess_id)
        search_game_response = SearchGameResponse(
            random_game_response(game_id=game_id.game_id))

        self.should_ask_query(SearchGameQuery(
            command.game_id), search_game_response)
        self.should_find_guess(guess_id, existing_guess)

        with self.assertRaises(GuessAlreadyExists) as context:
            self.handler.handle(command)
            self.assertEqual(context.exception, GuessAlreadyExists(guess_id))

    def test_should_fail_if_ten_guesses_already_exist_for_game(self):
        command = random_create_guess_command()

        game_id = GameId(command.game_id)
        guess_id = GuessId(command.guess_id)
        search_game_response = SearchGameResponse(
            random_game_response(game_id=game_id.game_id))
        already_existing_guesses = [random_guess() for _ in range(10)]

        self.should_ask_query(SearchGameQuery(
            command.game_id), search_game_response)
        self.should_not_find_guess(guess_id)
        self.should_find_guesses_by_game_id(game_id, already_existing_guesses)

        with self.assertRaises(GuessesLimitExceeded) as context:
            self.handler.handle(command)
            self.assertEqual(context.exception, GuessesLimitExceeded(
                GameId(command.game_id), 10))
