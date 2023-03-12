from enum import Enum

from static import AppIcons, Emoji


class WidgetStatusTypes(Enum):
    """Status of the widgets."""
    SUCCESS = Emoji.green_circle
    ERROR = Emoji.red_circle
    WARNING = Emoji.yellow_circle
    UNKNOWN = Emoji.black_circle
    UPDATING = Emoji.white_circle
    WIDGET_ERROR = Emoji.red_circle

    def to_global(self) -> 'MenuBarStatusTypes':
        if self == WidgetStatusTypes.SUCCESS:
            return MenuBarStatusTypes.SUCCESS
        if self == WidgetStatusTypes.ERROR:
            return MenuBarStatusTypes.ERROR
        if self == WidgetStatusTypes.WARNING:
            return MenuBarStatusTypes.WARNING
        if self == WidgetStatusTypes.UNKNOWN:
            return MenuBarStatusTypes.UNKNOWN
        if self == WidgetStatusTypes.UPDATING:
            return MenuBarStatusTypes.UPDATING
        if self == WidgetStatusTypes.WIDGET_ERROR:
            return MenuBarStatusTypes.ERROR


class MenuBarStatusTypes(Enum):
    """Status of the menu bar."""
    SUCCESS = AppIcons.green_logo
    ERROR = AppIcons.red_logo
    WARNING = AppIcons.yellow_logo
    UNKNOWN = AppIcons.black_logo
    UPDATING = AppIcons.pending_logo_black


class Status:
    def __init__(
            self,
            widget_status: 'WidgetStatusTypes' = WidgetStatusTypes.UNKNOWN,
            menubar_status: 'MenuBarStatusTypes' = MenuBarStatusTypes.UNKNOWN,
            message: str = None,
    ):
        self.widget_status = widget_status
        self.menubar_status = menubar_status or widget_status.to_global()
        self.message = message

    def __str__(self):
        return self.widget_status.value

    @staticmethod
    def success(message: str = None) -> 'Status':
        return Status(WidgetStatusTypes.SUCCESS, MenuBarStatusTypes.SUCCESS, message)

    @staticmethod
    def error(message: str = None) -> 'Status':
        return Status(WidgetStatusTypes.ERROR, MenuBarStatusTypes.ERROR, message)

    @staticmethod
    def warning(message: str = None) -> 'Status':
        return Status(WidgetStatusTypes.WARNING, MenuBarStatusTypes.WARNING, message)

    @staticmethod
    def unknown(message: str = None) -> 'Status':
        return Status(WidgetStatusTypes.UNKNOWN, MenuBarStatusTypes.UNKNOWN, message)

    @staticmethod
    def updating(message: str = None) -> 'Status':
        return Status(WidgetStatusTypes.UPDATING, MenuBarStatusTypes.UPDATING, message)

    @staticmethod
    def widget_error(message: str = None) -> 'Status':
        return Status(WidgetStatusTypes.WIDGET_ERROR, MenuBarStatusTypes.WARNING, 'Widget Error: {}'.format(message))
