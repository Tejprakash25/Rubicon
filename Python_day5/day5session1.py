# Assesment task day 5

#Load a csv file into a Dataframe
import pandas as pd

df = pd.read_csv('/home/tezprakash/Downloads/WALMART.csv')
# print(df)

#Display first rows and last rows
# print(df.head())
# print(df.tail())

#Get summary statistics of the data
# print(df.describe())

# Check datatypes of each column
# print(df.info())

# Handle missing values
# print(df.isnull())
 
# Rename columns
print(df.rename(columns=""))