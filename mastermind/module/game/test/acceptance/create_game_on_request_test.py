import json

from mastermind.infrastructure.app.mastermind import create_app
from mastermind.module.game.test.infrastructure.random.random_code_peg import random_code_peg, invalid_code_peg
from mastermind.module.game.test.infrastructure.random.random_game import random_game
from mastermind.module.game.test.infrastructure.random.random_game_id import random_game_id, invalid_game_id
from mastermind.module.shared.test.infrastructure.context.context_aware_test_case import ContextAwareTestCase


class CreateGameOnRequestTest(ContextAwareTestCase):
    GAME_ENDPOINT = "/games"

    def setUp(self):
        super().setUp()
        self.app = create_app(self.context)
        self.app.testing = True
        self.test_client = self.app.test_client()

    def test_should_create_game_on_request(self):
        expected_game = random_game()
        request_data = {
            "game_id": expected_game.game_id.game_id,
            "first_code_peg": expected_game.first_peg.peg_type,
            "second_code_peg": expected_game.second_peg.peg_type,
            "third_code_peg": expected_game.third_peg.peg_type,
            "fourth_code_peg": expected_game.fourth_peg.peg_type
        }

        response = self.test_client.post(self.GAME_ENDPOINT, data=request_data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data), {})
        self.assertEqual(
            self.context.game_repository.search(expected_game.game_id),
            expected_game
        )

    def test_game_already_exists(self):
        game = random_game()
        request_data = {
            "game_id": game.game_id.game_id,
            "first_code_peg": game.first_peg.peg_type,
            "second_code_peg": game.second_peg.peg_type,
            "third_code_peg": game.third_peg.peg_type,
            "fourth_code_peg": game.fourth_peg.peg_type
        }

        self.context.game_repository.insert(game)
        response = self.test_client.post(self.GAME_ENDPOINT, data=request_data)
        self.assertEqual(response.status_code, 409)

    def test_invalid_game_id(self):
        game = random_game()
        request_data = {
            "game_id": invalid_game_id(),
            "first_code_peg": game.first_peg.peg_type,
            "second_code_peg": game.second_peg.peg_type,
            "third_code_peg": game.third_peg.peg_type,
            "fourth_code_peg": game.fourth_peg.peg_type
        }

        response = self.test_client.post(self.GAME_ENDPOINT, data=request_data)
        self.assertEqual(response.status_code, 422)

    def test_invalid_first_code_peg(self):
        game = random_game()
        request_data = {
            "game_id": game.game_id.game_id,
            "first_code_peg": invalid_code_peg(),
            "second_code_peg": game.second_peg.peg_type,
            "third_code_peg": game.third_peg.peg_type,
            "fourth_code_peg": game.fourth_peg.peg_type
        }

        response = self.test_client.post(self.GAME_ENDPOINT, data=request_data)
        self.assertEqual(response.status_code, 422)

    def test_invalid_second_code_peg(self):
        game = random_game()
        request_data = {
            "game_id": game.game_id.game_id,
            "first_code_peg": game.first_peg.peg_type,
            "second_code_peg": invalid_code_peg(),
            "third_code_peg": game.third_peg.peg_type,
            "fourth_code_peg": game.fourth_peg.peg_type
        }

        response = self.test_client.post(self.GAME_ENDPOINT, data=request_data)
        self.assertEqual(response.status_code, 422)

    def test_invalid_third_code_peg(self):
        game = random_game()
        request_data = {
            "game_id": game.game_id.game_id,
            "first_code_peg": game.first_peg.peg_type,
            "second_code_peg": game.second_peg.peg_type,
            "third_code_peg": invalid_code_peg(),
            "fourth_code_peg": game.fourth_peg.peg_type
        }

        response = self.test_client.post(self.GAME_ENDPOINT, data=request_data)
        self.assertEqual(response.status_code, 422)

    def test_invalid_fourth_code_peg(self):
        game = random_game()
        request_data = {
            "game_id": game.game_id.game_id,
            "first_code_peg": game.first_peg.peg_type,
            "second_code_peg": game.second_peg.peg_type,
            "third_code_peg": game.third_peg.peg_type,
            "fourth_code_peg": invalid_code_peg()
        }

        response = self.test_client.post(self.GAME_ENDPOINT, data=request_data)
        self.assertEqual(response.status_code, 422)
