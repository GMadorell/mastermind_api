import unittest
from unittest.mock import MagicMock

from mastermind.module.game.domain.game_repository import GameRepository
from mastermind.module.game.domain.model.game import Game


class GameBehaviourSpec(unittest.TestCase):

    def setUp(self):
        super().setUp()
        GameRepository.__abstractmethods__ = frozenset()
        self.game_repository = GameRepository()
        self.game_repository.insert = MagicMock()

    def should_have_inserted_game(self, game: Game) -> None:
        self.game_repository.insert.assert_called_once_with(game)
