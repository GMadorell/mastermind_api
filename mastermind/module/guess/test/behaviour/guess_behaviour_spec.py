import unittest
from typing import List
from unittest.mock import MagicMock

from mastermind.module.guess.domain.guess_repository import GuessRepository
from mastermind.module.guess.domain.model.guess import Guess
from mastermind.module.guess.domain.model.guess_id import GuessId
from mastermind.module.shared.domain.bus.query_bus import QueryBus
from mastermind.module.shared.domain.model.game_id import GameId


class GuessBehaviourSpec(unittest.TestCase):
    def setUp(self):
        super().setUp()
        GuessRepository.__abstractmethods__ = frozenset()
        self.guess_repository = GuessRepository()
        self.guess_repository.insert = MagicMock()
        self.guess_repository.search = MagicMock()
        self.guess_repository.search_by_game_id = MagicMock()

        QueryBus.__abstractmethods__ = frozenset()
        self.query_bus = QueryBus()
        self.query_bus.ask = MagicMock()

        self.mock_assertions = []

    def tearDown(self):
        for assertion in self.mock_assertions:
            assertion()

    def should_not_find_guess(self, guess_id: GuessId):
        self.guess_repository.search.return_value = None
        self.mock_assertions.append(
            lambda: self.guess_repository
                        .search
                        .assert_called_once_with(guess_id)
        )

    def should_find_guess(self, guess_id: GuessId, guess: Guess):
        self.guess_repository.search.return_value = guess
        self.mock_assertions.append(
            lambda: self.guess_repository
                        .search
                        .assert_called_once_with(guess_id)
        )

    def should_find_guesses_by_game_id(
            self,
            game_id: GameId,
            guesses: List[Guess]
    ):
        self.guess_repository.search_by_game_id.return_value = guesses
        self.mock_assertions.append(
            lambda: self.guess_repository
                        .search_by_game_id
                        .assert_called_once_with(game_id)
        )

    def should_insert_guess(self, guess: Guess) -> None:
        self.mock_assertions.append(
            lambda: self.guess_repository.insert.assert_called_once_with(guess)
        )

    def should_ask_query(self, query, response) -> None:
        self.query_bus.ask.return_value = response
        self.mock_assertions.append(
            lambda: self.query_bus.ask.assert_called_once_with(query))
