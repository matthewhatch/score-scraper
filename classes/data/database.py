import psycopg2
from classes.data.abstract_data_handler import AbstractDataHandler

class Database(AbstractDataHandler):
    def save(self, table, **kwargs):
        pass

    def find(self, id):
        pass