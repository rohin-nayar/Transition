#!/usr/bin/env python

"""\ 
Transition: Data visualisation for personal exercise and sport activity
"""

from functools import reduce
import pandas as pd
import matplotlib.pyplot as plt

test = pd.read_csv("Data/Training_Records.csv")
print(test.head(5))
test['Date'] = pd.to_datetime(test['Date'],dayfirst=True)
sum_duration_by_date = test.groupby('Date')['Duration (min)'].sum().reset_index()
sum_duration_by_date.plot(x ="Date",y = "Duration (min)",kind='scatter')
plt.show()

class Data:

    def __init__(self,fileData,variables):
        self.fileData = fileData
        self.variables = variables

    def getData(self,parameter):
        load_data = pd.read_csv("Data/Training_Records.csv")

    def setData(self,fileData):
        self.fileData = fileData
    
    def setVariable(self,variables):
        self.variables = variables



# Print the result
print(sum_duration_by_date)
# class Routine:

#     data = {
#         'Monday': [],
#         'Tuesday': [],
#         'Wednesday': [],
#         'Thursday': [],
#         'Friday': [],
#         'Saturday': [],
#         'Sunday': []}
    
#     def __init__(self, date, sport, duration, NumberOfSessions):
#         self.date = date
#         self.sport = sport
#         self.duration = duration
#         self.NumberOfSessions = NumberOfSessions
    
#     def __repr__(self):
#         return "On {date} you have {sport} for {duration}!".format(date = self.date, sport = self.sport, duration = self.duration)
    
#     # Allocate the parameters to the data dictionary
#     def setActivity(self,data):
#         data[self.date] = [self.sport, self.duration, self.NumberOfSessions]

#     # Store entries to a text file or csv file 
    
#     # Can use a dataframe to store and access data too

#     # Retrieve data depending on input dates
#     def getActivity(self):