import pandas as pd
from tabulate import tabulate

df = pd.read_csv ('C:/Users/Leslie Saucedo/Desktop/DataMining/Covid Cases and Vaccination.csv')
print(df)

df = df[(df['country'] == 'mexico') | (df['country'] == 'germany')]
print(df)