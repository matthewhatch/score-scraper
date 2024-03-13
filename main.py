import argparse
import operator
import os
import requests
import sys

from bs4 import BeautifulSoup
from classes.game import Game
from termcolor import colored
from time import sleep
from utils.banner import print_banner
from utils.feed import get_feed

def stage(time):
    FINAL_TEXT = ['FINAL', 'FINAL/OT', 'FINAL/SO']
    GAME_STAGE = ['1st', '2nd', '3rd', '4th']
    
    if time.split()[0].upper() in FINAL_TEXT:
        return 'FINAL', 'light_green'

    if time.split()[1] in GAME_STAGE:
        return 'IN_PORGRESS', 'cyan'
    
    return 'NOT_STARTED','light_grey'

def main(args):
    feed = get_feed(args.feed)
    URL = f'https://sports.yahoo.com/{feed}'
    SELECTOR = 'li[data-carousel-item="true"]'
    Game.reset_games()

    response = requests.get(URL)
    os.system('clear')
    print_banner(args)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    schedule = soup.select(SELECTOR)

    for item in schedule:
        if item:
            try:
                datas = item.find_all('div')
                time = datas[7].text
                network = datas[9].text
                visitor = datas[18].span.text
                home = datas[27].span.text
                game = Game(home, visitor, network, time)

                if game.stage == 'FINAL' or game.stage == 'IN_PROGRESS':
                    scores = datas[10].find_all('div')
                    game.home_score = scores[12].text
                    game.visiting_score = scores[3].text
                    
            except IndexError:
                pass

    return Game.all_games

if __name__ == '__main__':
    while True:
        try:
            os.system('clear')
            parser = argparse.ArgumentParser()
            parser.add_argument('--feed', '-f', type=str, default='NFL', choices=['nba', 'nfl', 'college basketball', 'ncaam', 'nhl', 'ncaaw', 'tennis'])
            parser.add_argument('--loop', '-l', action='count', default=0)
            parser.add_argument('--wait', '-w', type=int, default=15, required=False)
            args = parser.parse_args()
            
            print_banner(args)
            print('Getting scores...')
            
            games = main(args)
            sorted_games = sorted(games, key=operator.attrgetter('stage'))
            for game in sorted_games:
                print_attrs = []
                if game.stage == 'FINAL': print_attrs.append('dark')

                print(colored(str(game), game.color, attrs=print_attrs))
            if args.loop:
                sleep(args.wait)
            else:
                sys.exit(0)

        except KeyboardInterrupt:
            print('\r\nexiting...')
            sys.exit(0)