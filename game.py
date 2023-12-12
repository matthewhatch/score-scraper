from utils.game import get_stage

class Game:
    all_games = []
    def __init__(self, home_team, visiting_team, network, time, home_score=None, visiting_score=None) -> None:
        self.home_team = home_team
        self.visiting_team = visiting_team
        self.home_score = home_score
        self.visiting_score = visiting_score
        self.network = network
        self.time = time
        self.stage, self.color = get_stage(time)
        Game.all_games.append(self)

    def reset_games():
         Game.all_games = []

    def __str__(self):
        visitor = self.visiting_team
        home = self.home_team

        if self.stage == 'FINAL' or self.stage == 'IN_PROGRESS':
            visitor = f'{self.visiting_score} {self.visiting_team}'
            home = f'{self.home_score} {self.home_team}'

        return f'{self.time} {self.network} - {visitor} @ {home}'