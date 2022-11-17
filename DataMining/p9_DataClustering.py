import pandas as pd
import seaborn as sns
import squarify as sq
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv ('C:/Users/Leslie Saucedo/Desktop/DataMining/Covid Cases and Vaccination.csv')

kmeans = KMeans(n_clusters=4)

kmeans.fit(df[["daily_vaccinations","daily_deaths"]])

kmeans.cluster_centers_

kmeans.labels_

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(10,6))
ax1.set_title('K Means')
ax1.scatter(df["daily_vaccinations"],df["daily_deaths"],c=kmeans.labels_,cmap='rainbow')

plt.savefig('Graphics/p9_DataClustering.png')