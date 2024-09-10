from classes.team import Team
from utils.connection import get_connection, close_connection

class Player:
    all_players = []
    def __init__(self, id, first_name, last_name, team_id, uniform_number) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.team_id = team_id
        self.uniform_number = uniform_number
        self.team = str(Team.find(team_id))
        Player.all_players.append(self)

    def save(self):
        if self.exists():
            self.update()
            return

        conn, cursor = get_connection()

        query = """
            INSERT INTO players(id, first_name, last_name, team_id, uniform_number)
            VALUES ('{0}',$${1}$$,$${2}$$,$${3}$$,'{4}')
        """.format(self.id, self.first_name, self.last_name, self.team_id, self.uniform_number)

        cursor.execute(query)
        conn.commit()
        close_connection(conn, cursor)

    def update(self):
        conn, cursor = get_connection()
        query = """
            UPDATE players
            SET first_name = $${0}$$, last_name = $${1}$$, team_id = $${2}$$, uniform_number = '{3}'
            WHERE id = '{4}'
        """.format(self.first_name, self.last_name, self.team_id, self.uniform_number, self.id)

        cursor.execute(query)
        conn.commit()
        close_connection(conn, cursor)

    def exists(self):
        conn, cursor = get_connection()
        query = "SELECT id FROM players where id = $${}$$".format(self.id)
        cursor.execute(query)
        result = cursor.fetchone()
        close_connection(conn, cursor)
        return result

    def __str__(self):
        return f'{self.id} {self.uniform_number} - {self.first_name} {self.last_name} - {self.team_id}'
    
        