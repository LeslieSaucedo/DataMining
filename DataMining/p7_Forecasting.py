import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
from tabulate import tabulate
from statsmodels.stats.outliers_influence import summary_table
from typing import Tuple, Dict
import numpy as np

df = pd.read_csv ('C:/Users/Leslie Saucedo/Desktop/DataMining/Covid Cases and Vaccination.csv')



def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))

def transform_variable(df: pd.DataFrame, x:str)->pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x] # type: pd.Series
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def linear_regression(df: pd.DataFrame, x:str, y: str)->Dict[str, float]:
    fixed_x = transform_variable(df, x)
    model= sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    bands = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]
    print_tabulate(pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0])
    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    r_2_t = pd.read_html(model.summary().tables[0].as_html(),header=None,index_col=None)[0]
    return {'m': coef.values[1], 'b': coef.values[0], 'r2': r_2_t.values[0][3], 'r2_adj': r_2_t.values[1][3], 'low_band': bands['[0.025'][0], 'hi_band': bands['0.975]'][0]}

def plt_lr(df: pd.DataFrame, x:str, y: str, m: float, b: float, r2: float, r2_adj: float, low_band: float, hi_band: float, colors: Tuple[str,str]):
    fixed_x = transform_variable(df, x)
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[ m * x + b for _, x in fixed_x.items()], color=colors[0])
    plt.fill_between(df[x],
                     [ m * x  + low_band for _, x in fixed_x.items()],
                     [ m * x + hi_band for _, x in fixed_x.items()], alpha=0.2, color=colors[1])


# list from numbers from 1 to 930
x = [i for i in range(1, 931)]


# list of daily deaths where country is mexico
y = df[df["country"] == "mexico"]["daily_deaths"].tolist()

df = pd.DataFrame({'daily_vaccinations': x, 'daily_deaths': y})

#print_tabulate(df_by_sal.head(5))
a = linear_regression(df, "daily_vaccinations", "daily_deaths")
plt_lr(df=df, x="daily_vaccinations", y="daily_deaths", colors=('red', 'orange'), **a)

plt.xticks(rotation=90)
# plt.savefig('Graphics/p7_Forecasting.png')
plt.close()