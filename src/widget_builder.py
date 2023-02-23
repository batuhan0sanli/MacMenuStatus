from config import Config
from src.base.widgets import Widgets
from widgets import widget_list

__all__ = ['WidgetBuilder']


class WidgetBuilder:
    _builded_widgets: 'Widgets' = Widgets()

    def __init__(self, config: 'Config'):
        self._config = config
        self._build()

    @property
    def builded_widgets(self):
        return self._builded_widgets

    def _build(self):
        for widget in self._config.get('widgets'):
            widget_obj = widget_list.get(widget.get('widget_type'))
            if not widget_obj:
                print(f"Widget {widget.get('widget_type')} not found")
                continue
            widget_obj = widget_obj(settings=widget.get('config'))
            widget_obj.name = widget.get('name') or widget_obj.name
            self._builded_widgets.add(widget_obj)
