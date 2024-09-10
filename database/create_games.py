# Create Games
# id, network, time, stage, date, home_team, visiting_team, home_score, visiting_score, location, id
from utils.connection import get_connection

def create_games_table() -> None:
    query = """
    CREATE TABLE games (
        id VARCHAR,
        home_team_id VARCHAR,
        visiting_team_id VARCHAR,
        home_score VARCHAR,
        visiting_score VARCHAR,
        network VARCHAR,
        time VARCHAR,
        stage VARCHAR,
        date VARCHAR,
        last_updated VARCHAR
    )
    """

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
    cursor.close()

create_games_table()