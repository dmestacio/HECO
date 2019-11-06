"""
main.py is the file representing the dashboard application

@author     Daphne Marie Tapia
@version    1.0
@since      11/3/2019
"""

# import environments to be used
import pandas as pd 
import datetime

# declaration of constant
LIST_OF_ISLANDS = ['Oahu', 'Hawaii Island', 'Maui', 'Sample']
LIST_OF_OAHU_SITES = ['Dole Plantation','Ko\'olau Center', 'Kapolei Commons', 'Hawai\'i Kai 7-Eleven', 'Ward 1', 'Ward 2', 'Wai\'anae Mall', '801 Dilingham'] 
LIST_OF_HAWAII_ISLAND_SITES = ['HELCO Hilo', 'HELCO Kona', 'Waimea KTA', 'The Shops at Mauna Lani']
LIST_OF_MAUI_SITES = ['MECO Kahului', 'Kaunakakai']
LIST_OF_SAMPLE_SITES = ['SiteA', 'SiteB']


class Site:
    def __init__(self, siteName):
        self.siteName = siteName

    def printSiteName(self):
        print('Analyzing site: ' + self.siteName)
    
    def gatherPowerData(self):
        # open file containing power data for site
        self.dataFrame = pd.read_excel(self.siteName + ' power.xlsx', sheet_name='Power Data')

        # adding values to an array 
        self.powerData = self.dataFrame.values.tolist()

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

    # Gather Power Data Site
    site = Site(siteName)
    site.printSiteName()

def createPowerTimeGraph():
    return

def createGraph():
    return

main()