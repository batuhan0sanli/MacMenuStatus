import os

import yaml


class Config:
    _instance = None
    path = os.path.expanduser('~/.config/macmenustatus/')
    file_name = 'config.yaml'
    config_path = os.path.join(path, file_name)
    example_config_path = os.path.join(os.path.dirname(__file__), 'example_config.yaml')

    def __init__(self):
        self._config = None
        self.__initialize()
        self.load()

    def __initialize(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        if not os.path.exists(self.config_path):
            with open(self.config_path, 'w') as file:
                with open(self.example_config_path) as example:
                    file.write(example.read())

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def get(self, item, default=None):
        return self._config.get(item) or default

    def load(self):
        with open(self.config_path) as file:
            self._config = yaml.load(file, Loader=yaml.FullLoader)
