from rumps import App, Timer, separator
from config import config
from static.emoji import Emoji
from src.widget_builder import WidgetBuilder
from src.base.widgets import Widgets


class MacMenuStatus(App):
    def __init__(self, widgets: 'Widgets'):
        super(MacMenuStatus, self).__init__(name="MacMenuStatus", title=Emoji.hollow_red_circle)
        self.widgets = widgets
        self._add_menu_items()

    def _add_menu_items(self):
        for widget in self.widgets:
            self.menu.add(widget.menu_item)
        self.menu.add(separator)
        # self.menu.add("Quit", callback=self.quit)

    def _update_title(self, _):
        self.widgets.update()
        self.title = self.widgets.menubar_status.value
        self.menu.clear()
        self._add_menu_items()

    def run(self):
        Timer(self._update_title, 10).start()
        super(MacMenuStatus, self).run()


if __name__ == "__main__":
    widgets = WidgetBuilder(config).build()
    app = MacMenuStatus(widgets)
    app.run()
