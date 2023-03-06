from rumps import Timer

import src.app as app
from static.mac_menu_status_icons import MacMenuStatusIcons


class ErrorFlipFlop:
    def __init__(self, sender: 'app.MacMenuStatus', interval: float):
        self.sender = sender
        self.interval = interval
        self._timer = Timer(self._callback, self.interval)

    def _callback(self, _=None):
        if self.sender.icon == MacMenuStatusIcons.red_logo:
            self.sender.icon = MacMenuStatusIcons.black_logo
        else:
            self.sender.icon = MacMenuStatusIcons.red_logo

    def start(self):
        self._timer.start()

    def stop(self):
        self._timer.stop()

    def __del__(self):
        self.stop()
