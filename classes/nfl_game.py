from classes.game import Game
import datetime

class NflGame(Game):
    def __init__(self, id, home_team, visiting_team, network, time, home_score=None, visiting_score=None, stage=None, stage_display=None, last_updated=None, updated=False) -> None:
        self.id = id
        self.last_updated = last_updated
        self.updated = updated

        super().__init__(home_team, visiting_team, network, time, home_score, visiting_score)
        self.stage = stage
        self.stage_display = stage_display
        self.date = datetime.datetime.strptime(time,'%a, %d %b %Y %H:%M:%S +0000').strftime('%a %b %d')

    def add_game(self):
        ids = [g.id for g in NflGame.all_games]
        if self.id not in ids or len(NflGame.all_games) == 0:
            NflGame.all_games.append(self)
            return

        for i, g in enumerate(NflGame.all_games):
            if g.id == self.id and g.last_updated != self.last_updated:
                self.updated = True
                NflGame.replace_game(i, self)
            else:
                self.updated = False
    
    def __str__(self):
        str_value = f'{self.stage_display} {super().__str__()}'
        return str_value