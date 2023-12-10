import argparse
import os
import requests

from bs4 import BeautifulSoup
from termcolor import colored

def stage(time):
    FINAL_TEXT = ['FINAL', 'FINAL/OT', 'FINAL/SO']
    GAME_STAGE = ['1st', '2nd', '3rd', '4th']
    
    if time.split()[0].upper() in FINAL_TEXT:
        return 'FINAL', 'light_green'

    if time.split()[1] in GAME_STAGE:
        return 'IN_PORGRESS', 'cyan'
    
    return 'NOT_STARTED','light_grey'

def main(feed):
    URL = f'https://sports.yahoo.com/{feed}'
    SELECTOR = 'li[data-carousel-item="true"]'
   
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    schedule = soup.select(SELECTOR)
    for game in schedule:
        if game:
            try:
                datas = game.find_all('div')
                time = datas[7].text
                network = datas[9].text
                visitor = datas[18].span.text
                home = datas[27].span.text
                game_stage, color = stage(time)

                if game_stage == 'FINAL' or game_stage == 'IN_PORGRESS':
                    scores = datas[10].find_all('div')
                    home_score = scores[12].text
                    away_score = scores[3].text
                    visitor = f'{away_score} {visitor}'
                    home = f'{home_score} {home}'
                
                game_info = f'{time} {network} - {visitor} at {home}'
                print(colored(game_info, color))
            except IndexError as e:
                pass

if __name__ == '__main__':
    os.system('clear')
    parser = argparse.ArgumentParser()
    parser.add_argument('--feed', '-f', type=str, default='nfl')
    args = parser.parse_args()
    main(args.feed)