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


if __name__ == "__main__":
    settings = {
        "network": "Wi-Fi",
        "dns": "192.168.1.100",
    }

    obj = CheckDNS(settings=settings)
    obj.update()
    print(obj.status.message)
