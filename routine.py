"""\ 
Transition: Data visualisation for personal exercise and sport activity
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import MonthLocator

#Enables control over what parameters to plot
#to understand specifics such as consistency for duration of swims

class DataAnalyser:
    
    def __init__(self, dataRecords):
        self.dataRecords = dataRecords

    def loadData(self):
        self.data = pd.DataFrame(pd.read_csv(self.dataRecords))
        print(self.data.head(5))
        self.data['Date'] = pd.to_datetime(self.data['Date'])

    def plotData(self):
        fig, ax = plt.subplots()
        sns.set_theme()
        sns.lineplot(x='Date', y='Body Weight (kg)', data=self.data, marker='o', color='b')  
        ax.xaxis.set_major_locator(MonthLocator(interval=1))
        plt.xlabel('Date')
        plt.ylabel('Body Weight (kg)')
        plt.title('Body Weight Over Time')
        plt.tight_layout()
        plt.show()

# Example for testing
example = DataAnalyser(dataRecords="Data/Records.csv")
example.loadData()
example.plotData()
