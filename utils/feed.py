FEEDS = {
    'NBA': 'nba',
    'NFL': 'nfl',
    'COLLEGE BASKETBALL': 'college-basketball',
    'NCAAM': 'college-basketball',
    'NHL': 'nhl',
    'NCAAW': 'college-womens-basketball',
    'TENNIS': 'tennis'
}

def get_feed(sport):
    return FEEDS[sport.upper()]


