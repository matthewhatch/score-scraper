from classes.abstract_team import AbstractTeam
from utils.connection import get_connection, close_connection

class Team(AbstractTeam):
    all_teams = []
    def __init__(self, id, display_name, city, mascot, abbr) -> None:
        self.id = id
        self.display_name = display_name
        self.city = city
        self.mascot = mascot
        self.abbr = abbr
        self.add_team()
        self.save()

    def add_team(self):
        ids = [t.id for t in Team.all_teams]
        if self.id not in ids:
            Team.all_teams.append(self)

    def find(id):
        for team in Team.all_teams:
            if team.id == id:
                return team
            
    def find_by_name(name):
        conn, cursor = get_connection()
        query = "SELECT id FROM teams where mascot = $${0}$$".format(name)
        cursor.execute(query)
        result = cursor.fetchone()

        close_connection(conn, cursor)
        return result[0]
    
    def save(self):
        if self.exists(): return
        
        conn, cursor = get_connection()
        league = self.id.split('.')[0].upper()
        query = """
            INSERT INTO teams(id, name, city, mascot, abbr,league)
            VALUES ('{0}','{1}', '{2}', '{3}', '{4}', '{5}')
        """.format(self.id, self.display_name, self.city, self.mascot, self.abbr, league)
        cursor.execute(query)
        conn.commit()
        close_connection(conn, cursor)
    
    def exists(self):
        conn, cursor = get_connection()
        query = """SELECT id FROM teams where id = '{0}'""".format(self.id)
        cursor.execute(query)
        result = cursor.fetchone()
        close_connection(conn, cursor)
        return result
    
    def __str__(self):
        return f'{self.city} {self.mascot}({self.abbr})'
    