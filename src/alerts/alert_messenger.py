from alerts.alert import Alert
from messaging.text_client import TextClient
from typing import List


class AlertMessenger:
    def __init__(self, alerts: List[Alert], text_client: TextClient):
        self.__alerts = alerts
        self.__text_client = text_client

    def send_messages(self):
        for alert in self.__alerts:
            self.__text_client.send_message(alert.get_message(), alert.get_person().get_number())
