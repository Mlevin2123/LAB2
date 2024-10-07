import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Cargar el dataset Iris
iris = load_iris()

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Filtrar las columnas relevantes
species_mapping = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['species'] = df['species'].map(species_mapping)

# Calcular la longitud promedio de los pétalos por especie
promedio_petal_length = df.groupby('species')['petal length (cm)'].mean()

# Crear el gráfico de barras
especies = promedio_petal_length.index  # Las especies son los índices del grupo
longitud_promedio = promedio_petal_length.values  # Las longitudes promedio

plt.bar(especies, longitud_promedio, color=['skyblue', 'lightgreen', 'lightcoral'])
plt.xlabel('Especies')
plt.ylabel('Longitud Promedio del Pétalo (cm)')
plt.title('Longitud Promedio del Pétalo por Especie en el Iris Dataset')
plt.xticks(rotation=45)  # Rotar las etiquetas si es necesario
plt.show()
