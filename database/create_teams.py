# Create the Teams Database
# id, name, city, mascot, abbr
from utils.connection import get_connection

def create_teams_table() -> None:
    query = """
    CREATE TABLE teams (
        id VARCHAR,
        name VARCHAR,
        city VARCHAR,
        mascot VARCHAR,
        abbr VARCHAR,
        league VARCHAR
    )
    """
    
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
    cursor.close()

create_teams_table()
