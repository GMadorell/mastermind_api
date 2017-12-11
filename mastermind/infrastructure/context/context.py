from records import Database

from mastermind.infrastructure.configuration.configuration import Configuration
from mastermind.module.game.application.create_game_use_case import CreateGameCommandHandler, GameCreator
from mastermind.module.game.domain.game_repository import GameRepository
from mastermind.module.game.infrastructure.persistence.mysql_game_repository import MySQLGameRepository


class Context:
    def __init__(self):
        self.configuration = Configuration()

        self.database = Database(self.configuration.database.url)

        self.game_repository: GameRepository = MySQLGameRepository(self.database)
        self.create_game_command_handler = CreateGameCommandHandler(GameCreator(self.game_repository))

    def tear_down(self):
        self.database.close()
