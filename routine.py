from functools import reduce
import pandas as pd
import matplotlib.pyplot as plt


# Concept is to have this record my workouts and perhaps write it to a file
# Also want to plot a basic activity graph to track and keep record of 
# the number of swim, gym, cycling and running sessions completed 
# during the week

test = pd.read_csv("Data/Records.csv")
print(test.head(5))
test['Date'] = pd.to_datetime(test['Date'],dayfirst=True)
sum_duration_by_date = test.groupby('Date')['Duration (min)'].sum().reset_index()
sum_duration_by_date.plot(x ="Date",y = "Duration (min)",kind='scatter')
plt.show()



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