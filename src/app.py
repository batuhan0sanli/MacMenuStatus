from rumps import App

from src.base import Widgets
from src.config import Config
from src.timer_container import TimerContainer
from src.timers import UpdateTimer, ErrorFlipFlop
from static import AppIcons


class MacMenuStatus(App):
    def __init__(self, config: 'Config', widgets: 'Widgets'):
        self.widgets = widgets
        self.config = config
        self.timers = TimerContainer(self)
        super(MacMenuStatus, self).__init__(name="MacMenuStatus", title='', icon=AppIcons.pending_logo_black)

        self._initialize_timers()

    def _initialize_timers(self):
        self.timers.add(UpdateTimer(self, self.config.get('update_interval', 10)))
        self.timers.add(ErrorFlipFlop(self, 0.5))

    def run(self):
        self.timers.start()
        super(MacMenuStatus, self).run()
