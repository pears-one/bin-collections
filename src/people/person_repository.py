from people.person import Person
from query import get_people_statement
import sqlite3
from typing import List


class PersonRepository:
    def __init__(self, repo_name):
        self.__repo_name = repo_name

    def get_people(self) -> List[Person]:
        conn = sqlite3.connect('data/bin_collections.db')
        c = conn.cursor()
        return [Person(*row) for row in c.execute(get_people_statement)]
