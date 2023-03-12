from rumps import MenuItem, separator, quit_application

from src.base import BaseTimer


class Updater(BaseTimer):
    name = 'Updater'

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
        if self.sender.widgets.global_status.name == 'ERROR':
            self.sender.timers['ErrorFlipFlop'].start()
        else:
            self.sender.timers['ErrorFlipFlop'].stop()
            self.sender.icon = self.sender.widgets.global_status.value
