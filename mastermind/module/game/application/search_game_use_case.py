from typing import NamedTuple, Optional

from mastermind.module.game.domain.game_repository import GameRepository
from mastermind.module.game.domain.model.game import Game
from mastermind.module.shared.domain.model.game_id import GameId


SearchGameQuery = NamedTuple("SearchGameQuery",
                             [("game_id", str)])

GameResponse = NamedTuple("GameResponse",
                          [("game_id", str),
                           ("first_code_peg", int),
                           ("second_code_peg", int),
                           ("third_code_peg", int),
                           ("fourth_code_peg", int)])

SearchGameResponse = NamedTuple("SearchGameResponse",
                                [("maybe_game_response", Optional[GameResponse])])


def game_to_response(game: Game)->GameResponse:
    return GameResponse(
        game.game_id.game_id,
        game.first_peg.peg_type,
        game.second_peg.peg_type,
        game.third_peg.peg_type,
        game.fourth_peg.peg_type
    )


class SearchGameQueryHandler:
    def __init__(self, repository: GameRepository):
        self.repository = repository

    def handle(self, query: SearchGameQuery) -> SearchGameResponse:
        game_id = GameId(query.game_id)
        maybe_game = self.repository.search(game_id)
        if maybe_game is not None:
            return SearchGameResponse(game_to_response(maybe_game))
        else:
            return SearchGameResponse(None)
