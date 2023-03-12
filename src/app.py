from rumps import App

from src.builders import TimerBuilder
from src.builders import WidgetBuilder
from src.config import Config
from src.containers import TimerContainer
from src.containers import WidgetContainer
from static import AppIcons


class MacMenuStatus(App):
    def __init__(self, config: 'Config'):
        self.config: 'Config' = config
        self.widgets: 'WidgetContainer' = WidgetBuilder(self).build()
        self.timers: 'TimerContainer' = TimerBuilder(self).build()
        super(MacMenuStatus, self).__init__(name="MacMenuStatus", title='', icon=AppIcons.pending_logo_black)

    def run(self):
        super(MacMenuStatus, self).run()
