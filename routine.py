
class Routine:

    data = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []}
    
    def __init__(self, date, sport, duration):
        self.date = date
        self.sport = sport
        self.duration = duration
    
    def __repr__(self):
        return "On {date} you have {sport} for {duration}!".format(date = self.date, sport = self.sport, duration = self.duration)
    
    # Allocate the parameters to the daily routine lists
    def setActivity(self, data):
        data[self.date] = [self.sport, self.duration]