from rumps import MenuItem, separator, quit_application

from src.base import BaseTimer
from src.timers.error_flip_flop import ErrorFlipFlop


class UpdateTimer(BaseTimer):
    def _callback(self, _=None):
        self.sender.widgets.update()
        self.update_flip_flop()
        self.update_menu_items()

    def update_menu_items(self):
        self.sender.menu.clear()
        for widget in self.sender.widgets:
            self.sender.menu.add(widget.menu_item)
        self.sender.menu.add(separator)
        self.sender.menu.add(MenuItem(title="Quit", callback=quit_application))

    def update_flip_flop(self):
        if self.sender.widgets.menubar_status.name == 'ERROR':
            if self.sender.icon_timer is None:
                self.sender.icon_timer = ErrorFlipFlop(self.sender, 0.5)
                self.sender.icon_timer.start()
        else:
            if self.sender.icon_timer is not None:
                self.sender.icon_timer.stop()
                self.sender.icon_timer = None
            self.sender.icon = self.sender.widgets.menubar_status.value
