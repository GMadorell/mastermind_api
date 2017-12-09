from typing import NamedTuple

from mastermind.module.shared.domain.validation.validation_exception\
    import ValidationException


class CodePeg(NamedTuple("CodePeg", [("peg_type", int)])):
    MAX_CODE_PEG_TYPES = 6

    def __new__(cls, peg_type: int):
        cls.guard_is_in_valid_range(peg_type)
        return super(CodePeg, cls).__new__(cls, peg_type)

    @staticmethod
    def guard_is_in_valid_range(peg_type: int):
        if not CodePeg.is_in_valid_range(peg_type):
            raise ValidationException(
                "Given peg_type '{}' was not in valid range.".format(peg_type))

    @staticmethod
    def is_in_valid_range(peg_type: int) -> bool:
        return 0 <= peg_type < CodePeg.MAX_CODE_PEG_TYPES
