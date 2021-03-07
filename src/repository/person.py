from model.person import Person
from query import get_people_statement, get_residents_statement
import sqlite3
from typing import List


class PersonRepository:
    def __init__(self, repo_name: str):
        self.__repo_name = repo_name

    def get_residents(self, uprn) -> List[Person]:
        conn = sqlite3.connect(self.__repo_name)
        c = conn.cursor()
        stmt = get_residents_statement.format(uprn=uprn)
        rows = c.execute(stmt)
        return [Person(*row) for row in rows]
