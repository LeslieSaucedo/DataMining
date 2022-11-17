import pandas as pd
import seaborn as sns
import squarify as sq
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv ('C:/Users/Leslie Saucedo/Desktop/DataMining/Covid Cases and Vaccination.csv')


def anova(df_aux: pd.DataFrame, str_ols: str):
    modl = ols(str_ols, data=df_aux).fit()
    anova_df = sm.stats.anova_lm(modl, typ=2)
    
    if anova_df["PR(>F)"][0] < 0.005:
        print("hay diferencias")
        print(anova_df)
    else:
        print("No hay diferencias")

def anova_1(df_complete: pd.DataFrame):
    df_by_type = df_complete.groupby(["country", 
                                      "date"])[["total_deaths"]].aggregate(pd.DataFrame.sum)
    df_by_type.reset_index(inplace=True)
    df_by_type.set_index("date", inplace=True)
    df_by_type.reset_index(inplace=True)
    
    
    df_aux = df_by_type.rename(columns={"total_deaths": "Total_Defunciones"}).drop(['date'], axis=1)
    print(df_aux.head())
    anova(df_aux, "Total_Defunciones ~ country")
    

#ANOVA
anova_1(df)