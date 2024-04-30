import json
import requests

from classes.abstract_game import AbstractGame
from classes.abstract_team import AbstractTeam
from classes.mlb_game import MLBGame
from classes.mlb_team import MLBTeam
from classes.nba_game import NBAGame
from classes.nba_team import NBATeam
from classes.ncaab_game import NCAABGame
from classes.ncaab_team import NCAABTeam
from classes.nfl_game import NFLGame
from classes.nfl_team import NFLTeam
from classes.nhl_game import NHLGame
from classes.nhl_team import NHLTeam
from classes.player import Player
from utils.feed import get_feed

def get_teams(team_class, teams) -> AbstractTeam:
    klass: AbstractTeam
    klass = globals()[team_class]

    for team in teams.values():
        team_id = team['team_id']
        display_name = team['display_name']
        city = team['first_name']
        mascot = team['last_name']
        abbr = team['abbr']
        klass(team_id, display_name, city, mascot, abbr)

def get_players(players):
    for player in players.values():
        id = player['player_id']
        first_name = player['first_name']
        last_name = player['last_name']
        team_id = player['team_id']
        uniform_number = player['uniform_number']

        Player(id, first_name, last_name, team_id, uniform_number)

    for player in Player.all_players:
        print(str(player))

def get_games(game_class, team_class, games) -> AbstractGame:
    klass: AbstractGame
    team_klass: AbstractTeam = globals()[team_class]

    for game in games.values():
        id = game['gameid']
        home_team = team_klass.find(game['home_team_id'])
        away_team = team_klass.find(game['away_team_id'])
        home_score =str(game['total_home_points'])
        away_score =str(game['total_away_points'])
        network = game['tv_coverage']
        time = game['start_time']
        status = game['status_description']
        status_display = game['status_display_name']
        last_updated = game['last_updated']

        # call appropriate Game Class based on League
        klass = globals()[game_class]
        klass(id, home_team, away_team, network, time, home_score, away_score, status, status_display, last_updated, False)
    
    return klass

def scrape(league, date='next_real') -> AbstractGame:
    # URL = get_feed(league.upper(), date)
    game_class = f'{league.upper()}Game'
    team_class = f'{league.upper()}Team'
    URL = globals()[game_class].URL(date)
    response = requests.get(URL)
    content = json.loads(response.content)

    try:
        get_teams(team_class, content['service']['scoreboard']['teams'])
    except Exception:
        print(f'There are no games for date: {date}')
        exit(0)
    
    return get_games(game_class, team_class, content['service']['scoreboard']['games'])

if __name__ == '__main__':
    scrape()
