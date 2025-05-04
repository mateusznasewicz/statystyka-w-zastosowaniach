import numpy as np
from scipy import stats

pop_mean = 50  
n = 30  
alpha = 0.05  

np.random.seed(0)  
próbka = np.random.normal(loc=49, scale=5, size=n)

próbka_mean = np.mean(próbka)
próbka_std_dev = np.std(próbka, ddof=1)  

t_statystyka, p_value = stats.ttest_1samp(próbka, pop_mean)

print(f"Średnia próbki: {próbka_mean:.2f}")
print(f"Odchylenie standardowe próbki: {próbka_std_dev:.2f}")
print(f"t-statystyka: {t_statystyka:.2f}")
print(f"Wartość p: {p_value:.4f}")

if p_value < alpha:
    print("Odrzucamy hipotezę zerową: Średnia próbki różni się istotnie od wartości referencyjnej.")
else:
    print("Nie odrzucamy hipotezy zerowej: Średnia próbki nie różni się istotnie od wartości referencyjnej.")
