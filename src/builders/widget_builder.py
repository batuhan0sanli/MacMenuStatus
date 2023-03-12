from src.base import BaseContainerBuilder
from src.containers import WidgetContainer
from src.widgets import widget_list

__all__ = ['WidgetBuilder']


class WidgetBuilder(BaseContainerBuilder):
    _container = WidgetContainer

    def build(self) -> 'WidgetContainer':
        for widget in self._sender.config.get('widgets'):
            widget_obj = widget_list.get(widget.get('widget_type'))
            if not widget_obj:
                print(f"Widget {widget.get('widget_type')} not found")
                continue
            widget_obj = widget_obj(settings=widget.get('config'))
            widget_obj.name = widget.get('name') or widget_obj.name
            self.container_instance.add(widget_obj)
        return self.container_instance
