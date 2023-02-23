from src.base.widgets import Widgets
from widgets import widget_list
from config import config
from widgets.check_dns import CheckDNS

print(config)


widgets_obj = Widgets()

for widget in config.get('widgets'):
    widget_obj = widget_list.get(widget.get('widget_type'))
    if not widget_obj:
        continue
    widget_obj = widget_obj(settings=widget.get('config'))
    widget_obj.name = widget.get('name') or widget_obj.name
    widgets_obj.add(widget_obj)
