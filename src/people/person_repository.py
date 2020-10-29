import csv
from people.person import Person
from typing import List


class PersonRepository:
    def __init__(self, repo_name):
        self.__repo_name = repo_name

    def get_people(self) -> List[Person]:
        with open(self.__repo_name) as people_csv:
            person_reader = csv.reader(people_csv, delimiter=',', quotechar='"')
            return [Person(*row) for row in person_reader]
