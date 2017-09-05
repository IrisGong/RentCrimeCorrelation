__author__ = "Huangxuanyu Gong"

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

scale = StandardScaler()

## We need to find the cities that showed up in both files. 
# Read the cityCrimeList.csv
crimeCityTable = pd.read_csv('cityCrimeList.csv')
# Clean the data in crimeCityList['City']
crimeCityTable['City'] = crimeCityTable['City'].apply(lambda x: x.rstrip('*2'))
crimeCityTable['City'] = crimeCityTable['City'].apply(lambda x: x.replace('St.', 'Saint'))
crimeCityTable['City'] = crimeCityTable['City'].apply(lambda x: x.split('-')[0])
# Read the rent data. 
rentCityTable = pd.read_csv('City_Zri_AllHomesPlusMultifamily_Summary.csv') 
# We make two list to check the common cities in both files.
crimeCityList = []
for city in crimeCityTable['City']:
    crimeCityList.append(city)

rentCityList = []
for city in rentCityTable['RegionName']:
    rentCityList.append(city)

commonCityList = []
for city in crimeCityList:
    if city in rentCityList:
            commonCityList.append(city)

# Read the rent data. 
rentCityTable = pd.read_csv('City_Zri_AllHomesPlusMultifamily_Summary.csv')
# Make a violent crime dictionary base on the crimeCityTable. 
violentDict = {}
for city, vio in zip(crimeCityTable['City'], crimeCityTable['Violent Crime']):
    violentDict[city] = vio
# Make a property crime dictionary base on the crimeCityTable.
propertyDict = {}
for city, prop in zip(crimeCityTable['City'], crimeCityTable['Property Crime']):
    propertyDict[city] = prop
# Make a rent dicitonary base on the rentCityTable.
rentDict = {}
for city, rent in zip(rentCityTable['RegionName'], rentCityTable['Zri']):
    rentDict[city] = float(rent)

# Make a dictionary for violent crime per capita. 
vpSumDict = {i: violentDict[i] + propertyDict[i] for i in violentDict}


### Graphing part, we only use the data for rent <= 3000
## Violent crime and rent graph.
# Set x,y
X = []
vrY = []
for city in commonCityList:
    if rentDict[city] <= 3000:
        X.append(rentDict[city])
        vrY.append(violentDict[city])

vrGraph = plt.figure(1)
plt.xlabel("Rent of Cities")
plt.ylabel("Violent Crime Per Capita")
plt.title("Violent Crime AND Rent")
vrP4 = np.poly1d(np.polyfit(X, vrY, 1))
vrxp = np.linspace(500, 3000, 10000)
plt.plot(vrxp, vrP4(vrxp), c = 'r')
vrGraph.show()

## Property crime and rent graph. 
# Set y
prY = []
for city in commonCityList:
    if rentDict[city] <= 3000:
        prY.append(propertyDict[city])

prGraph = plt.figure(2)
plt.scatter(X, prY)
plt.xlabel("Rent of Cities")
plt.ylabel("Property Crime Per Capita")
plt.title("Property Crime AND Rent")
prP4 = np.poly1d(np.polyfit(X, prY, 1))
prxp = np.linspace(500, 3000, 10000)
plt.plot(prxp, prP4(prxp), c = 'r')
prGraph.show()

## Crime and rent graph. 
# Set y
crY = []
for city in commonCityList:
    if rentDict[city] <= 3000:
        crY.append(vpSumDict[city])


crGraph = plt.figure(3)
plt.scatter(X, crY)
plt.xlabel("Rent of Cities")
plt.ylabel("Crime Per Capita")
plt.title("Crime AND Rent")
crP4 = np.poly1d(np.polyfit(X, crY, 1))
crxp = np.linspace(500, 3000, 10000)
plt.plot(crxp, crP4(crxp), c = 'r')
crGraph.show()


# All the r2 scores for all the above graph
vrr2 = r2_score(vrY, vrP4(X))
print(vrr2)
prr2 = r2_score(prY, prP4(X))
print(prr2)
crr2 = r2_score(crY, crP4(X))
print(crr2)

input()

