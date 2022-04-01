# Predicting the Detroit Tigers' Home Game Attendance Numbers
## Project Overview
Here I discuss my first personal data science project in which I predict the Detroit Tigers professional baseball team's home attendance numbers for the 2018 and 2019 seasons. I did this by training on data from the 2013-2017 seasons and inputting 2018-2019 test data to machine learning (ML) models. This repo contains the code I wrote to collect, clean, and wrangle the data; and to run the ML models for this project. This project topic was selected based on my casual interest in the sport and suitability with my current skill levels. The Tigers were selected as they are my home team.

Predictions were made with multiple linear regression, random forest regression, and support vector regression models. Upon comparison with actual 2018-2019 home attendance data, I found that the linear regression model yielded the best results.

## Code and Resources Used
- Python Version: 3.8
- Packages: pandas, numpy, sklearn, matplotlib, seaborn
- Web wrapper Github: https://github.com/toddrob99/MLB-StatsAPI

Special recognition should be given to Todd Roberts’ MLB Stats API Python web wrapper. Almost all the data used in this project’s analyses were extracted and collected via this Python package written by Mr. Roberts, which pulls data from mlb.com. The package can be easily installed to a Python environment, and its methods can be invoked to return data structures containing the pertinent information.

## Web Wrapping and Data Collection
I used the MLB Stats API wrapper to collect the following data for each game in the 2013-2019 seasons:
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
After collecting it, I cleaned and wrangled the data so that it can be used to run ML models. I created the following variables/features:
- Game number: I assigned a number to each home game in chronological order (0 for the home-opener, 1 for the 2nd home game, etc.). The numbering starts over for each new season.
- The day of the week that the game was played, where each day is represented by an integer (0-6 = Mon-Sun).
- Game start time: transformed to military time so that ML models read them chronologically (e.g., a 12:10pm start time won’t be interpreted as a later start time than 7:10pm). Times were also converted to decimal form (e.g., 7:15pm start time is inputted to ML models as 19.25).
- Weather conditions: There are seven categories of weather conditions represented as integers 1-5. Of all the games for which data was collected, only one had the weather condition "Rain", so I grouped it in the same category as "Drizzle." Fans would not really distinguish between "Clear" and "Sunny" conditions when deciding to attend a baseball game, so I grouped those two together as well.
  - Clear = 5
  - Sunny = 5
  - Partly Cloudy = 4
  - Cloudy = 3
  - Overcast = 2
  - Drizzle = 1
  - Rain = 1
- Home starting pitchers represented as integers: 6 used for the best starter (ace), 5 for the next pitcher in the rotation, and so on down to 1. Since the rotation can change throughout a season, I determined these integers subjectively (see pitchers_list.py) based on the season-ending statistics of each team’s pitchers, such as ERA, record, number of starts, number of innings pitched, and, if necessary, previous season’s performance.
- Opponent starting pitchers were represented in the same manner as home starters.
- The Tigers’ win rate entering each game. The first 15 home games’ win rates were replaced with the previous season’s final win rate.
- Attendance is the dependent variable to be predicted. Since home-openers consistently bring full-capacity crowds, I used the average of the training data's home-opener attendances to predict the attendance of 2018-2019 home-openers. The rest of the games were predicted with the regression model.

## Data Analysis and Model Building
The chart in Figure 1 was used to detect multicollinearity, which revealed significant correlation (0.5) between Game Number and Temperature. This makes sense since the temperature trend increases as the season progresses into the summer and early fall. To address this, a new feature called “Game+Temp”, which is simply the sum of the 'Game Number' and 'Temperature (F)' arrays, was created to replace those two features.

![corr_heat_map](https://user-images.githubusercontent.com/90481059/161100308-51f49e81-54d1-4f4c-80e3-49fb6dd6611e.png)

**Figure 1:** A correlation heat map chart of the features.

## Results
I first focused on the multiple linear regression (ordinary least squares) model to make attendance predictions. Predictions were evaluated through two methods:
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

![lin_reg_results_table](https://user-images.githubusercontent.com/90481059/161115973-32271b71-fb01-418e-98f3-6c479b1cd6a0.PNG)

*% Diff. = |Pred. Average – Actual Average| / Actual Average x 100

Note: The Detroit Tigers’ stadium capacity is 41,083.

![lin_reg_results_graph](https://user-images.githubusercontent.com/90481059/161100414-3f0f8f6d-9bac-4144-92ab-12003586b278.png)

**Figure 2:** Line graph of predicted and actual attendance over the 2018 and 2019 seasons. Note the spikes are the two home openers. Also, n=160 because zero-attendance games (due to double-headers) were dropped.

The model results appear to predict relatively well for 2018, but they over-predict for 2019. The 2019 season was a historically poor season for the Tigers in which they lost 114 games (2nd worst in franchise history), which could explain the model's performance for 2019.

Despite a weaker theoretical background in more advanced ML models, I attempted to make better predictions with random forest regressor and support vector regression models. 

**Table 2:** The best MAE's obtained after trialing many different parameter values as inputs to the random forest regressor and support vector regression models.

![rfr_svr_mae_table](https://user-images.githubusercontent.com/90481059/161116531-405c0004-9510-4eb1-8cb9-0431f2b0e4c4.PNG)

It is very likely that better results than above can be achieved with different parameters. However, based on the number of trials that were run (by brute-force method up to a practical point) and their results, I believe that the linear regression model produces the best predictions compared to actual.

## Statistical Summary of 2013-2019 Attendance Data
![all_att_line_graph](https://user-images.githubusercontent.com/90481059/161100523-30f966c4-52e9-4bf1-a8ef-067794f85faf.PNG)

**Figure 3:** Line graph of attendance for all home games in the 2013-2019 seasons.

**Table 3:** Descriptive statistics of attendance for all home games in the 2013-2019 seasons.

![all_att_stats_table](https://user-images.githubusercontent.com/90481059/161116566-a550dad4-c899-4294-bed1-aaf9233a3daf.PNG)

## Miscellaneous
Out of curiosity, I repeated this same process to train my model on the 2015-2019 seasons and to “predict” the attendance for the 2013-2014 seasons. The Tigers finished first in their division in both of these years, so I thought it would be interesting to see how the model would predict attendance for such seasons. Again, I used the final set of features that gave the best results for 2018-2019.

![lin_reg_2013_2014_graph](https://user-images.githubusercontent.com/90481059/161100603-741ebdf3-25cc-4114-9599-2f6cb892777f.PNG)

**Figure 4:** Line graph of predicted and actual attendance for 2013 and 2014 seasons.

**Table 4:** Quantified comparisons of predicted vs actual attendance for 2013 and 2013 seasons.

![lin_reg_2013_2014_table](https://user-images.githubusercontent.com/90481059/161116622-0f40c6ec-ac69-4244-9588-58a02a8dbf94.PNG)

Interestingly, these predictions are much closer to actual. This make sense because a team that generates more excitement would attract larger crowds, and these numbers would have lower variation due to many of these values being close to and limited by a ceiling (i.e. the stadium capacity). On the other hand, how low the floor can be would be harder to predict.

## Code
Descriptions of the Python files written for this project and uploaded to this repo:
- tigers_2013.py, tigers_2014.py, tigers_2015.py, tigers_2016.py, tigers_2017.py, tigers_2018.py, tigers_2019.py contain code for data collection and cleaning/wrangling for each season.
- pitchers_list.py contains a dictionary of pitchers assigned to integers for each season.
- tigers_att_model.py contains the code for building and running the linear regression model.

## Conclusion
This was my first personal data science project in which I collected, cleaned, and wrangled my own data set before using them to implement ML models. I gained valuable practical skills in programming with Python as well as using the pandas and sklearn libraries. I am particularly interested in developing my skills in regression models and predictive analytics, so there will certainly be more projects with this sort of focus on the way.
