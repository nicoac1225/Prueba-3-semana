import pandas as pd
import matplotlib.pyplot as mp

# Cargar los datos desde el archivo CSV
df = pd.read_csv ('ventas_productos.csv')

print (df.head()) #Mostrar el archivo

# Calcular el precio total por producto
df ['Precio Total'] = df[ 'Cantidad'] * df['Precio']

print (df.head()) #Agrego columna de precio total

#Crear un gráfico de barras para visualizar el precio total por producto
plt.bar (df ['Producto'], df['Precio'])
plt. xlabel ('Producto')
plt.ylabel ('Precio Total')
plt.title ('Precio Total por Producto')
plt. savefig ('grafico_precios.png') # Guardar el gráfico como PNG
plt. show ()
