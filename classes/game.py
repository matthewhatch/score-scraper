from classes.abstract_game import AbstractGame
from datetime import datetime
from typing import List
from utils.connection import get_connection, close_connection

class Game(AbstractGame):
    all_games: List['Game'] = []
    def __init__(self, id, home_team_id, visiting_team_id, home_team, visiting_team, network, time, home_score=None, visiting_score=None, stage=None, stage_display=None, last_updated=None, updated=False) -> None:
        self.id = id
        self.home_team_id = home_team_id
        self.visiting_team_id = visiting_team_id
        self.last_updated = last_updated
        self.updated = updated
        self.home_team = home_team
        self.visiting_team = visiting_team
        self.home_score = home_score
        self.visiting_score = visiting_score
        self.network = network
        self.time = time
        self.stage = stage
        self.stage_display = stage_display
        self.date = datetime.strptime(time,'%a, %d %b %Y %H:%M:%S +0000').strftime('%a %b %d %Y')

        self.add_game()
        self.save()

    @classmethod
    def URL(self, date) -> str:
        raise NotImplementedError('URL must be implemented')
 
    def add_game(self) -> None:
        ids = [g.id for g in Game.all_games]
        if self.id not in ids or len(Game.all_games) == 0:
            Game.all_games.append(self)
            return

        for i, g in enumerate(Game.all_games):
            if g.id == self.id and g.last_updated != self.last_updated:
                self.updated = True
                Game.replace_game(i, self)
            else:
                self.updated = False
        
    def replace_game(index, value) -> None:
        Game.all_games[index] = value

    def reset_games() -> None:
         Game.all_games = []

    def save(self) -> None:
        if self.exists():
            self.update()
            return

        conn, cursor = get_connection()

        query = """
            INSERT INTO games(id, home_team_id, visiting_team_id, home_score, visiting_score, network, stage, time, date, last_updated)
            VALUES ('{0}','{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}','{9}')
        """.format(self.id, self.home_team_id, self.visiting_team_id, self.home_score, self.visiting_score, self.network, self.stage, self.time, self.date, self.last_updated)
        cursor.execute(query)
        conn.commit()
        
        close_connection(conn, cursor)

    def update(self) -> None:
        conn, cursor = get_connection()

        query = """
            UPDATE games
            SET home_score = '{0}', visiting_score = '{1}', stage = '{2}', last_updated = '{3}'
            where id = '{4}'
        """.format(self.home_score, self.visiting_score, self.stage, self.last_updated,self.id)
        cursor.execute(query)
        conn.commit()
        close_connection(conn, cursor)

    def exists(self) -> bool:
        conn, cursor = get_connection()
        query = """SELECT id FROM games where id = '{0}'""".format(self.id)
        cursor.execute(query)
        result = cursor.fetchone()
        close_connection(conn, cursor)
        
        return result

    def __str__(self) -> str:
        visitor = self.visiting_team
        home = self.home_team

        if self.stage.upper() == 'FINAL' or self.stage.upper() == 'LIVE':
            visitor = f'{self.visiting_score} {self.visiting_team}'
            home = f'{self.home_score} {self.home_team}'

        return f'{self.stage_display} {self.network} - {visitor} at {home}'
