# Create Players
# first_name, last_name, sport
from utils.connection import get_connection

def create_players_table() -> None:
    query = """
    CREATE TABLE players (
        id VARCHAR,
        first_name VARCHAR,
        last_name VARCHAR,
        team_id VARCHAR,
        uniform_number VARCHAR
    )
    """

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
    cursor.close()

create_players_table()