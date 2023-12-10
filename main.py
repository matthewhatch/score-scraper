import requests
import os

from bs4 import BeautifulSoup
from termcolor import colored

def main():
    URL = 'https://sports.yahoo.com/nfl'
    SELECTOR = 'li[data-carousel-item="true"]'
    FINAL_TEXT = ['FINAL', 'FINAL/OT', 'FINAL/SO']
    GAME_STAGE = ['1st', '2nd', '3rd', '4th']

    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    schedule = soup.select(SELECTOR)
    for game in schedule:
        COLOR = 'light_grey'
        if game:
            try:
                datas = game.find_all('div')
                time = datas[7].text
                network = datas[9].text
                visitor = datas[18].span.text
                home = datas[27].span.text
            
                if time.split()[0].upper() in FINAL_TEXT or time.split()[1] in GAME_STAGE:
                    if time.split()[0].upper() in FINAL_TEXT:
                        COLOR = 'light_green'
                    else:
                        COLOR = 'cyan'

                    # COLOR = 'light_green'
                    scores = datas[10].find_all('div')
                    home_score = scores[12].text
                    away_score = scores[3].text
                    visitor = f'{away_score} {visitor}'
                    home = f'{home_score} {home}'
                
                game_info = f'{time} {network} - {visitor} at {home}'
                print(colored(game_info, COLOR))
            except IndexError as e:
                pass

if __name__ == '__main__':
    os.system('clear')
    main()