"""
main.py is the file representing the dashboard application

@author     thique-atto/Daphne
@version    2.0
@since      11/3/2019
"""

# import environments to be used
import pandas as pd 
import datetime
from calendar import monthrange
import plotly.graph_objects as go

# declaration of constants
LIST_OF_ISLANDS = ['Oahu', 'Hawaii Island', 'Maui', 'Sample']
LIST_OF_OAHU_SITES = ['Dole Plantation','Ko\'olau Center', 'Kapolei Commons', 'Hawai\'i Kai 7-Eleven', 'Ward 1', 'Ward 2', 'Wai\'anae Mall', '801 Dilingham'] 
LIST_OF_HAWAII_ISLAND_SITES = ['HELCO Hilo', 'HELCO Kona', 'Waimea KTA', 'The Shops at Mauna Lani']
LIST_OF_MAUI_SITES = ['MECO Kahului', 'Kaunakakai']
LIST_OF_SAMPLE_SITES = ['SiteA', 'SiteB']
LIST_OF_DURATIONS = ['Yearly', 'Monthly', 'Weekly', 'Daily', 'Hourly', 'Sample']


class Site:
    def __init__(self, siteName):
        self.siteName = siteName

    def printSiteName(self):
        print('Analyzing site: ' + self.siteName)
    
    def gatherPowerData(self):
        # open file containing power data for site
        self.powerDataFrame = pd.read_excel(self.siteName + ' power.xlsx', sheet_name='Power Data')

    def gatherTransactions(self):
        # open csv file containing transactions
        allData = pd.read_csv("Data_HACC.csv") 
        
        # if-else: For sample data purposes only. For real data, use only 'else' condition
        if self.siteName == 'SiteA':  
            self.transactions = allData[allData['Charge Station Name'] == 'A']
        elif self.siteName == 'SiteB':
            self.transactions = allData[allData['Charge Station Name'] == 'B']
        else:
            self.transactions = allData[allData['Charge Station Name'] == self.siteName]

def main():

    # For testing purposes:
    site = Site('SiteA')
    #site = Site(chooseSite())
    print('')
    site.printSiteName()

    # Gather power data from site
    site.gatherPowerData()
    print('Gathering Power Data...')
    print(site.powerDataFrame)

    # Gather transactions from site
    site.gatherTransactions()
    print('\nGathering Transactions...')
    print(site.transactions)

    #graphDuration = chooseDurationForGraph()
    #print(graphDuration)
    #createPowerTimeGraph(site.powerDataFrame, graphDuration)
    createPowerTimeGraph(site.powerDataFrame)

def chooseSite():

    # Choose which site to analyze data from
    print('Choose an island from list below:')
    for island in LIST_OF_ISLANDS:
        print('[' + str(LIST_OF_ISLANDS.index(island)) + '] ' + island)
    islandInput = int(input("Island Choice (index): "))

    print('Choose a site from list below:')
    if (islandInput == 0):
        for site in LIST_OF_OAHU_SITES:
            print('[' + str(LIST_OF_OAHU_SITES.index(site)) + '] ' + site)
        siteName = LIST_OF_OAHU_SITES[int(input("Site Choice (index): "))]
    elif (islandInput == 1):
        for site in LIST_OF_HAWAII_ISLAND_SITES:
            print('[' + str(LIST_OF_HAWAII_ISLAND_SITES.index(site)) + '] ' + site)
        siteName = LIST_OF_HAWAII_ISLAND_SITES[int(input("Site Choice (index): "))]
    elif (islandInput == 2):
        for site in LIST_OF_MAUI_SITES:
            print('[' + str(LIST_OF_MAUI_SITES.index(site)) + '] ' + site)
        siteName = LIST_OF_MAUI_SITES[int(input("Site Choice (index): "))]
    elif (islandInput == 3):
        for site in LIST_OF_SAMPLE_SITES:
            print('[' + str(LIST_OF_SAMPLE_SITES.index(site)) + '] ' + site)
        siteName = LIST_OF_SAMPLE_SITES[int(input("Site Choice (index): "))]

    return siteName

"""
def chooseDurationForGraph():
    
    #Choose duration
    print('Duration: ')
    for duration in LIST_OF_DURATIONS:
        print('[' + str(LIST_OF_DURATIONS.index(duration)) + '] ' + duration)
    durationInput = int(input("Island Choice (index): "))

    if (durationInput == 0): #yearly
        year = int(input("Year: "))
        start = datetime.datetime(year, 1, 1, 0, 0, 0)
        end = datetime.datetime(year, 12, 31, 23, 59, 0)
    elif (durationInput == 1): #monthly
        year = int(input("Year: "))
        month = int(input("Month: "))
        start = datetime.datetime(year, month, 1, 0, 0, 0)
        end = datetime.datetime(year, month, monthrange(year, month)[1], 23,59, 0)
    elif (durationInput == 2): #weekly
        year = int(input("Starting Year: "))
        month = int(input("Starting Month: "))
        day = int(input("Starting Day: "))
        start = datetime.datetime(year, month, day, 0, 0, 0)
        end = start + datetime.timedelta(days=6, hours=23, minutes=59)
    elif (durationInput == 3): #daily
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        start = datetime.datetime(year, month, day, 0, 0, 0)
        end = datetime.datetime(year, month, day, 23, 59, 0)
    elif (durationInput == 4): #hourly
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        hour = int(input("Hour: "))
        start = datetime.datetime(year, month, day, hour, 0, 0)
        end = start + datetime.timedelta(minutes=59)
    else: #testing
        start = datetime.datetime(2018, 9, 1, 11, 7, 0)
        end = datetime.datetime(2018, 9, 1, 11, 40, 0)
    
    duration = [start,end]
    return duration

def createPowerTimeGraph(data, duration):
    #adding values to an array 
    dataValues = data.values.tolist()
    x_values = []
    y_values = []

    for time, power in dataValues:
        if (time >= duration[0] and time < duration[1]):
            x_values.append(time)
            y_values.append(power)

    fig = go.Figure(data=go.Scatter(x=x_values, y=y_values))
    fig.show()
"""
# source code: https://plot.ly/python/range-slider/
def createPowerTimeGraph(data):

    # Create figure
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=list(data['Start Date and Time']), y =list(data['Power (kW)']))
    )

    # Title of graph
    fig.update_layout(
        title_text = 'Power vs. Time'
    )

    # Add range selector and slider
    fig. update_layout(
        xaxis = go.layout.XAxis(
            rangeselector = dict(
                buttons = list([
                    dict(count = 1,
                         label = 'YTD',
                         step = 'year',
                         stepmode = 'todate'),
                    dict(count = 1,
                         label = 'Yearly',
                         step = 'year',
                         stepmode = 'backward'),
                    dict(count = 6,
                         label = '6 Months',
                         step = 'month',
                         stepmode = 'backward'),
                    dict(count = 1,
                         label = 'Monthly',
                         step = 'month',
                         stepmode = 'backward'),
                    dict(count = 7,
                         label = 'Weekly',
                         step = 'day',
                         stepmode = 'backward'),
                    dict(count = 1,
                         label = 'Daily',
                         step = 'day',
                         stepmode = 'backward'),
                    dict(count = 1,
                         label = 'Hourly',
                         step = 'hour',
                         stepmode = 'backward'),
                    dict(count = 30,
                         label = '30 Minutes',
                         step = 'minute',
                         stepmode = 'backward'),
                    dict(step = 'all')
                ])
            ),
            rangeslider = dict(
                visible = True
            ),
            type = 'date'
        )
    )

    fig.show()

def createGraph():
    return

main()