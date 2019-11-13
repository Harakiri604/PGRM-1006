import pandas as pd

df = pd.read_csv("co2_emissions_tonnes_per_person.csv", index_col='country')

print(df.head(10))
print(df.describe())
print(df.columns)
print(df.index)

#Creating a list by columns
year19and20 = df[['1900', '2000']]
print(year19and20)

#Creating a list by rows
canadaAndchina = df.loc[['Canada','China']]
print(canadaAndchina)

#practice
india = df.loc['India']
print(india)

#Max/min etc
someMax = df[['1900','2000']].max()
print(someMax)

#Max of which country
maxCountry = df[['1950','1970','2014']].idxmax()
print(maxCountry)

#Add booleans
conditionals = df['2000'] > 10
print(conditionals)

#Booleans by row
conditionalsRow = df.loc['China'] > 6
print(conditionalsRow)

filtered = df['2000'][conditionals]
print(filtered)

#Plotting
df.loc['Canada'].plot()
df.loc['China'].plot()

#Plotting multiple
df.loc[['Canada','China','Russia', 'Mongolia']].T.plot()

#Sorting by specific column's values
df = df.sort_values(by='2014', ascending=False).head()
print(df.head())

