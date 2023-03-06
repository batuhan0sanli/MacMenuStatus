from src.base import BaseTimer
from static.mac_menu_status_icons import MacMenuStatusIcons


class ErrorFlipFlop(BaseTimer):
    def _callback(self, _=None):
        if self.sender.icon == MacMenuStatusIcons.red_logo:
            self.sender.icon = MacMenuStatusIcons.black_logo
        else:
            self.sender.icon = MacMenuStatusIcons.red_logo
