from rumps import App, MenuItem, Timer, separator, quit_application

from src.base import Widgets
from src.config import Config
from static.emoji import Emoji


class MacMenuStatus(App):
    def __init__(self, config: 'Config', widgets: 'Widgets'):
        super(MacMenuStatus, self).__init__(name="MacMenuStatus", title=Emoji.hollow_red_circle)
        self.widgets = widgets
        self.timer = Timer(self._update_title, config.get('update_interval', 10))
        self._add_menu_items()

    def _add_menu_items(self):
        for widget in self.widgets:
            self.menu.add(widget.menu_item)
        self.menu.add(separator)
        self.menu.add(MenuItem(title="Quit", callback=quit_application))

    def _update_title(self, _):
        self.widgets.update()
        self.title = self.widgets.menubar_status.value
        self.menu.clear()
        self._add_menu_items()

    def run(self):
        self.timer.start()
        super(MacMenuStatus, self).run()
