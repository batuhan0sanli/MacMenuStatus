from src.base import BaseTimer
from static import AppIcons


class ErrorFlipFlop(BaseTimer):
    def _callback(self, _=None):
        if self.sender.icon == AppIcons.red_logo:
            self.sender.icon = AppIcons.black_logo
        else:
            self.sender.icon = AppIcons.red_logo
