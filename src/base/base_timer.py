from rumps import Timer
from abc import ABC, abstractmethod
import src.app as app


class BaseTimer(ABC):
    def __init__(self, sender: 'app.MacMenuStatus', interval: float):
        self.sender = sender
        self.interval = interval
        self._timer = Timer(self._callback, self.interval)

    @abstractmethod
    def _callback(self, _=None):
        pass

    def start(self):
        self._timer.start()

    def stop(self):
        self._timer.stop()

    def __del__(self):
        self.stop()