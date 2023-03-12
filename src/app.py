from rumps import App

from src.builders import WidgetBuilder
from src.config import Config
from src.containers import TimerContainer
from src.timers import UpdateTimer, ErrorFlipFlop
from static import AppIcons


class MacMenuStatus(App):
    def __init__(self, config: 'Config'):
        self.config = config
        self.widgets = WidgetBuilder(self).build()
        self.timers = TimerContainer(self)
        super(MacMenuStatus, self).__init__(name="MacMenuStatus", title='', icon=AppIcons.pending_logo_black)

        self._initialize_timers()

    def _initialize_timers(self):
        updater_timer = UpdateTimer(self, self.config.get('update_interval', 10))
        error_flip_flop_timer = ErrorFlipFlop(self, 0.5)
        self.timers.add(updater_timer, start=True)
        self.timers.add(error_flip_flop_timer)

    def run(self):
        super(MacMenuStatus, self).run()
