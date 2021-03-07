from twilio.rest import Client
from config import TwilioConfig


class TextClient:
    def __init__(self, config: TwilioConfig):
        self.config = config

    def send_message(self, body, to):
        client = Client(self.config.get_account_sid(), self.config.get_auth_token())
        client.messages.create(body=body, to=to, from_=self.config.get_number())


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
