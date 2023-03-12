from enum import Enum

from src.status.global_status_types import GlobalStatusTypes
from static import Emoji


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
