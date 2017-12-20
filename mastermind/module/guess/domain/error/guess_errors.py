import abc

from mastermind.module.guess.domain.model.guess_id import GuessId
from mastermind.module.shared.domain.model.game_id import GameId


class GuessError(abc.ABC, Exception):
    pass


class GuessAlreadyExists(GuessError):
    def __init__(self, guess_id: GuessId) -> None:
        super(Exception, self).__init__(
            "Guess with guess_id '{}' already exists.".format(guess_id.guess_id)
        )


class GuessesLimitExceeded(GuessError):
    def __init__(self, game_id: GameId, limit: int) -> None:
        msg = "Game with game_id '{}' can't exceed limit of '{}' guesses.".format(game_id.game_id, limit)
        super(Exception, self).__init__(msg)


class GameNotFound(GuessError):
    def __init__(self, game_id: GameId) -> None:
        super(Exception, self).__init__(
            "Game with game_id '{}' didn't exist.".format(game_id.game_id)
        )
