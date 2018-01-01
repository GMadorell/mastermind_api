from records import Database

from mastermind.infrastructure.configuration.configuration\
    import Configuration
from mastermind.module.game.application.create_game_use_case\
    import CreateGameCommandHandler, GameCreator
from mastermind.module.game.application.search_game_use_case\
    import SearchGameQueryHandler, SearchGameQuery
from mastermind.module.game.domain.game_repository import GameRepository
from mastermind.module.game.infrastructure.persistence\
    .mysql_game_repository import MySQLGameRepository
from mastermind.module.guess.application.create_guess_use_case import \
    CreateGuessCommandHandler, GuessCreator
from mastermind.module.guess.domain.guess_repository import GuessRepository
from mastermind.module.guess.infrastructure.persistence.mysql_guess_repository\
    import MySQLGuessRepository
from mastermind.module.shared.domain.bus.query_bus import QueryBus
from mastermind.module.shared.infrastructure.bus.simple_query_bus\
    import SimpleQueryBus


class Context:
    def __init__(self):
        self.configuration = Configuration()

        self.database = Database(self.configuration.database.url)

        self.game_repository: GameRepository = MySQLGameRepository(
            self.database)
        self.create_game_command_handler = CreateGameCommandHandler(
            GameCreator(self.game_repository))
        self.search_game_query_handler = SearchGameQueryHandler(
            self.game_repository)

        self.query_bus: QueryBus = SimpleQueryBus({
            SearchGameQuery.__name__: self.search_game_query_handler
        })

        self.guess_repository: GuessRepository = MySQLGuessRepository(
            self.database)
        self.create_guess_command_handler = \
            CreateGuessCommandHandler(GuessCreator(
                self.guess_repository, self.query_bus))

    def tear_down(self):
        self.database.close()
