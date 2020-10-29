from datetime import timedelta

from alerts.alert_manager import AlertManager
from people.person_repository import PersonRepository
from alerts.alert_messenger import AlertMessenger
from alerts.alert_filter import AlertFilter
from config import TwilioConfig
from messaging.text_client import TextClient


def main():
    person_repo = PersonRepository('data/alertees.txt')
    manager = AlertManager(person_repo)
    alerts = manager.get_alerts()
    one_day = timedelta(0)
    alerts = AlertFilter(one_day).filter(alerts)
    text_client = TextClient(TwilioConfig.from_file())
    messenger = AlertMessenger(alerts, text_client)
    messenger.send_messages()


if __name__ == "__main__":
    main()
