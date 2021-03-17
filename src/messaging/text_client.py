from twilio.rest import Client
from config import TwilioConfig
import logging


class TextClient:
    def __init__(self, config: TwilioConfig):
        self.config = config

    def send_message(self, body, to):
        try:
            client = Client(self.config.get_account_sid(), self.config.get_auth_token())
            client.messages.create(body=body, to=to, from_=self.config.get_number())
            logging.info(f"message sent to {to}")
        except Exception as e:
            logging.error(f"failed to send message to {to}: {str(e)}")


class FakeClient(TextClient):
    def __init__(self, config: TwilioConfig):
        super().__init__(config)

    def send_message(self, body, to):
        print(
            f"""
            from: {self.config.get_number()}
            to: {to}
            
            body: {body}
            """
        )
