from functools import reduce

# Concept is to have this record my workouts and perhaps write it to a file
# Also want to plot a basic activity graph to track and keep record of 
# the number of swim, gym, cycling and running sessions completed 
# during the week

class Routine:

    data = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []}
    
    def __init__(self, date, sport, duration, NumberOfSessions):
        self.date = date
        self.sport = sport
        self.duration = duration
        self.NumberOfSessions = NumberOfSessions
    
    def __repr__(self):
        return "On {date} you have {sport} for {duration}!".format(date = self.date, sport = self.sport, duration = self.duration)
    
    # Allocate the parameters to the data dictionary
    def setActivity(self,data):
        data[self.date] = [self.sport, self.duration, self.NumberOfSessions]

    # Store entries to a text file or csv file 
    
    # Can use a dataframe to store and access data too

    # Retrieve data depending on input dates
    def getActivity(self):

        

