from typing import NamedTuple

from mastermind.module.shared.domain.validation.uuid_check import is_uuid
from mastermind.module.shared.domain.validation.validation_exception\
    import ValidationException


class GuessId(NamedTuple("GameId", [("guess_id", str)])):
    def __new__(cls, guess_id: str):
        GuessId.guard_is_uuid(guess_id)
        return super(GuessId, cls).__new__(cls, guess_id)

    @staticmethod
    def guard_is_uuid(guess_id: str) -> None:
        if not is_uuid(guess_id):
            raise ValidationException(
                "Given guess_id '{}' was not a correct uuid".format(guess_id))
