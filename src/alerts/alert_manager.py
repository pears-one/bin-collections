from people.person_repository import PersonRepository
from alerts.alert_compiler import AlertCompiler


class AlertManager:
    def __init__(self, person_repository: PersonRepository):
        self.__person_repository = person_repository

    def get_alerts(self):
        people = self.__person_repository.get_people()
        return [AlertCompiler(person).get_next_alert() for person in people]
