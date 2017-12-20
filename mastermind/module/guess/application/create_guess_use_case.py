from typing import NamedTuple

from mastermind.module.game.application.search_game_use_case import SearchGameResponse, SearchGameQuery
from mastermind.module.guess.domain.error.guess_errors import GuessesLimitExceeded, GuessAlreadyExists, GameNotFound
from mastermind.module.guess.domain.guess_repository import GuessRepository
from mastermind.module.guess.domain.model.guess import Guess
from mastermind.module.guess.domain.model.guess_id import GuessId
from mastermind.module.shared.domain.bus.query_bus import QueryBus
from mastermind.module.shared.domain.model.code_peg import CodePeg
from mastermind.module.shared.domain.model.game_id import GameId


class GuessCreator:
    MAX_GUESSES_PER_GAME = 10

    def __init__(self, guess_repository: GuessRepository, query_bus: QueryBus):
        self.guess_repository = guess_repository
        self.query_bus = query_bus

    def create(self,
               guess_id: GuessId,
               game_id: GameId,
               first_code_peg: CodePeg,
               second_code_peg: CodePeg,
               third_code_peg: CodePeg,
               fourth_code_peg: CodePeg) -> None:

        if not self._game_exists(game_id):
            raise GameNotFound(game_id)
        if self._guess_exists(guess_id):
            raise GuessAlreadyExists(guess_id)
        if self._too_many_guesses(game_id):
            raise GuessesLimitExceeded(game_id, self.MAX_GUESSES_PER_GAME)
        else:
            self.guess_repository.insert(
                Guess(guess_id,
                      game_id,
                      first_code_peg,
                      second_code_peg,
                      third_code_peg,
                      fourth_code_peg))

    def _game_exists(self, game_id: GameId) -> bool:
        response: SearchGameResponse = self.query_bus.ask(SearchGameQuery(game_id.game_id))
        return response.maybe_game_response is not None

    def _guess_exists(self, guess_id: GuessId) -> bool:
        return self.guess_repository.search(guess_id) is not None

    def _too_many_guesses(self, game_id: GameId) -> bool:
        game_guesses = self.guess_repository.search_by_game_id(game_id)
        return len(game_guesses) >= self.MAX_GUESSES_PER_GAME


CreateGuessCommand = NamedTuple("CreateGuessCommand",
                                [("guess_id", str),
                                 ("game_id", str),
                                 ("first_code_peg", int),
                                 ("second_code_peg", int),
                                 ("third_code_peg", int),
                                 ("fourth_code_peg", int)])


class CreateGuessCommandHandler:
    def __init__(self, creator: GuessCreator):
        self.creator = creator

    def handle(self, command: CreateGuessCommand) -> None:
        guess_id = GuessId(command.guess_id)
        game_id = GameId(command.game_id)
        first_code_peg = CodePeg(command.first_code_peg)
        second_code_peg = CodePeg(command.second_code_peg)
        third_code_peg = CodePeg(command.third_code_peg)
        fourth_code_peg = CodePeg(command.fourth_code_peg)
        self.creator.create(
            guess_id,
            game_id,
            first_code_peg,
            second_code_peg,
            third_code_peg,
            fourth_code_peg
        )
