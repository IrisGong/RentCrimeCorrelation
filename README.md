# Rent Crime Correlation

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
##### Result:
1. The following three graphs are the results for Violent Crime and Rent, Property Crime and Rent and Fitting Polynomials for All Crimes and Rent. 
2. Blue points are the 79 American major cities from crime per capita file and rent per city file. 
3. Line graphs are the 1st, 3rd, 5th polynomials to fit the data. 
4. R-squared errors are computed as following: 

  * The r-squared error for 1st polynomial is: 0.165356016742
  * The r-squared error for 3rd polynomial is: 0.173871149373
  * The r-squared error for 5th polynomial is: 0.177996043172
  
##### Conclusion:
A clear downward relation showed among scatter graph points. However, by increasing 2 degrees of polynomial at one time, the r-squared error merely increased by 0.01, which implies it is difficult to find the best fitting polynomials. 

![Violent Crime and Rent](https://github.com/IrisGong/RentCrimeCorrelation/blob/master/Violent%20Crime%20AND%20Rent.png)
![Property Crime and Rent](https://github.com/IrisGong/RentCrimeCorrelation/blob/master/Property%20Crime%20AND%20Rent.png)
![Fitting Polynomials for All Crimes and Rent](https://github.com/IrisGong/RentCrimeCorrelation/blob/master/Fitting%20Polynomials%20for%20All%20Crimes%20and%20Rent.png)


