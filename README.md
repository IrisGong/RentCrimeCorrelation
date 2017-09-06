# RentCrimeCorrelation

### Introduction
--------
We tend to believe the more expensive the rent price is, the safer the community is. This project tries to reveal the correlation between crime per capita and rent price for major American cities. 

### Data Sources:
--------
Data is taken from the following two websites:
1. Crime per capita: https://en.wikipedia.org/wiki/List_of_United_States_cities_by_crime_rate
2. Rent per city: https://www.zillow.com/research/data/

### Data Processing: 
--------
1. Extract City, Violent Crime and Property Crime columns from the crime per capita file, and RegionName and Zri columns from rent per city file. 
2. Match the cities from these two files to associate violent and property crime per calpita with rent price for each city. 
3. Use matlibplot library to make scatter plots for each crime type, and apply ployfit function to find the best fitting polynomials for the scatter plots. 

### Result and Conclusion:
--------
1. The following three graph are the results for Violent Crime and Rent, Property Crime and Rent, Crime and Rent. 
2. Blue points are the 79 American major cities from crime per capita file and rent per city file. 
3. Line graphs are the polynomial that 
![Violent Crime AND Rent](https://github.com/IrisGong/RentCrimeCorrelation/blob/master/Violent%20Crime%20AND%20Rent.png)
![Property Crime AND Rent](https://github.com/IrisGong/RentCrimeCorrelation/blob/master/Property%20Crime%20AND%20Rent.png)
![Crime AND Rent](https://github.com/IrisGong/RentCrimeCorrelation/blob/master/Crime%20AND%20Rent.png)