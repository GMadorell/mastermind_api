from mastermind.module.game.application.search_game_use_case \
    import SearchGameQuery
from mastermind.module.game.test.infrastructure.random.random_game_id\
    import random_game_id


def random_search_game_query(game_id: str = None)-> SearchGameQuery:
    game_id = random_game_id().game_id if game_id is None else game_id
    return SearchGameQuery(game_id)
