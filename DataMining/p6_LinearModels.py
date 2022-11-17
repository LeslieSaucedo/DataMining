import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
import numbers

df = pd.read_csv ('C:/Users/Leslie Saucedo/Desktop/DataMining/Covid Cases and Vaccination.csv')

# sns.pairplot(df,diag_kind='hist',diag_kws={"bins":10})

# list of daily vaccinations where country is mexico
# x = df[df["country"] == "mexico"]["daily_vaccinations"].tolist()

# list from numbers from 1 to 930
x = [i for i in range(1, 931)]


# list of daily deaths where country is mexico
y = df[df["country"] == "mexico"]["daily_deaths"].tolist()

# first date with daily vaccinations bigger than zero where country equals mexico
first_date = df[df["country"] == "mexico"][df["daily_vaccinations"] > 0].iloc[0]["date"]

print(first_date)


# # print count of list x
# print(len(x))

# # print count of list y
# print(len(y))

def transform_variable(df: pd.DataFrame, x:str)->pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x] # type: pd.Series
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def linear_regression(df: pd.DataFrame, x:str, y: str)->None:
    fixed_x = transform_variable(df, x)
    model= sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    print(model.summary())

    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[pd.DataFrame.mean(df[y]) for _ in fixed_x.items()], color='green')
    plt.plot(df[x],[ coef.values[1] * x + coef.values[0] for _, x in fixed_x.items()], color='red')
    plt.xticks(rotation=90)
    plt.show()
    # plt.savefig('Graphics/p6_LinearModels.png')

df = pd.DataFrame({'daily_vaccinations': x, 'daily_deaths': y})
linear_regression(df, 'daily_vaccinations', 'daily_deaths')

print(x)


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

# from sklearn.linear_model import LinearRegression

# lm = LinearRegression()

# lm.fit(X_train,y_train)

# # print the coeficients
# print(lm.coef_)

# # print the intercept
# print(lm.intercept_)

# coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['daily_deaths'])
# coeff_df

# predictions = lm.predict(X_test)

# plt.scatter(y_test,predictions)

# plt.savefig('Graphics/p6_LinearModels.png')



# fechas = df['date'].unique()

# for fecha in fechas:
#     muertes = df[df['date']==fecha]['daily_deaths'].sum()

# df = pd.DataFrame({'date':fechas, 'daily_deaths':muertes})




