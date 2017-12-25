from typing import Optional, List, Dict

from records import Database

from mastermind.module.guess.domain.guess_repository import GuessRepository
from mastermind.module.guess.domain.model.guess import Guess
from mastermind.module.guess.domain.model.guess_id import GuessId
from mastermind.module.shared.domain.model.code_peg import CodePeg
from mastermind.module.shared.domain.model.game_id import GameId


class MySQLGuessRepository(GuessRepository):
    def __init__(self, database: Database):
        self.database = database

    def insert(self, guess: Guess) -> None:
        self.database.query(
            """
            INSERT INTO guesses
            (guess_id, game_id, first_code_peg, second_code_peg, third_code_peg, fourth_code_peg)
            VALUES
            ('{}', '{}', '{}', '{}', '{}', '{}')
            """.format(
                guess.guess_id.guess_id,
                guess.game_id.game_id,
                guess.first_peg.peg_type,
                guess.second_peg.peg_type,
                guess.third_peg.peg_type,
                guess.fourth_peg.peg_type
            )
        )

    def search(self, guess_id: GuessId) -> Optional[Guess]:
        maybe_record = self.database.query(
            """select * from guesses where guess_id = '{}'""".format(guess_id.guess_id)
        ).first(as_dict=True)
        if maybe_record is None:
            return None
        else:
            return self.__record_dict_to_guess(maybe_record)

    def search_by_game_id(self, game_id: GameId) -> List[Guess]:
        records = self.database.query(
            """SELECT * FROM guesses WHERE game_id = '{}'""".format(game_id.game_id)
        ).all(as_dict=True)
        return list(map(self.__record_dict_to_guess, records))

    def __record_dict_to_guess(self, record_as_dict: Dict)-> Guess:
        return Guess(
            GuessId(record_as_dict["guess_id"]),
            GameId(record_as_dict["game_id"]),
            CodePeg(record_as_dict["first_code_peg"]),
            CodePeg(record_as_dict["second_code_peg"]),
            CodePeg(record_as_dict["third_code_peg"]),
            CodePeg(record_as_dict["fourth_code_peg"])
        )
