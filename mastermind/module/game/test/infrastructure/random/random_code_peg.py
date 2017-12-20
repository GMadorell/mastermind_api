import random

from mastermind.module.shared.domain.model.code_peg import CodePeg
from mastermind.module.shared.test.infrastructure.random.random_element import random_element


def random_code_peg(peg_type: int = None) -> CodePeg:
    peg_type = random_element(range(0, 6)) if peg_type is None else peg_type
    return CodePeg(peg_type)


def invalid_code_peg()->int:
    return random_element([-1, random.randrange(7, 20)])
