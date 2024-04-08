import argparse
import os
import sys

from time import sleep
from utils.banner import print_banner
from games import scrape

if __name__ == '__main__':
    while True:
        try:
            parser = argparse.ArgumentParser()
            parser.add_argument('--league', '-l', type=str, default='nfl', choices=['nfl', 'nhl', 'nba','ncaab','mlb'])
            parser.add_argument('--loop', '-L', action='count', default=0)
            parser.add_argument('--wait', '-w', type=int, default=15, required=False)
            parser.add_argument('--date', '-d', type=str, default='next_real', required=False)
            args = parser.parse_args()
            os.system('clear')

            print_banner(args)
            scrape(args.league, args.date)
            
            if args.loop:
                sleep(args.wait)
            else:
                sys.exit(0)
        except KeyboardInterrupt:
            print('\r\nexiting...')
            sys.exit(0)