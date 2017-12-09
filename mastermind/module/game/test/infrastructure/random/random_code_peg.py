import random

from mastermind.module.game.domain.model.code_peg import CodePeg


def random_code_peg(peg_type: int = random.choice(range(0, 6))) -> CodePeg:
    return CodePeg(peg_type)
