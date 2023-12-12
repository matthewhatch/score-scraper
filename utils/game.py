def get_stage(time):
    FINAL_TEXT = ['FINAL', 'FINAL/OT', 'FINAL/SO']
    GAME_STAGE = ['1st', '2nd', '3rd', '4th']
    
    if time.split()[0].upper() in FINAL_TEXT:
        return 'FINAL', 'light_green'

    if time.split()[1] in GAME_STAGE:
        return 'IN_PROGRESS', 'light_cyan'
    
    return 'NOT_STARTED', 'dark_grey' 
