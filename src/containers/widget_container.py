from typing import Dict

from src.base import BaseWidget
from src.base.status import GlobalStatusTypes


class WidgetContainer:
    def __init__(self, _=None):
        self._widgets: Dict[str, BaseWidget] = dict()
        self._global_status = GlobalStatusTypes.UNKNOWN

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
        self._global_status = GlobalStatusTypes.UPDATING
        for widget in self._widgets.values():
            widget.update()
        self._global_status = self._get_global_status()

    def _get_global_status(self) -> GlobalStatusTypes:
        for widget in self._widgets.values():
            if widget.status.global_status == GlobalStatusTypes.ERROR:
                return GlobalStatusTypes.ERROR
            if widget.status.global_status == GlobalStatusTypes.WARNING:
                return GlobalStatusTypes.WARNING
        return GlobalStatusTypes.SUCCESS

    def __iter__(self):
        return iter(self._widgets.values())

    def __len__(self):
        return len(self._widgets)

    def __getitem__(self, item):
        return self.get(item)
