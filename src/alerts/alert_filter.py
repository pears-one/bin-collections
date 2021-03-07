from datetime import timedelta, datetime
from model.alert import Alert
from typing import List


class AlertFilter:
    def __init__(self, notice: timedelta):
        self.__notice = notice

    def filter(self, alerts: List[Alert]) -> List[Alert]:
        filtered_alerts = []
        for alert in alerts:
            alert_day = datetime.today().date() + self.__notice
            if alert.get_date() == alert_day:
                filtered_alerts.append(alert)
        return filtered_alerts
