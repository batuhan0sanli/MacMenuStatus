from rumps import Timer, MenuItem, separator, quit_application
from static.mac_menu_status_icons import MacMenuStatusIcons
import src.app as app


class UpdateTimer:
    def __init__(self, sender: 'app.MacMenuStatus', interval: float):
        self.sender = sender
        self.interval = interval
        self._timer = Timer(self._callback, self.interval)

    def _callback(self, _=None):
        self.sender.widgets.update()
        if self.sender.widgets.menubar_status.name == 'ERROR':
            if self.sender.icon_timer is None:
                self.sender.icon_timer = MacMenuStatusIcons.error_flip_flop(self.sender)
                self.sender.icon_timer.start()
        else:
            if self.sender.icon_timer is not None:
                self.sender.icon_timer.stop()
                self.sender.icon_timer = None
            self.sender.icon = self.sender.widgets.menubar_status.value
        self.update_menu_items()

    def update_menu_items(self):
        self.sender.menu.clear()
        for widget in self.sender.widgets:
            self.sender.menu.add(widget.menu_item)
        self.sender.menu.add(separator)
        self.sender.menu.add(MenuItem(title="Quit", callback=quit_application))

    def start(self):
        self._timer.start()

    def stop(self):
        self._timer.stop()

    def __del__(self):
        self.stop()
