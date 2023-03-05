from rumps import App, MenuItem, Timer, separator, quit_application

from src.base import Widgets
from src.config import Config
from static.mac_menu_status_icons import MacMenuStatusIcons


class MacMenuStatus(App):
    def __init__(self, config: 'Config', widgets: 'Widgets'):
        self.widgets = widgets
        self.timer = Timer(self._update_title, config.get('update_interval', 10))
        super(MacMenuStatus, self).__init__(name="MacMenuStatus", title='', icon=MacMenuStatusIcons.black_logo)
        self._add_menu_items()

    def _add_menu_items(self):
        for widget in self.widgets:
            self.menu.add(widget.menu_item)
        self.menu.add(separator)
        self.menu.add(MenuItem(title="Quit", callback=quit_application))

    def _update_title(self, _=None):
        self.widgets.update()
        self.icon = self.widgets.menubar_status.value
        self.menu.clear()
        self._add_menu_items()

    def run(self):
        self.timer.start()
        super(MacMenuStatus, self).run()
