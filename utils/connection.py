from os import getenv
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    connection = psycopg2.connect(
            host = getenv('DB_HOST'),
            database = getenv('DATABASE'),
            user=getenv('DB_USER'),
            password=getenv('DB_PASSWORD'))
    cursor = connection.cursor()

    return (connection, cursor)

def close_connection(connection, cursor):
    connection.close()
    cursor.close()