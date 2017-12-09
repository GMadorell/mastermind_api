from mastermind.module.game.application.create_game_use_case \
    import CreateGameCommand
from mastermind.module.game.test.infrastructure.random.random_code_peg \
    import random_code_peg
from mastermind.module.game.test.infrastructure.random.random_game_id \
    import random_game_id


def random_create_game_command(
        game_id: str = random_game_id().game_id,
        first_peg: str = random_code_peg().peg_type,
        second_peg: str = random_code_peg().peg_type,
        third_peg: str = random_code_peg().peg_type,
        fourth_peg: str = random_code_peg().peg_type) -> CreateGameCommand:
    return CreateGameCommand(
        game_id,
        first_peg,
        second_peg,
        third_peg,
        fourth_peg
    )
