from typing import Dict

from src.base.base_widget import BaseWidget
from src.base.status import StatusTypes, MenuBarStatusTypes


class WidgetContainer:
    def __init__(self):
        self._widgets: Dict[str, BaseWidget] = dict()
        self._global_status = MenuBarStatusTypes.UNKNOWN

    @property
    def global_status(self):
        return self._global_status

    def add(self, widget: BaseWidget, name: str = None):
        if not name:
            name = widget.name
        self._widgets[name] = widget

    def remove(self, name: str):
        return self._widgets.pop(name)

    def get(self, name: str) -> BaseWidget | None:
        return self._widgets.get(name)

    def update(self):
        self._global_status = MenuBarStatusTypes.UPDATING
        for widget in self._widgets.values():
            widget.update()
        self._global_status = self._get_global_status()

    def _get_global_status(self) -> MenuBarStatusTypes:
        for widget in self._widgets.values():
            if widget.status.widget_status == StatusTypes.ERROR:
                return MenuBarStatusTypes.ERROR
            if widget.status.widget_status == StatusTypes.WARNING:
                return MenuBarStatusTypes.WARNING
        return MenuBarStatusTypes.SUCCESS

    def __iter__(self):
        return iter(self._widgets.values())

    def __len__(self):
        return len(self._widgets)

    def __getitem__(self, item):
        return self.get(item)
