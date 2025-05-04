import numpy as np
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

np.random.seed(0)

grupa1 = np.random.normal(loc=50, scale=5, size=30)
grupa2 = np.random.normal(loc=55, scale=5, size=30)
grupa3 = np.random.normal(loc=60, scale=5, size=30)

f_stat, p_value = stats.f_oneway(grupa1, grupa2, grupa3)

print(f"Statystyka F: {f_stat:.2f}")
print(f"Wartość p: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Odrzucamy hipotezę zerową: Istnieje istotna różnica między średnimi grup.")
    
    data = np.concatenate([grupa1, grupa2, grupa3])
    grupy = ['Grupa 1'] * len(grupa1) + ['Grupa 2'] * len(grupa2) + ['Grupa 3'] * len(grupa3)
    
    tukey = pairwise_tukeyhsd(data, grupy, alpha=0.05)
    print("\nWyniki testu Tukeya:")
    print(tukey)
    
else:
    print("Nie odrzucamy hipotezy zerowej: Brak istotnej różnicy między średnimi grup.")
