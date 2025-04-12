# https://www.ine.gob.cl/estadisticas/economia/indices-de-precio-e-inflacion/indice-de-precios-al-consumidor esta es del ipc


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

#leemos los datos del archivo del excel
df = pd.read_excel('IPC.xlsx', skiprows=3)
print(df.columns)
df=df[df['Año']!=2009]
tabla = df.pivot(index='Año', columns='Mes', values='Índice')
# Asegurarnos de que las columnas (meses) estén ordenadas
tabla = tabla.sort_index(axis=1)

# Opcional: reemplazar número por nombre de mes
nombres_meses = {
    1: 'Ene', 2: 'Feb', 3: 'Mar', 4: 'Abr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Ago', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dic'
}
tabla.columns = [nombres_meses[m] for m in tabla.columns]
# Graficar heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(tabla, annot=True, cmap="Reds", fmt=".2f", linewidths=.5)
plt.title("Evolución Mensual del Índice de Precios al Consumidor (IPC) en Chile")
plt.xlabel("Mes")
plt.ylabel("Año")
plt.tight_layout()
plt.show()
