import re
from typing import NamedTuple

from mastermind.module.shared.domain.validation.validation_exception\
    import ValidationException


class GameId(NamedTuple("GameId", [("game_id", str)])):
    def __new__(cls, game_id: str):
        GameId.guard_is_uuid(game_id)
        return super(GameId, cls).__new__(cls, game_id)

    @staticmethod
    def guard_is_uuid(string: str) -> None:
        if not is_uuid(string):
            raise ValidationException(
                "Given game_id '{}' was not a correct uuid".format(string))


def is_uuid(string: str) -> bool:
    uuid_regex = re.compile(
        "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
    return uuid_regex.match(string) is not None
