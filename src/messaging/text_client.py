from twilio.rest import Client
from config import TwilioConfig


class TextClient:
    def __init__(self, config: TwilioConfig):
        self.__config = config

    def send_message(self, body, to):
        client = Client(self.__config.get_account_sid(), self.__config.get_auth_token())
        client.messages.create(body=body, to=to, from_=self.__config.get_number())
