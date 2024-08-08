import json


class Config:

    def __init__(self, path='registration_config.json'):
        with open(path, 'r') as f:
            self.config = json.load(f)
        self.first_name = self.config["FIRST_NAME"]
        self.last_name = self.config["LAST_NAME"]
        self.email = self.config["EMAIL"]
        self.password = self.config["PASSWORD"]
