import pandas as pd
from tabulate import tabulate

df = pd.read_csv ('C:/Users/Leslie Saucedo/Desktop/DataMining/Covid Cases and Vaccination.csv')

# Sumatoria de muertes en todo el mundo
print('Total de muertes: ',df['daily_deaths'].sum())

# Cantidad de países
print('Cantidad de paises en el dataframe: ',df['country'].nunique())

# País con más muertes
paises = df['country'].unique()
total = []
for pais in paises:
    total.append(df[df['country']==pais]['daily_deaths'].sum())

temp = pd.DataFrame({'country':paises, 'total_deaths':total})
print('Pais con mas muertes en total: ',temp.iloc[temp['total_deaths'].idxmax()]['country'],':',max(total))	

# Sumatoria de muertes de México y Alemania
df = df[(df['country'] == 'mexico') | (df['country'] == 'germany')]
print('Total de muertes en Alemania y Mexico: ',df['daily_deaths'].sum())

# Promedio de muertes diarias en todo el mundo
print('Promedio de muertes por dia: ',df['daily_deaths'].sum() / df['daily_deaths'].count())

# Día con más muertes
print('Dia con mas muertes: ',df['daily_deaths'].max())