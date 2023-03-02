import os

from src.base import BaseWidget, Status


class CheckDNS(BaseWidget):
    name = "Check DNS"
    settings = {'network': 'Wi-Fi'}
    settings_schema = {
        "network": str,
        "dns": str,
    }

    def _check(self) -> Status:
        cmd_response = os.popen("networksetup -getdnsservers {}".format(self.settings.get('network'))).read().strip()
        if self.settings.get('dns') in cmd_response:
            return Status.success()
        else:
            return Status.error('DNS is not set to {}'.format(self.settings.get('dns')))
