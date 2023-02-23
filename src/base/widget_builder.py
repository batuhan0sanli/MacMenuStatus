from abc import ABC, abstractmethod
from src.base.status import Status
from rumps import MenuItem


class WidgetBuilder(ABC):
    name: str
    settings: dict = {}
    settings_schema: dict = {}
    status: Status = Status.unknown()

    def __init__(
            self,
            name: str = None,
            settings: dict = None,
    ):
        self.name = name or self.name
        self.settings = self.settings | (settings or {})
        self.ready = self._check_settings()

    def _check_settings(self) -> bool:
        for key, value in self.settings_schema.items():
            if key not in self.settings:
                self.status = Status.widget_error('Missing setting "{}" for {} widget'.format(key, self.name))
                return False
            if not isinstance(self.settings[key], value):
                self.status = Status.widget_error('Setting "{}" for {} widget must be of type {}'.format(key, self.name, value.__name__))
                return False
        return True

    @abstractmethod
    def _check(self) -> Status:
        pass

    def update(self, _=None) -> 'WidgetBuilder':
        print('Updating {}'.format(self.name))
        if not self.ready:
            return self

        self.status = Status.updating()
        try:
            self.status = self._check()
        except Exception as e:
            self.status = Status.widget_error(str(e))
        return self

    def callback(self, _=None):
        """
        This method is called when the widget is clicked. If you want to do something when the widget is clicked,
        override this method.
        """
        return self.update()

    @property
    def menu_item(self) -> MenuItem:
        return MenuItem(title="{}: {}".format(self.status.widget_status.value, self.name), callback=self.callback)

    # @abstractmethod
    # def alert(self):  # add send_alert for widgets
    #     pass
