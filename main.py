"""
main.py is the file representing the dashboard application

@author     thique-atto/Daphne
@version    1.0
@since      11/3/2019
"""

# import environments to be used
import pandas as pd 
import datetime
from calendar import monthrange

# declaration of constants
LIST_OF_ISLANDS = ['Oahu', 'Hawaii Island', 'Maui', 'Sample']
LIST_OF_OAHU_SITES = ['Dole Plantation','Ko\'olau Center', 'Kapolei Commons', 'Hawai\'i Kai 7-Eleven', 'Ward 1', 'Ward 2', 'Wai\'anae Mall', '801 Dilingham'] 
LIST_OF_HAWAII_ISLAND_SITES = ['HELCO Hilo', 'HELCO Kona', 'Waimea KTA', 'The Shops at Mauna Lani']
LIST_OF_MAUI_SITES = ['MECO Kahului', 'Kaunakakai']
LIST_OF_SAMPLE_SITES = ['SiteA', 'SiteB']
LIST_OF_DURATIONS = ['Yearly', 'Monthly', 'Weekly', 'Daily', 'Hourly']


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

    graphDuration = chooseDurationForGraph()
    print(graphDuration)

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


def chooseDurationForGraph():
    
    #Choose duration
    print('Duration: ')
    for duration in LIST_OF_DURATIONS:
        print('[' + str(LIST_OF_DURATIONS.index(duration)) + '] ' + duration)
    durationInput = int(input("Island Choice (index): "))

    if (durationInput == 0): #yearly
        year = int(input("Year: "))
        startDate = datetime.date(year,1,1)
        endDate = datetime.date(year,12,31)
    elif (durationInput == 1): #monthly
        year = int(input("Year: "))
        month = int(input("Month: "))
        startDate = datetime.date(year, month, 1)
        endDate = datetime.date(year, month, monthrange(year, month)[1])
    elif (durationInput == 2): #weekly
        year = int(input("Starting Year: "))
        month = int(input("Starting Month: "))
        day = int(input("Starting Day: "))
        startDate = datetime.date(year, month, day)
        endDate = startDate + datetime.timedelta(days=6)
    
    duration = [startDate,endDate]
    return duration

def createPowerTimeGraph(site):
    # adding values to an array 
    #site.powerData = site.powerDataFrame.values.tolist()
    return

def createGraph():
    return

main()