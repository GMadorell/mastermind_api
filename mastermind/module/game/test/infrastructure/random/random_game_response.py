from mastermind.module.game.application.search_game_use_case\
    import GameResponse
from mastermind.module.game.test.infrastructure.random.random_code_peg\
    import random_code_peg
from mastermind.module.game.test.infrastructure.random.random_game_id\
    import random_game_id


def random_game_response(game_id: str = None,
                         first_peg: str = None,
                         second_peg: str = None,
                         third_peg: str = None,
                         fourth_peg: str = None)->GameResponse:
    game_id = random_game_id().game_id if game_id is None \
        else game_id
    first_peg = random_code_peg().peg_type if first_peg is None \
        else first_peg
    second_peg = random_code_peg().peg_type if second_peg is None \
        else second_peg
    third_peg = random_code_peg().peg_type if third_peg is None\
        else third_peg
    fourth_peg = random_code_peg().peg_type if fourth_peg is None\
        else fourth_peg

    return GameResponse(
        game_id,
        first_peg,
        second_peg,
        third_peg,
        fourth_peg
    )
