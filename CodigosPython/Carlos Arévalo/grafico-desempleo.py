# https://si3.bcentral.cl/indicadoressiete/secure/Serie.aspx?gcode=TAS_DES_INE&param=VwAuAEMAdgBMAC4AcgBkADgALQBoADIAZABfADAAMAAzADIAYQBWAGMANABIAFoAaQBUAEsANgA2AHQAOQBHAFMAQQBrAFkAJAAwAEsARgBnAEYAeQB1ADUAZgBFAFQATAAwADYAQgA0AF8ATwB0AGoAcgBVAGYASwAxAHMAOABFAGwAYwBMAHgAawBVAEsARgBlAGYAWQB1ADIANwA2AGYAVABkAGsAQQBOAEoAVQBNAEgAUwBGAHYAeABNAGEA  tasa de desempleo
import pandas as pd
import matplotlib.pyplot as plt


# Carga los datos
df = pd.read_excel('Tasa_de_desempleo.xls', skiprows=3)

# Convierte 'Mes' a datetime
df['Mes'] = pd.to_datetime(df['Mes'], format="%d-%m-%Y")

# Extrae el año y el número de mes
df['Año'] = df['Mes'].dt.year
# Calcular promedio anual de tasa de desempleo
promedios_anuales = df.groupby('Año')['Valor'].mean().reset_index()

# Crear gráfico lollipop
plt.figure(figsize=(12, 6))
plt.stem(
    promedios_anuales['Año'], 
    promedios_anuales['Valor'], 
    basefmt=" ", 
    linefmt="darkred", 
    markerfmt="o"
)
plt.plot(
    promedios_anuales['Año'], 
    promedios_anuales['Valor'], 
    'o', 
    color='darkred'
)

# Etiquetas y diseño
plt.title('Promedio Anual de Tasa de Desempleo en Chile', fontsize=14)
plt.xlabel('Año')
plt.ylabel('Tasa de Desempleo Promedio (%)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()