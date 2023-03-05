from dataclasses import dataclass


@dataclass(frozen=True, init=False)
class MacMenuStatusIcons:
    pending_logo_white: str = 'static/mac_menu_status_icons/pending_logo_white.png'
    pending_logo_black: str = 'static/mac_menu_status_icons/pending_logo_black.png'
    white_logo: str = 'static/mac_menu_status_icons/white_logo.png'
    black_logo: str = 'static/mac_menu_status_icons/black_logo.png'
    red_logo: str = 'static/mac_menu_status_icons/red_logo.png'
    green_logo: str = 'static/mac_menu_status_icons/green_logo.png'
    yellow_logo: str = 'static/mac_menu_status_icons/yellow_logo.png'
