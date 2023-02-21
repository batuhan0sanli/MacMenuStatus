from dataclasses import dataclass


@dataclass(frozen=True, init=False)
class Emoji:
    # https://emojipedia.org/search/?q=Circle
    black_circle: str = "⚫️"
    white_circle: str = "⚪️"
    red_circle: str = "🔴"
    blue_circle: str = "🔵"
    green_circle: str = "🟢"
    yellow_circle: str = "🟡"
    orange_circle: str = "🟠"
    purple_circle: str = "🟣"
    brown_circle: str = "🟤"
    hollow_red_circle: str = "⭕"
