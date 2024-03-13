class Team:
    all_teams = []
    def __init__(self, id, display_name, city, mascot, abbr) -> None:
        self.id = id
        self.display_name = display_name
        self.city = city
        self.mascot = mascot
        self.abbr = abbr
        # Team.all_teams.append(self)
        self.add_team()

    def add_team(self):
        ids = [t.id for t in Team.all_teams]
        if self.id not in ids:
            Team.all_teams.append(self)

    def find(id):
        for team in Team.all_teams:
            if team.id == id:
                return team
    
    def __str__(self):
        return f'{self.city} {self.mascot}({self.abbr})'
    