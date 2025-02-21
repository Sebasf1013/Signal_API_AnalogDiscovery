import numpy as np
import matplotlib.pyplot as plt

# Definir parámetros de la señal
frecuencia = 1  # Frecuencia en Hz
amplitud = 1    # Amplitud de la onda
tiempo = np.linspace(0, 2, 1000)  # 2 segundos con 1000 puntos

# Crear la señal seno
onda_seno = amplitud * np.sin(2 * np.pi * frecuencia * tiempo)

# Graficar la señal
plt.figure(figsize=(8, 4))
plt.plot(tiempo, onda_seno, label="Onda Senoidal", color="b")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Gráfica de una Onda Senoidal")
plt.grid(True)
plt.legend()
plt.show()
