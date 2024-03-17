from utils.constants import NFL_FEED, NHL_FEED, NBA_FEED, NCAAB_FEED

FEEDS = {
    'NBA': NBA_FEED,
    'NFL': NFL_FEED,
    'COLLEGE BASKETBALL': 'college-basketball',
    # 'NCAAM': 'college-basketball',
    'NCAAB': NCAAB_FEED,
    'NHL': NHL_FEED,
    'NCAAW': 'college-womens-basketball',
    'TENNIS': 'tennis'
}

def get_feed(sport, date='next_real'):
    if sport.lower() == 'nfl':
        return FEEDS[sport.upper()]
    
    return f"https://api-secure.sports.yahoo.com/v1/editorial/s/scoreboard?lang=en-US&region=US&tz=America/New_York&ysp_redesign=1&ysp_platform=desktop&leagues={sport.lower()}&date={date}&v=2&ysp_enable_last_update=1"
