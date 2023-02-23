from config import config
from src.base.widgets import Widgets
from widgets import widget_list

__all__ = ['widgets_obj']


widgets_obj = Widgets()

for widget in config.get('widgets'):
    widget_obj = widget_list.get(widget.get('widget_type'))
    if not widget_obj:
        continue
    widget_obj = widget_obj(settings=widget.get('config'))
    widget_obj.name = widget.get('name') or widget_obj.name
    widgets_obj.add(widget_obj)
