import json
import requests

from classes.game import Game
from classes.player import Player
from classes.team import Team
from termcolor import colored
from utils.feed import get_feed

def get_teams(teams):
    for team in teams.values():
        team_id = team['team_id']
        display_name = team['display_name']
        city = team['first_name']
        mascot = team['last_name']
        abbr = team['abbr']
        Team(team_id, display_name, city, mascot, abbr)

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

def get_games(games):
    for game in games.values():
        id = game['gameid']
        home_team = Team.find(game['home_team_id'])
        away_team = Team.find(game['away_team_id'])
        home_score =str(game['total_home_points'])
        away_score =str(game['total_away_points'])
        network = game['tv_coverage']
        time = game['start_time']
        status = game['status_description']
        status_display = game['status_display_name']
        last_updated = game['last_updated']

        Game(id, home_team, away_team, network, time, home_score, away_score, status, status_display, last_updated, False)

    for game in Game.all_games:
        attrs = []
        color = 'light_grey'

        if game.stage.upper() == 'FINAL':
            color = 'green'

        if game.stage.upper() == 'LIVE':
            color = 'light_yellow'
        if game.updated:
            attrs.append('reverse')

        print(colored(str(game), color, attrs=attrs))

def scrape(league):
    URL = get_feed(league.upper())
    response = requests.get(URL)
    content = json.loads(response.content)

    get_teams(content['service']['scoreboard']['teams'])
    get_games(content['service']['scoreboard']['games'])

if __name__ == '__main__':
    scrape()
