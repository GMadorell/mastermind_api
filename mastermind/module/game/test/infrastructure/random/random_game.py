from mastermind.module.game.domain.model.code_peg import CodePeg
from mastermind.module.game.domain.model.game import Game
from mastermind.module.game.domain.model.game_id import GameId
from mastermind.module.game.test.infrastructure.random.random_code_peg import random_code_peg
from mastermind.module.game.test.infrastructure.random.random_game_id import random_game_id


def random_game(game_id: GameId = random_game_id(),
                first_peg: CodePeg = random_code_peg(),
                second_peg: CodePeg = random_code_peg(),
                third_peg: CodePeg = random_code_peg(),
                fourth_peg: CodePeg = random_code_peg()) -> Game:
    game_id = random_game_id() if game_id is None else game_id
    first_peg = random_code_peg() if first_peg is None else first_peg
    second_peg = random_code_peg() if second_peg is None else second_peg
    third_peg = random_code_peg() if third_peg is None else third_peg
    fourth_peg = random_code_peg() if fourth_peg is None else fourth_peg

    return Game(game_id, first_peg, second_peg, third_peg, fourth_peg)
