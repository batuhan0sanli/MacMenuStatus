from src.base import Widgets
from src.config import Config
from src.widgets import widget_list

__all__ = ['WidgetBuilder']


class WidgetBuilder:
    _built_widgets: 'Widgets' = Widgets()

    def __init__(self, config: 'Config'):
        self._config = config

    @property
    def built_widgets(self):
        return self._built_widgets

    def build(self):
        for widget in self._config.get('widgets'):
            widget_obj = widget_list.get(widget.get('widget_type'))
            if not widget_obj:
                print(f"Widget {widget.get('widget_type')} not found")
                continue
            widget_obj = widget_obj(settings=widget.get('config'))
            widget_obj.name = widget.get('name') or widget_obj.name
            self._built_widgets.add(widget_obj)
        return self._built_widgets
