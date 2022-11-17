from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import AgglomerativeClustering
from matplotlib import pyplot
import pandas as pd
import tabulate as tb
from typing import Tuple, Dict, List
from functools import reduce
import matplotlib.pyplot as plt
from scipy.stats import mode
from sklearn.svm import SVC
from copy import deepcopy
from sklearn.cluster import KMeans

df = pd.read_csv ('C:/Users/Leslie Saucedo/Desktop/DataMining/Covid Cases and Vaccination.csv')


# df_imp=df[['Lattitude','Longtitude']]
# from sklearn import preprocessing

# x = df_imp #regresa un numpy array
# min_max_scaler = preprocessing.MinMaxScaler()
# x_scaled = min_max_scaler.fit_transform(x)
# df = pd.DataFrame(x_scaled)
# df.head()

# def Kmeans(df: pd.DataFrame(), n: int):
#     kmeans = KMeans(n_clusters=n, random_state=0).fit(df)
#     labels = kmeans.labels_
#     #Pegar de nuevo a los datos originales
#     df['clusters'] = labels
#     df2 = df.rename(columns = {0 : 'Lattitude', 1: 'Longtitude'})
#     #Agregar la columna a nuestra lista
#     return df2

# import seaborn as sns
# k=3;
# sns.lmplot('Lattitude', 'Longtitude', data = Kmeans(df, k), fit_reg=False,hue="clusters",  scatter_kws={"marker": "D", "s": 100})
# plt.title('Latitude v/s Longitude')
# plt.xlabel('Latitude')
# plt.ylabel('Longitude')
# plt.savefig(f'Clustering/cluster_{k}_Latitude_Longitude.png')
# plt.show()


def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))

def generate_df(means: List[Tuple[float, float, str]], n: int) -> pd.DataFrame:
    lists = [
        (df["daily_vaccinations"], df["daily_deaths"], df["country"])
        for _x, _y, _l in means
    ]
    x = df.array([])
    y = df.array([])
    labels = df.array([])
    for _x, _y, _l in lists:
        x = df.concatenate((x, _x), axis=None)
        y = df.concatenate((y, _y))
        labels = df.concatenate((labels, _l))
    return pd.DataFrame({"x": x, "y": y, "label": labels})

def get_cmap(n, name="hsv"):
    return plt.cm.get_cmap(name, n)

def scatter_group_by(
    file_path: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str
):
    fig, ax = plt.subplots(figsize=(25,10))
    labels = pd.unique(df[label_column])
    cmap = get_cmap(len(labels) + 1)
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i))
    ax.legend()
    plt.savefig(file_path)
    plt.close()

groups = [(20, 20, "grupo1"), (80, 40, "grupo2"), (200, 200, "grupo3")]
df = generate_df(groups, 100)
filtro = df['x'] < 400000
df = df[filtro]
scatter_group_by("graficas/groups.png", df, "x", "y", "label")