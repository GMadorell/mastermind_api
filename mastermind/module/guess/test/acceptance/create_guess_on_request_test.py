import json

from mastermind.infrastructure.app.mastermind import create_app
from mastermind.module.game.test.infrastructure.random.random_code_peg \
    import invalid_code_peg
from mastermind.module.game.test.infrastructure.random.random_game \
    import random_game
from mastermind.module.game.test.infrastructure.random.random_game_id \
    import non_empty_invalid_game_id
from mastermind.module.guess.test.infrastructure.random.random_guess \
    import random_guess
from mastermind.module.guess.test.infrastructure.random.random_guess_id \
    import invalid_guess_id
from mastermind.module.shared.domain.model.game_id import GameId
from mastermind.module.shared.test.infrastructure.context \
    .context_aware_test_case import ContextAwareTestCase


class CreateGuessOnRequestTest(ContextAwareTestCase):
    GUESS_ENDPOINT_TEMPLATE = "/games/{game_id}/guesses"

    def setUp(self):
        super().setUp()
        self.app = create_app(self.context)
        self.app.testing = True
        self.test_client = self.app.test_client()

    def test_should_create_game_on_request(self):
        expected_guess = random_guess()
        game = random_game(game_id=expected_guess.game_id)

        self.context.game_repository.insert(game)

        request_data = {
            "guess_id": expected_guess.guess_id.guess_id,
            "first_code_peg": expected_guess.first_peg.peg_type,
            "second_code_peg": expected_guess.second_peg.peg_type,
            "third_code_peg": expected_guess.third_peg.peg_type,
            "fourth_code_peg": expected_guess.fourth_peg.peg_type
        }

        endpoint = self.__guess_endpoint_for_game_id(expected_guess.game_id)
        response = self.test_client.post(endpoint, data=request_data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data), {})
        self.assertEqual(
            self.context.guess_repository.search(expected_guess.guess_id),
            expected_guess
        )

    def test_should_fail_when_game_does_not_exist(self):
        expected_guess = random_guess()
        request_data = {
            "guess_id": expected_guess.guess_id.guess_id,
            "first_code_peg": expected_guess.first_peg.peg_type,
            "second_code_peg": expected_guess.second_peg.peg_type,
            "third_code_peg": expected_guess.third_peg.peg_type,
            "fourth_code_peg": expected_guess.fourth_peg.peg_type
        }

        endpoint = self.__guess_endpoint_for_game_id(expected_guess.game_id)
        response = self.test_client.post(endpoint, data=request_data)

        self.assertEqual(response.status_code, 404)
        self.assertNotEquals(json.loads(response.data), {})
        self.assertEqual(
            self.context.guess_repository.search(expected_guess.guess_id),
            None
        )

    def test_should_fail_when_guess_does_already_exist(self):
        expected_guess = random_guess()
        game = random_game(game_id=expected_guess.game_id)
        existing_guess = random_guess(guess_id=expected_guess.guess_id)

        self.context.game_repository.insert(game)
        self.context.guess_repository.insert(existing_guess)

        request_data = {
            "guess_id": expected_guess.guess_id.guess_id,
            "first_code_peg": expected_guess.first_peg.peg_type,
            "second_code_peg": expected_guess.second_peg.peg_type,
            "third_code_peg": expected_guess.third_peg.peg_type,
            "fourth_code_peg": expected_guess.fourth_peg.peg_type
        }

        endpoint = self.__guess_endpoint_for_game_id(expected_guess.game_id)
        response = self.test_client.post(endpoint, data=request_data)

        self.assertEqual(response.status_code, 409)
        self.assertNotEquals(json.loads(response.data), {})
        self.assertEqual(
            self.context.guess_repository.search(expected_guess.guess_id),
            existing_guess
        )

    def test_should_fail_when_the_guesses_limit_is_surpassed(self):
        expected_guess = random_guess()
        game = random_game(game_id=expected_guess.game_id)

        self.context.game_repository.insert(game)
        for _ in range(10):
            self.context.guess_repository.insert(
                random_guess(game_id=expected_guess.game_id)
            )

        request_data = {
            "guess_id": expected_guess.guess_id.guess_id,
            "first_code_peg": expected_guess.first_peg.peg_type,
            "second_code_peg": expected_guess.second_peg.peg_type,
            "third_code_peg": expected_guess.third_peg.peg_type,
            "fourth_code_peg": expected_guess.fourth_peg.peg_type
        }

        endpoint = self.__guess_endpoint_for_game_id(expected_guess.game_id)
        response = self.test_client.post(endpoint, data=request_data)

        self.assertEqual(response.status_code, 409)
        self.assertNotEquals(json.loads(response.data), {})
        self.assertEqual(
            self.context.guess_repository.search(expected_guess.guess_id),
            None
        )

    def test_invalid_guess_id(self):
        guess = random_guess()

        request_data = {
            "guess_id": invalid_guess_id(),
            "first_code_peg": guess.first_peg.peg_type,
            "second_code_peg": guess.second_peg.peg_type,
            "third_code_peg": guess.third_peg.peg_type,
            "fourth_code_peg": guess.fourth_peg.peg_type
        }

        endpoint = self.__guess_endpoint_for_game_id(guess.game_id)
        response = self.test_client.post(endpoint, data=request_data)

        self.assertEqual(response.status_code, 422)

    def test_invalid_first_code_peg(self):
        guess = random_guess()

        request_data = {
            "guess_id": guess.guess_id.guess_id,
            "first_code_peg": invalid_code_peg(),
            "second_code_peg": guess.second_peg.peg_type,
            "third_code_peg": guess.third_peg.peg_type,
            "fourth_code_peg": guess.fourth_peg.peg_type
        }

        endpoint = self.__guess_endpoint_for_game_id(guess.game_id)
        response = self.test_client.post(endpoint, data=request_data)

        self.assertEqual(response.status_code, 422)

    def test_invalid_second_code_peg(self):
        guess = random_guess()

        request_data = {
            "guess_id": guess.guess_id.guess_id,
            "first_code_peg": guess.first_peg.peg_type,
            "second_code_peg": invalid_code_peg(),
            "third_code_peg": guess.third_peg.peg_type,
            "fourth_code_peg": guess.fourth_peg.peg_type
        }

        endpoint = self.__guess_endpoint_for_game_id(guess.game_id)
        response = self.test_client.post(endpoint, data=request_data)

        self.assertEqual(response.status_code, 422)

    def test_invalid_third_code_peg(self):
        guess = random_guess()

        request_data = {
            "guess_id": guess.guess_id.guess_id,
            "first_code_peg": guess.first_peg.peg_type,
            "second_code_peg": guess.second_peg.peg_type,
            "third_code_peg": invalid_code_peg(),
            "fourth_code_peg": guess.fourth_peg.peg_type
        }

        endpoint = self.__guess_endpoint_for_game_id(guess.game_id)
        response = self.test_client.post(endpoint, data=request_data)

        self.assertEqual(response.status_code, 422)

    def test_invalid_fourth_code_peg(self):
        guess = random_guess()

        request_data = {
            "guess_id": guess.guess_id.guess_id,
            "first_code_peg": guess.first_peg.peg_type,
            "second_code_peg": guess.second_peg.peg_type,
            "third_code_peg": guess.third_peg.peg_type,
            "fourth_code_peg": invalid_code_peg()
        }

        endpoint = self.__guess_endpoint_for_game_id(guess.game_id)
        response = self.test_client.post(endpoint, data=request_data)

        self.assertEqual(response.status_code, 422)

    def test_invalid_game_id(self):
        guess = random_guess()

        request_data = {
            "guess_id": guess.guess_id.guess_id,
            "first_code_peg": guess.first_peg.peg_type,
            "second_code_peg": guess.second_peg.peg_type,
            "third_code_peg": guess.third_peg.peg_type,
            "fourth_code_peg": guess.fourth_peg.peg_type
        }

        endpoint = self.__guess_endpoint_for_raw_game_id(
            non_empty_invalid_game_id())
        response = self.test_client.post(endpoint, data=request_data)

        self.assertEqual(response.status_code, 422)

    def __guess_endpoint_for_game_id(self, game_id: GameId) -> str:
        return self.GUESS_ENDPOINT_TEMPLATE.format(game_id=game_id.game_id)

    def __guess_endpoint_for_raw_game_id(self, raw_game_id: str) -> str:
        return self.GUESS_ENDPOINT_TEMPLATE.format(game_id=raw_game_id)
