import pandas as pd
import seaborn as sns
import squarify as sq
import matplotlib.pyplot as plt


df = pd.read_csv ('C:/Users/Leslie Saucedo/Desktop/DataMining/Covid Cases and Vaccination.csv')

# Gráfica de porcentaje de muertes por país
'''
total_muertes = df['daily_deaths'].sum()

paises = df['country'].unique()

muertes_por_pais = []
for pais in paises:
    muertes_por_pais.append(df[df['country'] == pais]['daily_deaths'].sum()/total_muertes)

temp = pd.DataFrame({'Pais':paises, 'Muertes':muertes_por_pais})
temp = temp.sort_values('Muertes').tail(10)
temp = temp.append({'Pais':'Others', 'Muertes':(1-temp['Muertes'].sum())}, ignore_index=True)

paises = temp['Pais']
muertes_por_pais = temp['Muertes']

fig1, ax1 = plt.subplots()
ax1.pie(muertes_por_pais, labels=paises, autopct='%1.1f%%')
ax1.axis('equal')
plt.title('Porcentaje de muertes por pais')
plt.savefig('Graphics/p4_DataVisualization_Porcentaje de muertes por pais.png')
'''

# Gráfica de barras de vacunados por país
'''
total_vacunados = df['daily_vaccinations'].sum()

paises = df['country'].unique()

vacunados_por_pais = []

for pais in paises:
    vacunados_por_pais.append(df[df['country'] == pais]['daily_vaccinations'].sum()/total_vacunados)

temp = pd.DataFrame({'Pais':paises, 'Vacunados':vacunados_por_pais})
temp = temp.sort_values('Vacunados').tail(10)
temp = temp.append({'Pais':'Others', 'Vacunados':(1-temp['Vacunados'].sum())}, ignore_index=True)

paises = temp['Pais']
vacunados_por_pais = temp['Vacunados']

fig1, ax1 = plt.subplots()
ax1.bar(paises, vacunados_por_pais)
plt.title('Porcentaje de vacunados por pais')
plt.ylabel('Porcentaje de vacunados')
plt.xticks(rotation=90)
plt.savefig('Graphics/p4_DataVisualization_Porcentaje de vacunados por pais.png')
'''

# Gráfica de casos diarios por país
'''
total_casos = df['daily_cases'].sum()

paises = df['country'].unique()

casos_por_pais = []

for pais in paises:
    casos_por_pais.append(df[df['country'] == pais]['daily_cases'].sum()/total_casos)

temp = pd.DataFrame({'Pais':paises, 'Casos':casos_por_pais})
temp = temp.sort_values('Casos').tail(10)
temp = temp.append({'Pais':'Others', 'Casos':(1-temp['Casos'].sum())}, ignore_index=True)

paises = temp['Pais']
casos_por_pais = temp['Casos']

fig1, ax1 = plt.subplots()
ax1.bar(paises, casos_por_pais)
plt.title('Porcentaje de casos por pais')
plt.ylabel('Porcentaje de casos')
plt.xticks(rotation=90)
plt.savefig('Graphics/p4_DataVisualization_Porcentaje de casos por pais.png')
'''