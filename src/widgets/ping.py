import os

from src.base import BaseWidget, Status


class Ping(BaseWidget):
    name = "Ping"
    settings = {'hostname': 'google.com'}
    settings_schema = {
        "hostname": str,
    }

    def _check(self) -> Status:
        cmd_response = os.system("ping -c 1 {}".format(self.settings.get('hostname')))
        if cmd_response == 0:
            return Status.success()
        else:
            return Status.error('No response from {}'.format(self.settings.get('hostname')))
