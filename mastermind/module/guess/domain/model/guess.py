from typing import NamedTuple

from mastermind.module.guess.domain.model.guess_id import GuessId
from mastermind.module.shared.domain.model.code_peg import CodePeg
from mastermind.module.shared.domain.model.game_id import GameId

Guess = NamedTuple("Guess", [
    ("guess_id", GuessId),
    ("game_id", GameId),
    ("first_peg", CodePeg),
    ("second_peg", CodePeg),
    ("third_peg", CodePeg),
    ("fourth_peg", CodePeg)])
