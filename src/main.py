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
    notice_in_days = timedelta(5)
    alerts = AlertFilter(notice_in_days).filter(alerts)
    text_client = TextClient(TwilioConfig.from_env())
    messenger = AlertMessenger(alerts, text_client)
    messenger.send_messages()


if __name__ == "__main__":
    main()
