from typing import NamedTuple

from mastermind.module.game.domain.error.game_errors import GameAlreadyExists
from mastermind.module.game.domain.game_repository import GameRepository
from mastermind.module.game.domain.model.game import Game
from mastermind.module.shared.domain.model.code_peg import CodePeg
from mastermind.module.shared.domain.model.game_id import GameId


class GameCreator:
    def __init__(self, game_repository: GameRepository):
        self.game_repository = game_repository

    def create(self,
               game_id: GameId,
               first_code_peg: CodePeg,
               second_code_peg: CodePeg,
               third_code_peg: CodePeg,
               fourth_code_peg: CodePeg) -> None:

        maybe_game = self.game_repository.search(game_id)
        if maybe_game is not None:
            raise GameAlreadyExists(game_id)
        else:
            self.game_repository.insert(
                Game(game_id,
                     first_code_peg,
                     second_code_peg,
                     third_code_peg,
                     fourth_code_peg))


CreateGameCommand = NamedTuple("CreateGameCommand",
                               [("game_id", str),
                                ("first_code_peg", int),
                                ("second_code_peg", int),
                                ("third_code_peg", int),
                                ("fourth_code_peg", int)])


class CreateGameCommandHandler:
    def __init__(self, creator: GameCreator):
        self.creator = creator

    def handle(self, command: CreateGameCommand) -> None:
        game_id = GameId(command.game_id)
        first_code_peg = CodePeg(command.first_code_peg)
        second_code_peg = CodePeg(command.second_code_peg)
        third_code_peg = CodePeg(command.third_code_peg)
        fourth_code_peg = CodePeg(command.fourth_code_peg)
        self.creator.create(game_id, first_code_peg,
                            second_code_peg, third_code_peg, fourth_code_peg)
