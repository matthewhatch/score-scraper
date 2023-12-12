from termcolor import colored
from utils.feed import get_feed

def print_banner(args):
    refresh = ''
    if args.loop:
        refresh = f'refresh: {args.wait}s'

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
feed: {args.feed.upper()}
{refresh}
-----------------------------------------------------------------
    '''

    print(colored(banner, 'cyan'))
