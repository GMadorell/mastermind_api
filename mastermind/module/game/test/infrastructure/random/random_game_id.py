from typing import Optional

from mastermind.module.shared.domain.model.game_id import GameId
from mastermind.module.shared.test.infrastructure.random.random_element import random_element
from mastermind.module.shared.test.infrastructure.random.random_uuid \
    import random_uuid
from mastermind.module.shared.test.infrastructure.string.string_utils import remove_random_char


def random_game_id(game_id: Optional[str] = None) -> GameId:
    game_id = random_uuid() if game_id is None else game_id
    return GameId(game_id)


def invalid_game_id()-> str:
    return random_element(["", remove_random_char(random_uuid())])
