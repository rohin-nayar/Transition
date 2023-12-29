"""\ 
Transition: Data visualisation for personal exercise and sport activity
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import MonthLocator

class DataAnalyser:
    
    def __init__(self, dataRecords):
        self.dataRecords = dataRecords

    def loadData(self):
        self.data = pd.read_csv(self.dataRecords)
        print(self.data.head(5))
        self.data['Date'] = pd.to_datetime(self.data['Date'])

    def plotData(self, xval='Date', yvals=['Body Weight (kg)', 'Duration (min)']):
        sns.set_theme()
        sns.set_style("whitegrid")

        # Create subplots
        fig, axes = plt.subplots(nrows=len(yvals), figsize=(12, 7))

        # Plot each set of data on its respective subplot
        for idx, yval in enumerate(yvals):
            if yval == 'Duration (min)':
                # Use bar plot for Duration
                sns.barplot(x=xval, y=yval, data=self.data, color='b', ax=axes[idx])
                # Set x-axis major ticks at monthly intervals
                axes[idx].xaxis.set_major_locator(plt.MaxNLocator(nbins=12))

            else:
                # Use line plot for other variables
                sns.lineplot(x=xval, y=yval, data=self.data, marker='o', color='g', ax=axes[idx])
                axes[idx].set_xlabel(xval)
                axes[idx].set_ylabel(yval)

        plt.tight_layout()
        plt.show()

# Example for testing
example = DataAnalyser(dataRecords="Data/Records.csv")
example.loadData()
example.plotData()