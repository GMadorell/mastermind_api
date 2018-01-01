import unittest
from unittest.mock import MagicMock

from mastermind.module.game.domain.game_repository import GameRepository
from mastermind.module.game.domain.model.game import Game
from mastermind.module.shared.domain.model.game_id import GameId


class GameBehaviourSpec(unittest.TestCase):

    def setUp(self):
        super().setUp()
        GameRepository.__abstractmethods__ = frozenset()
        self.game_repository = GameRepository()
        self.game_repository.insert = MagicMock()
        self.game_repository.search = MagicMock()

        self.mock_assertions = []

    def tearDown(self):
        for assertion in self.mock_assertions:
            assertion()

    def should_not_find_game(self, game_id: GameId):
        self.game_repository.search.return_value = None
        self.mock_assertions.append(
            lambda: self.game_repository
                        .search
                        .assert_called_once_with(game_id)
        )

    def should_find_game(self, game_id: GameId, game: Game):
        self.game_repository.search.return_value = game
        self.mock_assertions.append(
            lambda: self.game_repository
                        .search
                        .assert_called_once_with(game_id)
        )

    def should_insert_game(self, game: Game) -> None:
        self.mock_assertions.append(
            lambda: self.game_repository.insert.assert_called_once_with(game))
