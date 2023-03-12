from src.base.base_timer import BaseTimer


class TimerContainer:
    def __init__(self, sender):
        self._sender = sender
        self._timers = dict()

    def add(self, timer: BaseTimer, name: str = None, start: bool = False):
        if not name:
            name = timer.name or timer.__class__.__name__ + str(id(timer))
        timer.name = name
        timer.sender = self._sender
        self._timers[name] = timer
        if start:
            timer.start()

    def start(self):
        for timer in self._timers.values():
            timer.start()

    def stop(self):
        for timer in self._timers.values():
            timer.stop()

    def __iter__(self):
        return iter(self._timers.values())

    def __getitem__(self, item):
        return self._timers[item]

    def __len__(self):
        return len(self._timers)

    def __repr__(self):
        return f"<TimerContainer: {self._timers}>"

    def __str__(self):
        return f"<TimerContainer: {self._timers}>"

    def __del__(self):
        self.stop()
