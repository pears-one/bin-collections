from datetime import timedelta
import sys
import os

from alerts.alert_manager import AlertManager
from repository.person import PersonRepository
from repository.property import PropertyRepository
from alerts.alert_filter import AlertFilter
from config import TwilioConfig
from messaging.text_client import TextClient, FakeClient


def main(dev: bool):
    if not dev:
        sys.stdout = open("stout.txt", 'w')
        sys.stderr = open("sterr.txt", 'w')
    person_repo = PersonRepository(os.environ['DB_ADDRESS'])
    property_repo = PropertyRepository(os.environ['DB_ADDRESS'])
    client_type = FakeClient if dev else TextClient
    text_client = client_type(TwilioConfig.from_env())
    manager = AlertManager(property_repo, person_repo, text_client)
    alerts = manager.get_alerts()
    notice_in_days = timedelta(int(os.environ['DELAY_IN_DAYS']))
    alerts = AlertFilter(notice_in_days).filter(alerts)
    manager.send_messages(alerts)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args[0] == "dev")
