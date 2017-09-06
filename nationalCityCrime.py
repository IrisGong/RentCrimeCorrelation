__author__ = "Huangxuanyu Gong"

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

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
plt.scatter(X, vrY)
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
crP1 = np.poly1d(np.polyfit(X, crY, 1))
crP3 = np.poly1d(np.polyfit(X, crY, 3))
crP5 = np.poly1d(np.polyfit(X, crY, 5))
crxp = np.linspace(500, 3000, 10000)
plt.plot(crxp, crP1(crxp), c = 'r')
plt.plot(crxp, crP3(crxp), c = 'k')
plt.plot(crxp, crP5(crxp), c = 'g')
plt.legend(['1st Poly', '3rd Poly', '5th Poly'], loc = 1)
crGraph.show()


# All the r2 scores for all the above graph
print("The r-squared error for 1st polynomial is: " + str(r2_score(crY, crP1(X))))
print("The r-squared error for 3rd polynomial is: " + str(r2_score(crY, crP3(X))))
print("The r-squared error for 5th polynomial is: " + str(r2_score(crY, crP5(X))))


input()

