import abc

from mastermind.module.shared.domain.model.game_id import GameId


class GameError(abc.ABC, Exception):
    pass


class GameAlreadyExists(GameError):
    def __init__(self, game_id: GameId) -> None:
        super(Exception, self).__init__(
            "Game with game_id '{}' already exists.".format(game_id.game_id)
        )
