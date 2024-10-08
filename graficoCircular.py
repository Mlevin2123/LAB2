import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
dataset = pd.read_csv('vgsales.csv')

# Agrupar por plataforma y sumar las ventas globales
ventas_por_plataforma = dataset.groupby('Platform')['Global_Sales'].sum()

# Seleccionar solo las 2 plataformas más vendidas
plataformas_seleccionadas = ventas_por_plataforma.nlargest(2).index.tolist()
ventas_seleccionadas = ventas_por_plataforma[plataformas_seleccionadas]

# Agrupar las demás plataformas como 'Otras'
otras_ventas = ventas_por_plataforma.drop(plataformas_seleccionadas).sum()
ventas_seleccionadas['Otras'] = otras_ventas

# Crear el gráfico circular
plt.figure(figsize=(12, 12))  # Aumentar el tamaño del gráfico
plt.pie(ventas_seleccionadas, autopct='%1.1f%%', startangle=140)

# Añadir leyenda
plt.legend(ventas_seleccionadas.index, loc="best")

# Título del gráfico
plt.title('Porcentaje de ventas por plataforma (Global)', fontsize=16)

# Mostrar el gráfico
plt.show()
