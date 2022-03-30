# Predicting the Detroit Tigers' Home Game Attendance Numbers
## Project Overview
Here I discuss my first personal data science project in which I predict the Detroit Tigers home attendance numbers for the 2018 and 2019 seasons by training on data from the 2013-2017 seasons and inputting 2018-2019 test data to machine learning (ML) models. This repo contains the code I wrote to collect/wrangle the data and to run the ML models for this project. This project topic was selected based on some personal interest in the sport and suitability with my current skill level.

Predictions were made with multiple linear regression, random forest regression, and support vector regression models. Upon comparison with actual 2018-2019 home attendance data, it was found that the multiple linear regression model yielded the best results.

## Code and Resources Used
- Python Version: 3.8
- Packages: pandas, numpy, sklearn, matplotlib, seaborn
- Web wrapper Github: https://github.com/toddrob99/MLB-StatsAPI

Special recognition should be given to Todd Roberts’ MLB Stats API Python web wrapper. Almost all the data used in this project’s analyses were extracted and collected via this Python package written by Mr. Roberts, which pulls data from mlb.com. The package can be easily installed to a Python environment, and its methods can be invoked to return data structures containing the pertinent information.

## Web Wrapping and Data Collection
The MLB Stats API wrapper was used to collect the following data for each game in the 2013-2019 seasons:
- Game date
- Day of the week that each game was played
- Game start time
- Temperature (F)
- Weather conditions
- Opponent
- Home starting pitcher
- Opponent starting pitcher
- Tigers’ win rate entering each game
- Opponent’s win rate entering each game
- Game attendance

## Data Cleaning and Wrangling
After collection, cleaned and wrangled the data so that it can used to run machine learning (ML) models. I created the following variables/features:
- Game number: I assigned a number to each home game in chronological order (0 for the home-opener, 1 for the 2nd home game, etc.). The numbering starts over for each new season.
- The day of the week that the game was played, where each day is represented by an integer (0-6 = Mon-Sun).
- Game start time: transformed to military time so that ML models read them chronologically (e.g., a 12:10pm start time won’t be interpreted as a later start time than 7:10pm). Times were also converted to decimal form (e.g., 7:15pm start time is inputted to ML models as 19.25).
- Weather conditions: There are six categories of weather conditions represented as integers.
  - Clear = 5
  - Sunny = 5
  - Partly Cloudy = 4
  - Cloudy = 3
  - Overcast = 2
  - Drizzle = 1
  - Rain = 1
- Home starting pitcher represented as integers: 6 used for the best starter (ace), 5 for the next pitcher in the rotation, and so on down to 1. Since the rotation can change throughout a season, I determined these integers subjectively (see pitchers_list.py) based on the season-ending statistics of each team’s pitchers, such as ERA, record, number of starts, number of innings pitched, and, if necessary, previous season’s performance.
- Opponent starting pitchers were categorized in the same manner as home starters.
- Tigers’ win rate entering each game. The first 15 home games’ win rate were replaced with the previous season’s final win rate.
- Attendance is the dependent variable to be predicted. Since home-openers consistently bring full-stadium crowds, I used the average of the training data's home-opener attendances to predict the attendance of 2018-2019 home-openers.

## Data Analysis and Model Building
Below is a correlation heat map chart of the features.
![corr_heat_map](https://user-images.githubusercontent.com/90481059/160762654-e788cafe-069a-46e3-af80-bdb28d460790.png)
This chart was used to detect multicollinearity, which revealed significant correlation (0.52) between Game Number and Temperature. This makes sense since the temperature trend increases as the season progresses into the summer and early fall. To address this, a new feature called “Game+Temp” was created, which is simply the sum of the Game Number and Temperature arrays.

## Results
I first focused on the multiple linear regression (ordinary least squares) model to make attendance predictions. Predictions were evaluated with two methods:
1.	Predicted vs actual average season attendance
2.	Mean absolute error (MAE)
After experimenting, I found that removing some of the features improved the results. Therefore, the final features used are:
- Game+Temp: sum of game number and temperature feature arrays.
- Day (0-6 = Mon-Sun)
- Game start time
- Weather condition
- Win rate
- Opponent’s win rate
 
The table below shows comparisons of actual vs predicted attendance using the final set of features.
![lin_reg_results_table](https://user-images.githubusercontent.com/90481059/160764840-46752dd7-1dad-4d17-9097-e90b0efa2cd0.PNG)
