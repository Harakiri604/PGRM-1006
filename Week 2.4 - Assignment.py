'''
Import the relevant dataset and pandas
'''

import pandas as pd
df = pd.read_csv("life_expectancy_years.csv", index_col='country')

'''
TASK 1 - ROWS AND COLUMNS
TASK 2 - YEARS
Printing columns and rows(index) tells us that there are 219 columns and 187 
rows. It also tells us that the data spans 1800-2018.
'''

print(df.columns)
print(df.index)

'''
TASK 3 - SUMMARY STATS
Running summary stats tells us that the mean, std, min, max, and quartiles for
the first and final year of the dataset.
'''

print(df.describe())

'''
TASK 4 - MIN AND MAX FOR SA
Creating a variable "SA", then populating it with data from the South Africa
row and running a summary stat tells us the mi (11.5) and max (65.0) for the country. 
'''

SA=df.loc['South Africa']
print(SA.describe())

'''
TASK 5 - YEARS OF MIN AND MAX FOR SA
Creating a filter based on the known min and max values and then printing a
filtered version of the row tells us that 1918 and 1993 are min and max years.

'''

maxSA=df.loc['South Africa'] == 11.5
maxFilSA=df.loc['South Africa'][maxSA]
print(maxFilSA)

minSA=df.loc['South Africa'] == 65.0
minFilSA=df.loc['South Africa'][minSA]
print(minFilSA)

'''
TASK 6 - MIN AND MAX COUNTRIES IN 2018
Creating variables based on idxmax and idxmin for 2018 tells us that Japan and
Lesotho were the max and min countries in that year. 
'''

maxCountry=df['2018'].idxmax()
minCountry=df['2018'].idxmin()
print(maxCountry)
print(minCountry)

'''
TASK 7 - COUNTRIES WITH >50 IN 1800
TASK 8 - COUNTRIES WITH >50 IN 2018
Same approach as task 5, i.e. using a mask. No results for 1800 and 184 in 2018
'''

over1800=df['1800'] > 50.0
over1800Fil=df['1800'][over1800]
print(over1800Fil) 

over2018=df['2018'] > 50.0
over2018Fil=df['2018'][over2018]
print(over2018Fil) 

'''
TASK 9 - UNITED STATES vs. GERMANY
Dips on graphs show - US Civil War in 1861-1865 (US), WWI in 1914-1918 (Germany),
Influenza Epidemic in 1918 (US and Germany), and WWII in 1939-1945 (Germany)
'''

df.loc[['United States','Germany']].T.plot()
