from model.property import Property
from query import get_property_statement
import sqlite3
from typing import List


class PropertyRepository:
    def __init__(self, conn_str):
        self.__conn_str = conn_str

    def get_properties(self) -> List[Property]:
        conn = sqlite3.connect(self.__conn_str)
        c = conn.cursor()
        return [Property(*row) for row in c.execute(get_property_statement)]
