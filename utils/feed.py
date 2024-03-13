from utils.constants import NFL_FEED, NHL_FEED, NBA_FEED

FEEDS = {
    'NBA': NBA_FEED,
    'NFL': NFL_FEED,
    'COLLEGE BASKETBALL': 'college-basketball',
    'NCAAM': 'college-basketball',
    'NHL': NHL_FEED,
    'NCAAW': 'college-womens-basketball',
    'TENNIS': 'tennis'
}

def get_feed(sport):
    return FEEDS[sport.upper()]
