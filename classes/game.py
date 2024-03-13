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
        self.add_game()

    def add_game(self):
        Game.all_games.append(self)
        
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

        return f'{self.network} - {visitor} at {home}'