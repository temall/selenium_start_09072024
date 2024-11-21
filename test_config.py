import json


class Config:

    def __init__(self, path='config.json'):
        with open(path, 'r') as f:
            self.config = json.load(f)
        self.first_name = self.config["FIRST_NAME"]
        self.last_name = self.config["LAST_NAME"]
        self.email = self.config["EMAIL"]
        self.password = self.config["PASSWORD"]
        self.url = self.config["URL"]
        self.admin_login = self.config["ADMIN_LOGIN"]
        self.admin_password = self.config["ADMIN_PASSWORD"]
        self.logger_name = self.config["LOGGER_NAME"]
