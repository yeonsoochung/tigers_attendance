"""
YSC's Detroit Tigers Attendance Project
"""
import statsapi
import re
import pandas as pd
import datetime
from pitchers_list import starters_by_int

det_stad_cap = 41083 # Comerica Park capacity

team_codes = ['ariz', 'atl', 'bal', 'bos', 'chc', 'cws', 'cin', \
              'cle', 'col', 'det', 'hou', 'kc', 'angels', 'dodgers', \
               'mia', 'mil', 'min', 'nym', 'nyy', 'oak', 'phi', \
               'pit', 'sd', 'sf', 'sea', 'stl', 'tb', 'tex', 'tor', \
               'was']

# dict of each team's divisionID (needed for computing win %)
div_dict = {'Baltimore Orioles': 201, 'Boston Red Sox': 201, \
                   'New York Yankees': 201, 'Tampa Bay Rays': 201, \
                   'Toronto Blue Jays': 201, 'Chicago White Sox': 202, \
                   'Cleveland Indians': 202, 'Detroit Tigers': 202, \
                   'Kansas City Royals': 202, 'Minnesota Twins': 202, \
                   'Houston Astros': 200, 'Los Angeles Angels': 200, \
                   'Oakland Athletics': 200, 'Seattle Mariners': 200, \
                   'Texas Rangers': 200, 'Atlanta Braves': 204, \
                   'Miami Marlins': 204, 'New York Mets': 204, \
                   'Philadelphia Phillies': 204, 'Washington Nationals': 204, \
                   'Chicago Cubs': 205, 'Cincinnati Reds': 205, \
                   'Milwaukee Brewers': 205, 'Pittsburgh Pirates': 205, \
                   'St. Louis Cardinals': 205, 'Arizona Diamondbacks': 203, \
                   'Colorado Rockies': 203, 'Los Angeles Dodgers': 203, \
                   'San Diego Padres': 203, 'San Francisco Giants': 203}

det_game_ids_2013 = [] # list of gamePks for Detroit's 2013 season
det_game_dates_2013 = [] # list of game dates
det_game_day_2013 = [] # list of game day of week (int 0-6)
det_against_2013 = [] # list of opponents
det_homePitcher_2013 = [] # list of tiger starting pitchers
det_awayPitcher_2013 = [] # list of opposing starting pitchers
for game in statsapi.schedule(start_date='2013-01-01', \
                              end_date='2013-12-31', team=116):
    if game['game_type'] == 'R' and game['home_name'] == 'Detroit Tigers' and \
        game['status'] != 'Postponed' and game['status'] != 'Cancelled':
        det_game_ids_2013.append(game['game_id'])
        det_game_dates_2013.append(game['game_date'])
        det_against_2013.append(game['away_name'])
        det_homePitcher_2013.append(game['home_probable_pitcher'])
        det_awayPitcher_2013.append(game['away_probable_pitcher'])

# ====================================================================
# This section creates a list of integers 0-6 representing day of week that game
# is played.
det_game_day_2013 = det_game_dates_2013[:]
# below: make each element of det_game_day_2013 a list [year, month, day]
for i in range(len(det_game_dates_2013)):
    det_game_day_2013[i] = [int(det_game_dates_2013[i][:4]), \
                            int(det_game_dates_2013[i][5:7]), \
                            int(det_game_dates_2013[i][8:])]

for i in range(len(det_game_dates_2013)): # create list of game day of week (int)
    det_game_day_2013[i] = datetime.date(det_game_day_2013[i][0], \
                                         det_game_day_2013[i][1], \
                                         det_game_day_2013[i][2]).weekday()
# ====================================================================
# Change date format in det_game_dates_2013 from yyyy-mm-dd to mm/dd/yyyy. This
# format is desired because it is later used to extract data when computing team win %.
for i in range(len(det_game_dates_2013)):
    det_game_dates_2013[i] = datetime.datetime.strptime(det_game_dates_2013[i], \
                                                        '%Y-%m-%d').strftime('%m/%d/%Y')
# ====================================================================
# Represent starting pitchers with integers 1-6, where 1 means they are their team's
# best pitcher, etc. 
# Home starters
home_starters_int_2013 = []
for pitcher in det_homePitcher_2013:
    if pitcher in starters_by_int[2013][6]:
        home_starters_int_2013.append(6)
    elif pitcher in starters_by_int[2013][5]:
        home_starters_int_2013.append(5)
    elif pitcher in starters_by_int[2013][4]:
        home_starters_int_2013.append(4)
    elif pitcher in starters_by_int[2013][3]:
        home_starters_int_2013.append(3)
    elif pitcher in starters_by_int[2013][2]:
        home_starters_int_2013.append(2)
    else:
        home_starters_int_2013.append(1)
        
# Away starters
away_starters_int_2013 = []
for pitcher in det_awayPitcher_2013:
    if pitcher in starters_by_int[2013][6]:
        away_starters_int_2013.append(6)
    elif pitcher in starters_by_int[2013][5]:
        away_starters_int_2013.append(5)
    elif pitcher in starters_by_int[2013][4]:
        away_starters_int_2013.append(4)
    elif pitcher in starters_by_int[2013][3]:
        away_starters_int_2013.append(3)
    elif pitcher in starters_by_int[2013][2]:
        away_starters_int_2013.append(2)
    else:
        away_starters_int_2013.append(1)
# ====================================================================
# Create list of Tigers' win % as season progresses and list of opponent's
# win %. First 15 home game win % (or ~30 regular season games) are replaced
# with previous season's final win % (regular season). Same for opponent.

# Create list of Tigers' win rate GOING INTO each game.
det_win_rate_2013 = []
for i in range(len(det_game_dates_2013)):
    if i < 15:
        standings = statsapi.standings_data(leagueId="103", division="all", \
                       include_wildcard=False, season='2012', standingsTypes=None, \
                       date=None)
        for j in standings[div_dict['Detroit Tigers']]['teams']:
            if j['name'] == 'Detroit Tigers':
                det_win_rate_2013.append(j['w']/(j['w']+j['l']))
    else:
        standings = statsapi.standings_data(leagueId="103", division="all", \
                       include_wildcard=False, season=None, standingsTypes=None, \
                       date=det_game_dates_2013[i-1])
        for j in standings[div_dict['Detroit Tigers']]['teams']:
            if j['name'] == 'Detroit Tigers':
                det_win_rate_2013.append(j['w']/(j['w']+j['l']))

# Create list of visiting team's win rate GOING INTO each game.
visitors_win_rate_2013 = []
for i in range(len(det_against_2013)):
    if i < 15:
        standings = statsapi.standings_data(leagueId="103,104", division="all", \
                       include_wildcard=False, season='2012', standingsTypes=None, \
                       date=None)
        for j in standings[div_dict[det_against_2013[i]]]['teams']:
            if j['name'] == det_against_2013[i]:
                visitors_win_rate_2013.append(j['w']/(j['w']+j['l']))
    else:
        standings = statsapi.standings_data(leagueId="103,104", division="all", \
                       include_wildcard=False, season=None, standingsTypes=None, \
                       date=det_game_dates_2013[i-1])
        for j in standings[div_dict[det_against_2013[i]]]['teams']:
            if j['name'] == det_against_2013[i]:
                visitors_win_rate_2013.append(j['w']/(j['w']+j['l']))
# ====================================================================
det_game_time_2013 = [] # list of game start time (first pitch)
det_game_weather_2013 = [] # list of game weather before split into temp & cond
det_game_temp_2013 = [] # list of game weather temperature
det_game_cond_2013 = [] # list of game weather conditions
det_game_att_2013 = [] # list of game attendance
det_game_att_dec_2013 = [] # list of game attendance as decimal of stad cpcty

for game_id in det_game_ids_2013:
    det_game_time_2013.append(statsapi.boxscore_data(game_id)\
                               ['gameBoxInfo'][-5]['value'])
    det_game_weather_2013.append(statsapi.boxscore_data(game_id)\
                               ['gameBoxInfo'][-7]['value'])
    det_game_att_2013.append(int(re.sub('[,.]', '', \
                               statsapi.boxscore_data(game_id)\
                               ['gameBoxInfo'][-3]['value'])))
# ====================================================================
# Clean weather data.
# split weather data into temp and cond
for weather in det_game_weather_2013:
    det_game_temp_2013.append(int(re.split(' degrees, ', weather)[0]))
    det_game_cond_2013.append(re.split(' degrees, ', weather)[1][:-1])

# classify weather conditions as integers: clear=1, sunny=2, partly cloudy=3, \
    # cloudy=4, overcast=5, drizzle=6
det_game_cond_int_2013 = det_game_cond_2013[:]
cond_int_dict = {'Clear': 5, 'Sunny': 5, 'Partly Cloudy': 4, 'Cloudy': 3, \
                 'Overcast': 2, 'Drizzle': 1, 'Rain': 1}
for i in range(len(det_game_cond_int_2013)):
    det_game_cond_int_2013[i] = cond_int_dict[det_game_cond_int_2013[i]]
# ==================================================================== 
# Divide attendance by stadium capacity
det_game_att_dec_2013 = [att/det_stad_cap for att in det_game_att_2013]
# ====================================================================
# Convert entries in game_start to military time
det_game_time_mil_2013 = det_game_time_2013[:]
for i in range(len(det_game_time_mil_2013)):
    det_game_time_mil_2013[i] = re.split('[: .]', det_game_time_mil_2013[i])[:-1]
    if det_game_time_mil_2013[i][0] == '12':
        det_game_time_mil_2013[i][0] = 12
    elif det_game_time_mil_2013[i][-1] == 'PM':
        det_game_time_mil_2013[i][0] = int(det_game_time_mil_2013[i][0]) + 12
    else:
        det_game_time_mil_2013[i][0] = int(det_game_time_mil_2013[i][0])
    det_game_time_mil_2013[i] = det_game_time_mil_2013[i][0] + \
        float(det_game_time_mil_2013[i][1])/60
# ====================================================================
# Create data frame.
det_game_att_2013_df = pd.DataFrame({'Game ID': det_game_ids_2013, \
                                     'Game Number': list(range(len(det_game_ids_2013))), \
                                     'Game Date': det_game_dates_2013, \
                                     'Day (0-6 = Mon-Sun)': det_game_day_2013, \
                                     # 'Game Start Time': det_game_time_2013, \
                                     'Game Start Time': det_game_time_mil_2013, \
                                     # 'Weather': det_game_weather_2013, \
                                     'Temperature (F)': det_game_temp_2013, \
                                     'Conditions': det_game_cond_2013, \
                                     'Conditions (Int)': det_game_cond_int_2013, \
                                     'Opponent': det_against_2013, \
                                     'Home Starter': det_homePitcher_2013, \
                                     'Home Starter (Int)': home_starters_int_2013, \
                                     'Away Starter': det_awayPitcher_2013, \
                                     'Away Starter (Int)': away_starters_int_2013, \
                                     'Win Rate': det_win_rate_2013, \
                                     "Visitor's Win Rate": visitors_win_rate_2013, \
                                     'Attendance': det_game_att_2013, \
                                     'Attendance/Capacity': det_game_att_dec_2013})

# print(det_game_att_2013_df.head())
det_game_att_2013_df.to_csv('Tigers_Attendance_2013.csv', index=False)



  

