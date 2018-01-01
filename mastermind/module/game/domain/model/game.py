from typing import NamedTuple

from mastermind.module.shared.domain.model.code_peg import CodePeg
from mastermind.module.shared.domain.model.game_id import GameId

Game = NamedTuple("Game", [
    ("game_id", GameId),
    ("first_peg", CodePeg),
    ("second_peg", CodePeg),
    ("third_peg", CodePeg),
    ("fourth_peg", CodePeg)])
