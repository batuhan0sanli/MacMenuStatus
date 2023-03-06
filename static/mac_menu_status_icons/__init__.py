from dataclasses import dataclass
from rumps import Timer


@dataclass(frozen=True, init=False)
class MacMenuStatusIcons:
    pending_logo_white: str = 'static/mac_menu_status_icons/pending_logo_white.png'
    pending_logo_black: str = 'static/mac_menu_status_icons/pending_logo_black.png'
    white_logo: str = 'static/mac_menu_status_icons/white_logo.png'
    black_logo: str = 'static/mac_menu_status_icons/black_logo.png'
    red_logo: str = 'static/mac_menu_status_icons/red_logo.png'
    green_logo: str = 'static/mac_menu_status_icons/green_logo.png'
    yellow_logo: str = 'static/mac_menu_status_icons/yellow_logo.png'

    @classmethod
    def _error_flip_flop_callback(cls, sender):
        if sender.icon == cls.red_logo:
            sender.icon = cls.black_logo
        else:
            sender.icon = cls.red_logo

    @classmethod
    def error_flip_flop(cls, sender) -> Timer:
        return Timer(lambda _: cls._error_flip_flop_callback(sender), 0.5)
