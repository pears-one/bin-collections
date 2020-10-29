from collection.collection_scraper import CollectionScraperConfig
import yaml

class TwilioConfig:
    def __init__(self, account_sid: str, auth_token: str, number: str):
        self.__account_sid = account_sid
        self.__auth_token = auth_token
        self.__number = number

    def get_account_sid(self):
        return self.__account_sid

    def get_auth_token(self):
        return self.__auth_token

    def get_number(self):
        return self.__number

    @staticmethod
    def from_file():
        file_path = "config/raspberrypi.yaml"
        with open(file_path) as file:
            twilio_config = yaml.load(file, Loader=yaml.FullLoader)["app"]["twilio"]
        return TwilioConfig(
            twilio_config["account_sid"],
            twilio_config["auth_token"],
            twilio_config["number"]
        )
