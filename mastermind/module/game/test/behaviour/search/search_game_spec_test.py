from mastermind.module.game.application.search_game_use_case import SearchGameQueryHandler, SearchGameResponse, \
    GameResponse
from mastermind.module.game.test.behaviour.game_behaviour_spec import GameBehaviourSpec
from mastermind.module.game.test.infrastructure.random.random_game import random_game
from mastermind.module.game.test.infrastructure.random.random_game_id import random_game_id
from mastermind.module.game.test.infrastructure.random.random_search_game_query import random_search_game_query


class SearchGameSpecTest(GameBehaviourSpec):
    def setUp(self):
        super().setUp()
        self.handler = SearchGameQueryHandler(self.game_repository)

    def test_should_find_existing_game(self):
        query = random_search_game_query()

        game_id = random_game_id(query.game_id)
        game = random_game(game_id=game_id)
        expected_response = SearchGameResponse(
            GameResponse(
                game.game_id.game_id,
                game.first_peg.peg_type,
                game.second_peg.peg_type,
                game.third_peg.peg_type,
                game.fourth_peg.peg_type
            )
        )

        self.should_find_game(game_id, game)

        self.assertEqual(
            self.handler.handle(query),
            expected_response
        )

    def test_should_not_find_unexisting_game(self):
        query = random_search_game_query()

        game_id = random_game_id(query.game_id)
        expected_response = SearchGameResponse(None)

        self.should_not_find_game(game_id)

        self.assertEqual(
            self.handler.handle(query),
            expected_response
        )
