import pandas as pd
from tabulate import tabulate

from kaggle.api.kaggle_api_extended import KaggleApi
import os
api = KaggleApi()
api.authenticate()
#api.dataset_download_files('kunwarakash/covid-cases-and-vaccination-data', path='covid_cases__vaccination.csv', unzip=True)
#os.rename('Covid Cases and Vaccionation.csv', 'Covid Cases and Vaccination.csv')

df = pd.read_csv ('C:/Users/Leslie Saucedo/Desktop/DataMining/Covid Cases and Vaccination.csv')
print(df)