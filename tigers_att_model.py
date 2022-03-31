"""
YSC's Detroit Tigers Attendance Project

This file runs a linear regression model to predict attendance.
"""
import pandas as pd
import statsapi
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# =============================================================================
# # This section: aggregate data frames from all seasons.
# from tigers_2013 import det_game_att_2013_df
# from tigers_2014 import det_game_att_2014_df
# from tigers_2015 import det_game_att_2015_df
# from tigers_2016 import det_game_att_2016_df
# from tigers_2017 import det_game_att_2017_df
# from tigers_2018 import det_game_att_2018_df
# from tigers_2019 import det_game_att_2019_df
# 
# # full data for all seasons (all features and attendance)
# det_game_att_df = pd.concat([det_game_att_2013_df, det_game_att_2014_df, \
#                               det_game_att_2015_df, det_game_att_2016_df, \
#                               det_game_att_2017_df, det_game_att_2018_df, \
#                               det_game_att_2019_df])
# 
# det_game_att_df.to_csv('Tigers_Full_Data_2013-2019.csv', index=False) # all data
# =============================================================================
pd.set_option('display.max_columns', None)

data = pd.read_csv(r'C:\Users\Yeon Soo Chung\Documents\KAGGLE\MLB_Proj\Tigers_Full_Data_2013-2019.csv')

# REMOVE THE GAMES WITH 0 ATTENDANCE (due to double header)
zero_att = data['Game Start Time']==0
data = data.drop(data[zero_att].index)

# Add new column to data: game number + temperature
data['Game+Temp'] = data['Game Number'] + data['Temperature (F)']
# print(data.head())

# Below: plot line graph of all attendance data.
plt.figure()
plt.plot(data.Attendance.values, label='all actual')
plt.title('Home Game Attendance for 2013-2019 Seasons')
plt.xlabel('Games (n=564)')
plt.ylabel('Attendance')

# =============================================================================
# # This section: print the descriptive statistics for each season's attendance data.
# data_2013, data_2014, data_2015, data_2016 = [], [], [], []
# data_2017, data_2018, data_2019 = [], [], []
# for i in range(len(data['Game Date'])):
#     if '2013' in data['Game Date'].iloc[i]:
#         data_2013.append(data['Attendance'].iloc[i])
#     elif '2014' in data['Game Date'].iloc[i]:
#         data_2014.append(data['Attendance'].iloc[i])
#     elif '2015' in data['Game Date'].iloc[i]:
#         data_2015.append(data['Attendance'].iloc[i])
#     elif '2016' in data['Game Date'].iloc[i]:
#         data_2016.append(data['Attendance'].iloc[i])
#     elif '2017' in data['Game Date'].iloc[i]:
#         data_2017.append(data['Attendance'].iloc[i])
#     elif '2018' in data['Game Date'].iloc[i]:
#         data_2018.append(data['Attendance'].iloc[i])
#     elif '2019' in data['Game Date'].iloc[i]:
#         data_2019.append(data['Attendance'].iloc[i])
#         
# data_2013 = pd.Series(data_2013)
# data_2014 = pd.Series(data_2014)
# data_2015 = pd.Series(data_2015)
# data_2016 = pd.Series(data_2016)
# data_2017 = pd.Series(data_2017)
# data_2018 = pd.Series(data_2018)
# data_2019 = pd.Series(data_2019)
# 
# print('2013 summary:', data_2013.describe())
# print('2014 summary:', data_2014.describe())
# print('2015 summary:', data_2015.describe())
# print('2016 summary:', data_2016.describe())
# print('2017 summary:', data_2017.describe())
# print('2018 summary:', data_2018.describe())
# print('2019 summary:', data_2019.describe())
# =============================================================================

# Create CSV with the zero-attendance games dropped:
# data.to_csv('Att_Preds_2018-2019_Dropped.csv', index=False)

# =============================================================================
# # original features list w/ attendance for Figure 1 correlation chart:
# # game number and temp are separate
# att_features = ['Game Number', 'Day (0-6 = Mon-Sun)', 'Game Start Time', 'Temperature (F)', \
#                 'Conditions (Int)', 'Home Starter (Int)', 'Away Starter (Int)', \
#                 'Win Rate', "Visitor's Win Rate", 'Attendance']
# =============================================================================
# =============================================================================
# # features list w/ "Game+Temp" and attendance (overall mae = 5647):
# att_features = ['Day (0-6 = Mon-Sun)', 'Game Start Time', 'Game+Temp', \
#                 'Conditions (Int)', 'Home Starter (Int)', 'Away Starter (Int)', \
#                 'Win Rate', "Visitor's Win Rate", 'Attendance']
# =============================================================================
# final features list plus attendance (overall mae = 5553):
att_features = ['Day (0-6 = Mon-Sun)', 'Game Start Time', 'Game+Temp', \
                'Win Rate', "Visitor's Win Rate", 'Attendance']


# Below: SAVE average home-opener attendance for 2013-2017 to use for preds.
# Then REMOVE home-openers so they are not trained on.
home_opener = data['Game Number']==0
opener_att = np.array(data[home_opener].Attendance)
opener_avg = np.mean(opener_att[:5])
data = data.drop(data[home_opener].index)

# train = training data
train = data[att_features][:399] # train on all data for 2013-2017
# print(train.head())
# print(train[-5:])

# test data is all data from 2018-2019 EXCEPT attendance
test = data[att_features[:-1]][399:] # type DataFrame
# print(test.head())
# print(test[-5:])
      
# attendance data from 2018-2019
# actual_att = data[['Attendance']][399:] # gives a Series (creates error later)
actual_att = data.Attendance.values[399:] # gives an array instead of a Series
# print(actual_att[:8])

# correlation plot (need to modify code to plot this for original features list)
plt.figure()
heatmap = sns.heatmap(train.corr(), vmin=-1, vmax=1, annot=True)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Linear Regression Model
y_train = train[['Attendance']]
X_train = train[att_features[:-1]]
X_test = test[att_features[:-1]]
# print(X_test.head())
lr = LinearRegression()
lr.fit(X_train, y_train)
preds = lr.predict(X_test)
preds = [int(i) for i in preds]
# print(preds)

# Re-insert actual home-opener attendances for 2018-2019 (previously dropped)
actual_att = np.insert(actual_att, 0, opener_att[5], axis=None)
actual_att = np.insert(actual_att, 81, opener_att[6], axis=None)

# Insert 2013-2017 home-opener average into preds data (first game of 2018 & 2019)
preds = np.insert(preds, 0, opener_avg, axis=None)
preds = np.insert(preds, 81, opener_avg, axis=None)

# Create columns for difference (preds-actual) and % difference
diff = preds - actual_att
percent_diff = (preds - actual_att)/actual_att
# print(diff[:5])
# print(percent_diff[:5])

print('2018 pred avg:', np.mean(preds[:81]), '2018 actual avg:', np.mean(actual_att[:81]))
print('2019 pred avg:', np.mean(preds[81:]), '2019 actual avg:', np.mean(actual_att[81:]))
print('2018-2019 preds avg:', np.mean(preds), '2018-2019 avg att:', actual_att.mean())
print('2018 MAE:', mean_absolute_error(actual_att[:81], preds[:81]))
print('2019 MAE:', mean_absolute_error(actual_att[81:], preds[81:]))
print('2018-2019 MAE:', mean_absolute_error(actual_att, preds))

# Below: plot line graph of actual and predicted attendance for 2018 and 2019.
plt.figure()
plt.plot(range(len(actual_att)), actual_att, label='Actual')
plt.plot(range(len(preds)), preds, label='Predictions')
plt.title('Linear Regression Results (2018-2019)')
plt.xlabel('Games (n=160)')
plt.ylabel('Home Attendance')
plt.legend()

att_comp = pd.DataFrame({'Actual Att.': actual_att, \
                          'Pred. Att': preds, \
                          'Difference': diff, \
                          '% Difference': percent_diff})

# att_comp.to_csv('Att_Preds_2018-2019.csv', index=False)
# =============================================================================
# # This section is the code above modified to "predict" the 2013 and 2014 season
# # attendances per the "Miscellaneous" section of this project's github README.
# 
# # Below: SAVE average home-opener attendance for 2013-2017 to use for preds.
# # Then REMOVE home-openers so they are not trained on.
# home_opener = data['Game Number']==0
# opener_att = np.array(data[home_opener].Attendance)
# opener_avg = np.mean(opener_att[2:])
# data = data.drop(data[home_opener].index)
# 
# # Train on 2015-2019 and predict 2013-2014
# # training data is all data from 2015-2019
# 
# train_start_index = data[data['Game Date']=='4/8/2015'].index[0]
# # train_start_index = data[train_start].index
# print(train_start_index)
# train = data[att_features][train_start_index:] # train on 2013-2017 data
# # print(train.head())
# # print(train[-5:])
# 
# # test data is all data from 2013-2014 EXCEPT attendance
# test = data[att_features[:-1]][:train_start_index] # type DataFrame
# # print(test.head())
# # print(test[-5:])
#       
# # attendance data from 2013-2014
# # actual_att = data[['Attendance']][399:] # gives a Series
# actual_att = data.Attendance.values[:train_start_index] # gives us an array instead of a Series
# # print(actual_att[:8])
# 
# # # correlation plot
# # plt.figure()
# # heatmap = sns.heatmap(train.corr(), vmin=-1, vmax=1, annot=True)
# 
# # Linear Regression Model
# # Use 2015-2019 data for training
# y_train = train[['Attendance']]
# X_train = train[att_features[:-1]]
# X_test = test[att_features[:-1]]
# # print(X_test.head())
# 
# # import statsmodels.api as sm
# # X_train_copy = X_train[:]
# # X_sm = X_train_copy = sm.add_constant(X_train_copy)
# # model = sm.OLS(y_train, X_train_copy)
# # print(model.fit().summary())
# 
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_absolute_error
# 
# lr = LinearRegression()
# lr.fit(X_train, y_train)
# preds = lr.predict(X_test)
# preds = [int(i) for i in preds]
# # print(preds)
# 
# # Insert home-opener attendance for 2013-2017 into actual_att
# actual_att = np.insert(actual_att, 0, opener_att[5], axis=None)
# actual_att = np.insert(actual_att, 81, opener_att[6], axis=None)
# 
# # Insert 2015-2019 home-opener avg into 2013, 2014
# preds = np.insert(preds, 0, opener_avg, axis=None)
# preds = np.insert(preds, 81, opener_avg, axis=None)
# 
# # Create columns for difference (preds-actual) and % difference
# diff = preds - actual_att
# percent_diff = (preds - actual_att)/actual_att
# # print(diff[:5])
# # print(percent_diff[:5])
# 
# print('2013 pred avg:', np.mean(preds[:81]), '2013 actual avg:', np.mean(actual_att[:81]))
# print('2014 pred avg:', np.mean(preds[81:]), '2014 actual avg:', np.mean(actual_att[81:]))
# print('2013-2014 preds avg:', np.mean(preds), '2013-2014 avg att:', actual_att.mean())
# print('2013 MAE:', mean_absolute_error(actual_att[:81], preds[:81]))
# print('2014 MAE:', mean_absolute_error(actual_att[81:], preds[81:]))
# print('2013-2014 MAE:', mean_absolute_error(actual_att, preds))
# 
# from sklearn.metrics import r2_score
# print('2013 R2 score:', r2_score(actual_att[:81], preds[:81]))
# print('2014 R2 score:', r2_score(actual_att[81:], preds[81:]))
# print('2013-2014 R2 score:', r2_score(actual_att, preds))
# 
# plt.figure()
# plt.plot(range(len(actual_att)), actual_att, label='Actual')
# plt.plot(range(len(preds)), preds, label='Predictions')
# plt.title('Linear Regression Results (2013-2014)')
# plt.xlabel('Games (n=162)')
# plt.ylabel('Home Attendance')
# plt.legend()
# 
# att_comp = pd.DataFrame({'Actual Att.': actual_att, \
#                           'Pred. Att': preds, \
#                           'Difference': diff, \
#                           '% Difference': percent_diff})
# 
# # att_comp.to_csv('Att_Preds_2013-2014.csv', index=False)
# =============================================================================


