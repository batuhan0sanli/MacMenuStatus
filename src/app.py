from rumps import App

from src.base import Widgets
from src.config import Config
from static.mac_menu_status_icons import MacMenuStatusIcons
from src.timers import UpdateTimer, ErrorFlipFlop


class MacMenuStatus(App):
    def __init__(self, config: 'Config', widgets: 'Widgets'):
        self.widgets = widgets
        self.timer: UpdateTimer = UpdateTimer(self, config.get('update_interval', 10))
        self.icon_timer: ErrorFlipFlop | None = None
        super(MacMenuStatus, self).__init__(name="MacMenuStatus", title='', icon=MacMenuStatusIcons.black_logo)

    def run(self):
        self.timer.start()
        super(MacMenuStatus, self).run()
