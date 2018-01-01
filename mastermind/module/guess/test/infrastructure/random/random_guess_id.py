from mastermind.module.guess.domain.model.guess_id import GuessId
from mastermind.module.shared.test.infrastructure.random.random_element import random_element
from mastermind.module.shared.test.infrastructure.random.random_uuid import random_uuid
from mastermind.module.shared.test.infrastructure.string.string_utils import remove_random_char


def random_guess_id(guess_id: str = None) -> GuessId:
    guess_id = random_uuid() if guess_id is None else guess_id
    return GuessId(guess_id)


def invalid_guess_id() -> str:
    return random_element(["", remove_random_char(random_uuid())])
