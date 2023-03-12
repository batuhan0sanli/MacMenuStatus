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

    def to_global(self) -> 'GlobalStatusTypes':
        if self == WidgetStatusTypes.SUCCESS:
            return GlobalStatusTypes.SUCCESS
        if self == WidgetStatusTypes.ERROR:
            return GlobalStatusTypes.ERROR
        if self == WidgetStatusTypes.WARNING:
            return GlobalStatusTypes.WARNING
        if self == WidgetStatusTypes.UNKNOWN:
            return GlobalStatusTypes.UNKNOWN
        if self == WidgetStatusTypes.UPDATING:
            return GlobalStatusTypes.UPDATING
        if self == WidgetStatusTypes.WIDGET_ERROR:
            return GlobalStatusTypes.ERROR


class GlobalStatusTypes(Enum):
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
            global_status: 'GlobalStatusTypes' = GlobalStatusTypes.UNKNOWN,
            message: str = None,
    ):
        self.widget_status = widget_status
        self.global_status = global_status or widget_status.to_global()
        self.message = message

    def __str__(self):
        return self.widget_status.value

    @staticmethod
    def success(message: str = None) -> 'Status':
        return Status(WidgetStatusTypes.SUCCESS, GlobalStatusTypes.SUCCESS, message)

    @staticmethod
    def error(message: str = None) -> 'Status':
        return Status(WidgetStatusTypes.ERROR, GlobalStatusTypes.ERROR, message)

    @staticmethod
    def warning(message: str = None) -> 'Status':
        return Status(WidgetStatusTypes.WARNING, GlobalStatusTypes.WARNING, message)

    @staticmethod
    def unknown(message: str = None) -> 'Status':
        return Status(WidgetStatusTypes.UNKNOWN, GlobalStatusTypes.UNKNOWN, message)

    @staticmethod
    def updating(message: str = None) -> 'Status':
        return Status(WidgetStatusTypes.UPDATING, GlobalStatusTypes.UPDATING, message)

    @staticmethod
    def widget_error(message: str = 'Not defined error message!') -> 'Status':
        return Status(WidgetStatusTypes.WIDGET_ERROR, GlobalStatusTypes.WARNING, 'Widget Error: {}'.format(message))
