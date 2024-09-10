import argparse
from scraper import scrape_roster
from classes.team import Team

if __name__ == '__main__':
    print('Scraping Team Rosters')
    parser = argparse.ArgumentParser()
    parser.add_argument('--team', type=str)
    args = parser.parse_args()

    id = Team.find_by_name(args.team)
    scrape_roster(id)