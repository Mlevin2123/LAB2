import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('worldPopulationByCountries2020.csv')
data = {
    'Country': ['China', 'China', 'China', 'India', 'India', 'India', 'USA', 'USA', 'USA'],
    'Year': [1960, 1990, 2020, 1960, 1990, 2020, 1960, 1990, 2020],
    'Population': [667070000, 1143335000, 1402112000, 450547679, 873277798, 1380004385, 180671000, 248709873, 331002651]
}    #datos de poblacion ficticios

# Convertir el diccionario en un DataFrame de pandas
df = pd.DataFrame(data)

# Filtrar datos de los países de interés
countries = ['China', 'India', 'USA']
df_filtered = df[df['Country'].isin(countries)]

# Crear el gráfico de línea
plt.figure(figsize=(10,6))

for country in countries:
    country_data = df_filtered[df_filtered['Country'] == country]
    plt.plot(country_data['Year'], country_data['Population'], marker='o', label=country)

# Personalización del gráfico
plt.title('Evolución de la Población (1960 - 2020)')
plt.xlabel('Año')
plt.ylabel('Población')
plt.legend(title="País")
plt.grid(True)

# Mostrar el gráfico
plt.show()

#link del datasets: https://www.kaggle.com/datasets/themlphdstudent/world-population-by-countries-2020