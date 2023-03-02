from .check_dns import CheckDNS
from .ping import Ping

widget_list = {
    'check_dns': CheckDNS,
    'ping': Ping,
}

__all__ = ['widget_list']
