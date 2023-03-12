from rumps import App

from src.builders import WidgetBuilder
from src.builders.timer_builder import TimerBuilder
from src.config import Config
from src.containers import TimerContainer
from src.timers import UpdateTimer, ErrorFlipFlop
from static import AppIcons


class MacMenuStatus(App):
    def __init__(self, config: 'Config'):
        self.config = config
        self.widgets = WidgetBuilder(self).build()
        self.timers = TimerBuilder(self).build()
        super(MacMenuStatus, self).__init__(name="MacMenuStatus", title='', icon=AppIcons.pending_logo_black)

    def run(self):
        super(MacMenuStatus, self).run()
