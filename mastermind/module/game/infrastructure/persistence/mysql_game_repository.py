from typing import Optional

from records import Database

from mastermind.module.game.domain.game_repository import GameRepository
from mastermind.module.game.domain.model.game import Game
from mastermind.module.shared.domain.model.code_peg import CodePeg
from mastermind.module.shared.domain.model.game_id import GameId


class MySQLGameRepository(GameRepository):
    def __init__(self, database: Database):
        self.database = database

    def insert(self, game: Game) -> None:
        self.database.query(
            """
            INSERT INTO games
            (game_id, first_code_peg, second_code_peg, third_code_peg, fourth_code_peg)
            VALUES
            ('{}', '{}', '{}', '{}', '{}')
            """.format(game.game_id.game_id, game.first_peg.peg_type, game.second_peg.peg_type, game.third_peg.peg_type,
                       game.fourth_peg.peg_type))

    def search(self, game_id: GameId) -> Optional[Game]:
        maybe_record = self.database.query(
            """select * from games where game_id = '{}'""".format(game_id.game_id)).first()
        if maybe_record is None:
            return None
        else:
            game_raw_data = maybe_record.as_dict()
            return Game(GameId(game_raw_data["game_id"]), CodePeg(game_raw_data["first_code_peg"]),
                        CodePeg(game_raw_data["second_code_peg"]), CodePeg(game_raw_data["third_code_peg"]),
                        CodePeg(game_raw_data["fourth_code_peg"]))
