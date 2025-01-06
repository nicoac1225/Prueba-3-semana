import pandas as pd
import matplotlib.pyplot as mp

# Cargar los datos desde el archivo CSV
df = pd.read_csv ('ventas_productos.csv')

print (df.head()) #Mostrar el archivo

# Calcular el precio total por producto
df ['Precio Total'] = df[ 'Cantidad'] * df['Precio']

print (df.head()) #Agrego columna de precio total