from typing import List, Tuple, Type, Dict

from mastermind.module.shared.domain.bus.query_bus import QueryBus


class SimpleQueryBus(QueryBus):
    def __init__(self, handlers: Dict):
        """
        @:param handlers: Dict[QueryType, QueryHandler]
        """
        self.__handlers = handlers

    def ask(self, query):
        query_type = query.__class__.__name__
        handler = self.__handlers[query_type]
        return handler.handle(query)
