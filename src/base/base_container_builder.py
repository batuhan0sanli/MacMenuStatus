from abc import ABC, abstractmethod
# from src.base import BaseContainer


class BaseContainerBuilder(ABC):
    _container: 'BaseContainer'

    def __init__(self, sender):
        self._sender = sender
        self.container_instance = self._container(self._sender) if self._container else None

    @abstractmethod
    def build(self) -> 'BaseContainer':
        pass
