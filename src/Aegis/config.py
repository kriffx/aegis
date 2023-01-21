from os import path, getenv
from dotenv import load_dotenv
from robot.libraries.BuiltIn import BuiltIn

class Config:
    def __init__(self):
        env = BuiltIn().get_variable_value("${env}", "local")
        load_dotenv(path.join("configs", "{}.env".format(env)))

    def env(self, key: str, default = None) -> (str | None):
        return getenv(key, default)
    
    def retry(self) -> (str | None):
        return self.env("retry", "12x")

    def retry_interval(self) -> (str | None):
        return self.env("retry_interval", "5s")