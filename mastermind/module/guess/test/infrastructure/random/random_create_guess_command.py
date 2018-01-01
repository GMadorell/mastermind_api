from mastermind.module.game.test.infrastructure.random.random_code_peg\
    import random_code_peg
from mastermind.module.game.test.infrastructure.random.random_game_id\
    import random_game_id
from mastermind.module.guess.application.create_guess_use_case \
    import CreateGuessCommand
from mastermind.module.guess.test.infrastructure.random.random_guess_id \
    import random_guess_id


def random_create_guess_command(
        guess_id: str = None,
        game_id: str = None,
        first_code_peg: int = None,
        second_code_peg: int = None,
        third_code_peg: int = None,
        fourth_code_peg: int = None
) -> CreateGuessCommand:
    guess_id = random_guess_id().guess_id if guess_id is None else guess_id
    game_id = random_game_id().game_id if game_id is None else game_id
    first_code_peg = random_code_peg().peg_type if first_code_peg is None \
        else first_code_peg
    second_code_peg = random_code_peg(
    ).peg_type if second_code_peg is None else second_code_peg
    third_code_peg = random_code_peg().peg_type if third_code_peg is None \
        else third_code_peg
    fourth_code_peg = random_code_peg(
    ).peg_type if fourth_code_peg is None else fourth_code_peg
    return CreateGuessCommand(
        guess_id,
        game_id,
        first_code_peg,
        second_code_peg,
        third_code_peg,
        fourth_code_peg
    )
