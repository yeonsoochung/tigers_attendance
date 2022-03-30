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


