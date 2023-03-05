from typing import List

from .base_widget import BaseWidget
from .status import StatusTypes, MenuBarStatusTypes


class Widgets:
    widget_list: List['BaseWidget'] = []
    menubar_status: MenuBarStatusTypes = MenuBarStatusTypes.UNKNOWN
    _instances = None

    def __new__(cls, *args, **kwargs):
        if not cls._instances:
            cls._instances = super(Widgets, cls).__new__(cls)
        return cls._instances

    def add(self, widget: BaseWidget):
        self.widget_list.append(widget)

    def remove(self, widget: BaseWidget):
        self.widget_list.remove(widget)

    def get(self, name: str) -> BaseWidget | None:
        for widget in self.widget_list:
            if widget.name == name:
                return widget
        return None

    def update(self):
        self.menubar_status = MenuBarStatusTypes.UPDATING
        for widget in self.widget_list:
            widget.update()
        self.menubar_status = self._get_menubar_status()

    def _get_menubar_status(self) -> MenuBarStatusTypes:
        for widget in self.widget_list:
            if widget.status.widget_status == StatusTypes.ERROR:
                return MenuBarStatusTypes.ERROR
            if widget.status.widget_status == StatusTypes.WARNING:
                return MenuBarStatusTypes.WARNING
        return MenuBarStatusTypes.SUCCESS

    def __iter__(self):
        return iter(self.widget_list)

    def __len__(self):
        return len(self.widget_list)

    def __getitem__(self, item):
        return self.get(item)
