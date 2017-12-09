from typing import NamedTuple

from mastermind.module.game.domain.game_repository import GameRepository
from mastermind.module.game.domain.model.code_peg import CodePeg
from mastermind.module.game.domain.model.game import Game
from mastermind.module.game.domain.model.game_id import GameId


class GameCreator:
    def __init__(self, game_repository: GameRepository):
        self.game_repository = game_repository

    def create(self,
               game_id: GameId,
               first_code_peg: CodePeg,
               second_code_peg: CodePeg,
               third_code_peg: CodePeg,
               fourth_code_peg: CodePeg) -> None:
        self.game_repository.insert(
            Game(game_id,
                 first_code_peg,
                 second_code_peg,
                 third_code_peg,
                 fourth_code_peg))


CreateGameCommand = NamedTuple("CreateGameCommand",
                               [("game_id", GameId),
                                ("first_code_peg", CodePeg),
                                ("second_code_peg", CodePeg),
                                ("third_code_peg", CodePeg),
                                ("fourth_code_peg", CodePeg)])


class CreateGameCommandHandler:
    def __init__(self, creator: GameCreator):
        self.creator = creator

    def handle(self, command: CreateGameCommand) -> None:
        game_id = GameId(command.game_id)
        first_code_peg = CodePeg(command.first_code_peg)
        second_code_peg = CodePeg(command.first_code_peg)
        third_code_peg = CodePeg(command.first_code_peg)
        fourth_code_peg = CodePeg(command.first_code_peg)
        self.creator.create(game_id, first_code_peg,
                            second_code_peg, third_code_peg, fourth_code_peg)
