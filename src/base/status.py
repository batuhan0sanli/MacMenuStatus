from enum import Enum

from static.emoji import Emoji
from static.mac_menu_status_icons import MacMenuStatusIcons


class StatusTypes(Enum):
    """Status of a services."""
    SUCCESS = Emoji.green_circle
    ERROR = Emoji.red_circle
    WARNING = Emoji.yellow_circle
    UNKNOWN = Emoji.black_circle
    UPDATING = Emoji.white_circle
    WIDGET_ERROR = Emoji.red_circle


class MenuBarStatusTypes(Enum):
    SUCCESS = MacMenuStatusIcons.green_logo
    ERROR = MacMenuStatusIcons.red_logo
    WARNING = MacMenuStatusIcons.yellow_logo
    UNKNOWN = MacMenuStatusIcons.black_logo
    UPDATING = MacMenuStatusIcons.pending_logo_black
    WIDGET_ERROR = MacMenuStatusIcons.red_logo


class Status:
    def __init__(
            self,
            widget_status: 'StatusTypes' = StatusTypes.UNKNOWN,
            menubar_status: 'StatusTypes' = StatusTypes.UNKNOWN,
            message: str = None,
    ):
        self.widget_status = widget_status
        self.menubar_status = menubar_status or widget_status
        self.message = message

    def __str__(self):
        return self.widget_status.value

    @staticmethod
    def success(message: str = None) -> 'Status':
        return Status(StatusTypes.SUCCESS, StatusTypes.SUCCESS, message)

    @staticmethod
    def error(message: str = None) -> 'Status':
        return Status(StatusTypes.ERROR, StatusTypes.ERROR, message)

    @staticmethod
    def warning(message: str = None) -> 'Status':
        return Status(StatusTypes.WARNING, StatusTypes.WARNING, message)

    @staticmethod
    def unknown(message: str = None) -> 'Status':
        return Status(StatusTypes.UNKNOWN, StatusTypes.UNKNOWN, message)

    @staticmethod
    def updating(message: str = None) -> 'Status':
        return Status(StatusTypes.UPDATING, StatusTypes.UPDATING, message)

    @staticmethod
    def widget_error(message: str = None) -> 'Status':
        return Status(StatusTypes.WIDGET_ERROR, StatusTypes.WIDGET_ERROR, 'Widget Error: {}'.format(message))
