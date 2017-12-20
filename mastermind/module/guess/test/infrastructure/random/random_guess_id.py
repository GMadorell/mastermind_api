from mastermind.module.guess.domain.model.guess_id import GuessId
from mastermind.module.shared.test.infrastructure.random.random_uuid import random_uuid


def random_guess_id(guess_id: str = None)-> GuessId:
    guess_id = random_uuid() if guess_id is None else guess_id
    return GuessId(guess_id)
