from people.person import Person
import sqlite3
from typing import List


class PersonRepository:
    def __init__(self, repo_name):
        self.__repo_name = repo_name

    def get_people(self) -> List[Person]:
        get_people_statement = """
        SELECT person.first_name as name, person.phone_number as number , property.uprn as uprn
        FROM person
        JOIN residency ON (person.phone_number = residency.phone_number)
        JOIN property ON (residency.uprn = property.uprn)
        """
        conn = sqlite3.connect('data/bin_collections.db')
        c = conn.cursor()
        return [Person(*row) for row in c.execute(get_people_statement)]
