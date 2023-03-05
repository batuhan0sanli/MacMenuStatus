from rumps import App, MenuItem, Timer, separator, quit_application

from src.base import Widgets
from src.config import Config
from static.mac_menu_status_icons import MacMenuStatusIcons


class MacMenuStatus(App):
    def __init__(self, config: 'Config', widgets: 'Widgets'):
        self.widgets = widgets
        self.timer = Timer(self._update_title, config.get('update_interval', 10))
        self.icon_timer = None
        super(MacMenuStatus, self).__init__(name="MacMenuStatus", title='', icon=MacMenuStatusIcons.black_logo)
        self._add_menu_items()

    def _add_menu_items(self):
        for widget in self.widgets:
            self.menu.add(widget.menu_item)
        self.menu.add(separator)
        self.menu.add(MenuItem(title="Quit", callback=quit_application))

    def _update_title(self, _=None):
        self.widgets.update()
        if self.widgets.menubar_status.name == 'ERROR':
            if self.icon_timer is None:
                self.icon_timer = MacMenuStatusIcons.error_flip_flop(self)
                self.icon_timer.start()
        else:
            if self.icon_timer is not None:
                self.icon_timer.stop()
                self.icon_timer = None
            self.icon = self.widgets.menubar_status.value

        self.menu.clear()
        self._add_menu_items()

    def run(self):
        self.timer.start()
        super(MacMenuStatus, self).run()
