from src.status.global_status_types import GlobalStatusTypes
from src.status.widget_status_types import WidgetStatusTypes


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
