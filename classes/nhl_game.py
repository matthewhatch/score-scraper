from classes.game import Game
from utils.feed import get_feed

class NHLGame(Game):
    def __init__(self, id, home_team, visiting_team, network, time, home_score=None, visiting_score=None, stage=None, stage_display=None, last_updated=None, updated=False) -> None:
        super().__init__(id, home_team, visiting_team, network, time, home_score, visiting_score, stage, stage_display, last_updated, updated)

    @classmethod
    def URL(self, date) -> str:
        return get_feed('NHL',date)