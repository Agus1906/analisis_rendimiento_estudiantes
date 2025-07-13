# 📊 Análisis de Rendimiento de Estudiantes
# 👩‍💻 Autor: Agustina Irisarri
# 📁 Proyecto: Analisis_rendimiento_estudiantes

# 📥 Importar librerías
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ✅ Configuración para mostrar gráficos dentro de VS Code Interactive Window
%matplotlib inline
sns.set(style="whitegrid")

# 📂 Cargar el dataset
data = pd.read_csv('data/students_performance.csv')

# 🔍 Mostrar las primeras filas
print("📌 Primeras filas del dataset:")
display(data.head())

# ℹ️ Información general del dataset
print("\nℹ️ Información del dataset:")
display(data.info())

# 📊 Estadísticas descriptivas
print("\n📊 Estadísticas descriptivas:")
display(data.describe())

# 📈 Visualización: Distribución de puntajes en matemática
plt.figure(figsize=(10,6))
sns.histplot(data['math_score'], bins=20, kde=True, color='blue')
plt.title('Distribución de Puntajes en Matemáticas')
plt.xlabel('Puntaje')
plt.ylabel('Cantidad de Estudiantes')
plt.show()

# 📦 Visualización: Boxplot de puntajes por género
plt.figure(figsize=(8,6))
sns.boxplot(x='gender', y='math_score', data=data, palette='Set2')
plt.title('Puntajes en Matemáticas por Género')
plt.xlabel('Género')
plt.ylabel('Puntaje en Matemáticas')
plt.show()

# 🔗 Relación entre lectura y escritura
plt.figure(figsize=(8,6))
sns.scatterplot(x='reading_score', y='writing_score', hue='gender', data=data)
plt.title('Relación entre Puntajes de Lectura y Escritura')
plt.xlabel('Puntaje de Lectura')
plt.ylabel('Puntaje de Escritura')
plt.legend(title='Género')
plt.show()

