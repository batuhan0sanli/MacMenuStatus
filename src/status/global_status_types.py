from enum import Enum

from static import AppIcons


class GlobalStatusTypes(Enum):
    """Status of the menu bar."""
    SUCCESS = AppIcons.green_logo
    ERROR = AppIcons.red_logo
    WARNING = AppIcons.yellow_logo
    UNKNOWN = AppIcons.black_logo
    UPDATING = AppIcons.pending_logo_black
