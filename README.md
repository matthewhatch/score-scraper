```

 _____                      _____                                
/  ___|                    /  ___|                               
\ `--.  ___ ___  _ __ ___  \ `--.  ___ _ __ __ _ _ __   ___ _ __ 
 `--. \/ __/ _ \| '__/ _ \  `--. \/ __| '__/ _` | '_ \ / _ \ '__|
/\__/ / (_| (_) | | |  __/ /\__/ / (__| | | (_| | |_) |  __/ |   
\____/ \___\___/|_|  \___| \____/ \___|_|  \__,_| .__/ \___|_|   
                                                | |              
                                                |_|              
          
```
Scraping Score from Yahoo! Sports. Its faster than waiting for the ticker
install:
```shell
git clone git@github.com:matthewhatch/score-scraper.git
cd score-scraper
python -m venv env
source env/bin/activate
```

usage:
```shell
# scrape nhl scores and refresh every 30 seconds
python score_scraper.py --league nhl --loop --wait 30

# scrape nba score and refresh deafult 15 seconds
python score_scraper.py -league nba --loop
```

tests:
```shell
# single run
python -m unittest discover -s tests/*

# watch files and run tests on changes... like watch
ls . | entr -c python -m unittest discover -s tests/*
```
