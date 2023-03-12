from src.base import BaseContainerBuilder
from src.containers import TimerContainer
from src.timers import UpdateTimer, ErrorFlipFlop

__all__ = ['TimerBuilder']


class TimerBuilder(BaseContainerBuilder):
    _container = TimerContainer

    def build(self) -> 'TimerContainer':
        updater_timer = UpdateTimer(self._sender, self._sender.config.get('update_interval', 10))
        error_flip_flop_timer = ErrorFlipFlop(self._sender, 0.5)

        self.container_instance.add(updater_timer, start=True)
        self.container_instance.add(error_flip_flop_timer)
        return self.container_instance
