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
    return Game(game_id, first_peg, second_peg, third_peg, fourth_peg)
