from mastermind.module.game.domain.model.game_id import GameId
from mastermind.module.shared.test.infrastructure.random_uuid\
    import random_uuid


def random_game_id(game_id: str = random_uuid()) -> GameId:
    return GameId(game_id)
