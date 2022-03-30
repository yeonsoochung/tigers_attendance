# Predicting the Detroit Tigers' Home Game Attendance Numbers
## Project Overview
Here I discuss my first personal data science project in which I predict the Detroit Tigers professional baseball team's home attendance numbers for the 2018 and 2019 seasons by training on data from the 2013-2017 seasons and inputting 2018-2019 test data to machine learning (ML) models. This repo contains the code I wrote to collect/wrangle the data and to run the ML models for this project. This project topic was selected based on some personal interest in the sport and suitability with my current skill level.

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
After collection, I cleaned and wrangled the data so that it can used to run machine learning (ML) models. I created the following variables/features:
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
The chart in Figure 1 was used to detect multicollinearity, which revealed significant correlation (0.52) between Game Number and Temperature. This makes sense since the temperature trend increases as the season progresses into the summer and early fall. To address this, a new feature called “Game+Temp” was created, which is simply the sum of the Game Number and Temperature arrays.

![corr_heat_map](https://user-images.githubusercontent.com/90481059/160762654-e788cafe-069a-46e3-af80-bdb28d460790.png)
**Figure 1:** A correlation heat map chart of the features.

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
 
**Table 1:** Quantified comparisons of actual vs predicted attendances using the final set of features listed above.
![lin_reg_results_table](https://user-images.githubusercontent.com/90481059/160764840-46752dd7-1dad-4d17-9097-e90b0efa2cd0.PNG)

*% Diff. = |Pred. Average – Actual Average| / Actual Average x 100

Note: The Detroit Tigers’ stadium capacity is 41,083.

![lin_reg_results_graph](https://user-images.githubusercontent.com/90481059/160924072-36aa81ef-cdc2-4374-b0d5-b7b2a5e66eb1.png)

**Figure 2:** Line graph of predicted and actual attendance over the 2018 and 2019 seasons. Note the spikes are the two home openers. Also, n=159 because games with no attendance (due to double-headers) were dropped.

The predictions appear to follow the trends relatively well for 2018, but greatly over-predicts for 2019. The 2019 season was a historically poor season for the Tigers in which they lost 114 games - 2nd worst in franchise history. The model clearly could not fully the take severity of this performance into account with the training data.

Despite a weaker theoretical background in more advanced ML models, I attempted to make better predictions with random forest regressor and support vector regression models. 

**Table 2:** The best MAE obtained after trialing a variety of parameters as inputs to the random forest regressor and support vector regression models.
![rfr_svr_mae_table](https://user-images.githubusercontent.com/90481059/160932633-a8263ebf-e727-4cee-b56b-d08f86ad632c.PNG)

It is very likely that better results than above can be achieved with different parameters. However, based on the number of trials that were run and their results, I believe that the linear regression model produces the best predictions compared to actual.

## 2013-2019 Attendance Statistics
For reference, this section contains statistical descriptions of all actual attendance data collected for this project. 
![all_att_line_graph](https://user-images.githubusercontent.com/90481059/160933920-fbb33dba-d0e8-44db-a394-ed8315578af4.PNG)

**Figure 3:** Graph of attendance of all home games in the 2013-2019 seasons.

**Table 3:** Descriptive statistics of attendance of all home games in the 2013-2019 seasons. 

![all_att_stats_table](https://user-images.githubusercontent.com/90481059/160934113-4197522e-06b0-49cc-9520-ef24498c67d3.PNG)

## Miscellaneous
Out of curiosity, I repeated this same process to train my model on the 2015-2019 seasons and to “predict” the attendance for the 2013-2014 seasons. The Tigers finished first in their division in both of these years, so I thought it would be interesting to see how the model would predict attendance for such seasons. I used the final set of features that gave the best results for 2018-2019.

![lin_reg_2013_2014](https://user-images.githubusercontent.com/90481059/160935812-ad37343d-d4e5-45e1-9483-90b20505b603.PNG)

**Figure 4:** Line graph of predicted and actual attendance for 2013 and 2014 seasons.

**Table 4:** Quantified comparisons of predicted vs actual attendance for 2013 and 2013 seasons.

