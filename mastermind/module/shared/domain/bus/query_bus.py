import abc


class QueryBus(abc.ABC):
    @abc.abstractmethod
    def ask(self, query):
        pass
