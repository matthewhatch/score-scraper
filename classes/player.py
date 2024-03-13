from classes.team import Team

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

    def __str__(self):
        return f'{self.uniform_number} - {self.first_name} {self.last_name} - {self.team}'
    
        