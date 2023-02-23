import os
import yaml


class Config:
    _instance = None

    def __init__(self):
        self._config = None
        self.path = os.path.join(os.path.dirname(__file__), 'example_config.yaml')
        self.load()

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def get(self, item):
        return self._config.get(item, None)

    def load(self):
        with open(self.path) as file:
            self._config = yaml.load(file, Loader=yaml.FullLoader)
