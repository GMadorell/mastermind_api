import abc
from typing import List, Optional

from mastermind.module.guess.domain.model.guess import Guess
from mastermind.module.guess.domain.model.guess_id import GuessId
from mastermind.module.shared.domain.model.game_id import GameId


class GuessRepository(abc.ABC):
    @abc.abstractmethod
    def insert(self, guess: Guess) -> None:
        pass

    def search(self, guess_id: GuessId) -> Optional[Guess]:
        pass

    def search_by_game_id(self, game_id: GameId) -> List[Guess]:
        pass
