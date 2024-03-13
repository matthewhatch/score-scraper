from datetime import datetime
from termcolor import colored
from utils.feed import get_feed

def print_banner(args):
    current_time = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
    league = None
    if hasattr(args, 'league'):
        league = args.league.upper()
    
    if hasattr(args, 'feed'):
        league = args.feed.upper()

    metadata = f'''
League: {league}
Time: {current_time}
'''
    
    if hasattr(args, 'loop'):
        metadata += f'''Refresh: {args.wait}s\r\n'''

    banner = f'''
 _____                      _____                                
/  ___|                    /  ___|                               
\ `--.  ___ ___  _ __ ___  \ `--.  ___ _ __ __ _ _ __   ___ _ __ 
 `--. \/ __/ _ \| '__/ _ \  `--. \/ __| '__/ _` | '_ \ / _ \ '__|
/\__/ / (_| (_) | | |  __/ /\__/ / (__| | | (_| | |_) |  __/ |   
\____/ \___\___/|_|  \___| \____/ \___|_|  \__,_| .__/ \___|_|   
                                                | |              
                                                |_|              
          
Getting Sports Scores From Yahoo! Sports
-----------------------------------------------------------------
{metadata}
-----------------------------------------------------------------
'''

    print(colored(banner, 'cyan'))
