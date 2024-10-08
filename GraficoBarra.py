import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset 
df = pd.read_csv('netflix_titles.csv')

df_clean = df.dropna(subset=['release_year', 'type'])

# Filtrar solo los títulos de los últimos 10 años
df_filtered = df_clean[df_clean['release_year'] >= 2013]

# Contar el número de películas y series por año
titles_per_year = df_filtered.groupby(['release_year', 'type']).size().unstack(fill_value=0)

# Configura el tamaño del gráfico
plt.figure(figsize=(10, 6))

# Crear el gráfico de barras apiladas
titles_per_year.plot(kind='bar', stacked=True, color=['#FF9999', '#66B2FF'], width=0.7)


plt.title('Películas y Series en Netflix (últimos 10 años)', fontsize=18)
plt.xlabel('Año de Lanzamiento', fontsize=14)
plt.ylabel('Cantidad de Títulos', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.legend(title='Tipo', labels=['Película', 'Serie de TV'], fontsize=12)
plt.tight_layout()
# Mostrar el gráfico
plt.show()
