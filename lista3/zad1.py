import numpy as np
from scipy import stats

rozklad_mean = 50 
rozklad_std_dev = 5
n = 30  
alpha = 0.05 

np.random.seed(0)
próbka = np.random.normal(rozklad_mean, rozklad_std_dev, n)

próbka_mean = np.mean(próbka)
próbka_std_dev = np.std(próbka, ddof=1)

z_statystyka = (próbka_mean - rozklad_mean) / (próbka_std_dev / np.sqrt(n))

p_value = 2 * (1 - stats.norm.cdf(abs(z_statystyka)))

print(f"Średnia próbki: {próbka_mean:.2f}")
print(f"Z-statystyka: {z_statystyka:.2f}")
print(f"Wartość p: {p_value:.4f}")

if p_value < alpha:
    print("Odrzucamy hipotezę zerową: Średnia próbki jest istotnie różna od wartości referencyjnej.")
else:
    print("Nie odrzucamy hipotezy zerowej: Średnia próbki nie jest istotnie różna od wartości referencyjnej.")
