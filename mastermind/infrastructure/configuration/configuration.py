import os
from typing import NamedTuple

from pyhocon import ConfigFactory

DatabaseConfig = NamedTuple("DatabaseConfig", [("url", str)])


class Configuration:
    def __init__(self) -> None:
        config_path = os.environ["MASTERMIND_CONFIG"]
        parsed_config = ConfigFactory.parse_file(config_path)

        self.database = DatabaseConfig(parsed_config["database"]["url"])
