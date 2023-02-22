from typing import List
from .widget_builder import WidgetBuilder
from .status import StatusTypes


class Widgets:
    widget_list: List['WidgetBuilder'] = []
    menubar_status: StatusTypes = StatusTypes.UNKNOWN
    _instances = None

    def __new__(cls, *args, **kwargs):
        if not cls._instances:
            cls._instances = super(Widgets, cls).__new__(cls)
        return cls._instances

    def add(self, widget: WidgetBuilder):
        self.widget_list.append(widget)

    def remove(self, widget: WidgetBuilder):
        self.widget_list.remove(widget)

    def get(self, name: str) -> WidgetBuilder | None:
        for widget in self.widget_list:
            if widget.name == name:
                return widget
        return None

    def update(self):
        self.menubar_status = StatusTypes.UPDATING
        for widget in self.widget_list:
            widget.update()
        self.menubar_status = self._get_menubar_status()

    def _get_menubar_status(self) -> StatusTypes:
        for widget in self.widget_list:
            if widget.status.widget_status == StatusTypes.ERROR:
                return StatusTypes.ERROR
            if widget.status.widget_status == StatusTypes.WARNING:
                return StatusTypes.WARNING
        return StatusTypes.SUCCESS

    def __iter__(self):
        return iter(self.widget_list)

    def __len__(self):
        return len(self.widget_list)

    def __getitem__(self, item):
        return self.get(item)
