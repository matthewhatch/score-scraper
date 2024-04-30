import datetime
from classes.abstract_game import AbstractGame
from utils.game import get_stage

class Game(AbstractGame):
    all_games = []
    def __init__(self, id, home_team, visiting_team, network, time, home_score=None, visiting_score=None, stage=None, stage_display=None, last_updated=None, updated=False) -> None:
        self.id = id
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
        self.date = datetime.datetime.strptime(time,'%a, %d %b %Y %H:%M:%S +0000').strftime('%a %b %d')

        self.add_game()

    @classmethod
    def URL(self, date) -> str:
        raise NotImplementedError('URL must be implemented')
 
    def add_game(self):
        # BaseGame.all_games.append(self)
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
        
    def replace_game(index, value):
        # value.updated = True
        Game.all_games[index] = value

    def reset_games():
         Game.all_games = []

    def __str__(self):
        visitor = self.visiting_team
        home = self.home_team

        if self.stage.upper() == 'FINAL' or self.stage.upper() == 'LIVE':
            visitor = f'{self.visiting_score} {self.visiting_team}'
            home = f'{self.home_score} {self.home_team}'

        return f'{self.stage_display} {self.network} - {visitor} at {home}'