from classes.team import Team

class NHLTeam(Team):
    def __init__(self, id, display_name, city, mascot, abbr) -> None:
        super().__init__(id, display_name, city, mascot, abbr)
