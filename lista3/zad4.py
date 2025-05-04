import numpy as np
from scipy import stats


obserwowane = np.array([50, 30, 10, 10])
oczekiwane = np.array([25, 25, 25, 25]) 

chi2_stat, p_value = stats.chisquare(obserwowane, oczekiwane)

# Wyniki
print(f"Chi-kwadrat: {chi2_stat:.2f}")
print(f"Wartość p: {p_value:.4f}")

# Interpretacja wyniku
alpha = 0.05
if p_value < alpha:
    print("Odrzucamy hipotezę zerową: Obserwowany rozkład różni się istotnie od oczekiwanego.")
else:
    print("Nie odrzucamy hipotezy zerowej: Obserwowany rozkład nie różni się istotnie od oczekiwanego.")
