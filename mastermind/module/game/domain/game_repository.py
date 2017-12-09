import abc

from mastermind.module.game.domain.model.game import Game


class GameRepository(abc.ABC):
    @abc.abstractmethod
    def insert(self, game: Game) -> None:
        pass
