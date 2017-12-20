import abc
from typing import Optional

from mastermind.module.game.domain.model.game import Game
from mastermind.module.shared.domain.model.game_id import GameId


class GameRepository(abc.ABC):
    @abc.abstractmethod
    def insert(self, game: Game) -> None:
        pass

    def search(self, game_id: GameId) -> Optional[Game]:
        pass
