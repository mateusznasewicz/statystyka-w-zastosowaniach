import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu
import matplotlib.pyplot as plt

# Ustawienie ziarna losowości
np.random.seed(0)

# Generowanie danych z rozkładu wykładniczego
grupa1 = np.random.exponential(scale=1.0, size=30)
grupa2 = np.random.exponential(scale=1.5, size=30)  # Inna skala => inna mediana/średnia

# Wizualizacja rozkładów (opcjonalnie)
plt.hist(grupa1, bins=15, alpha=0.6, label='Grupa 1', color='skyblue')
plt.hist(grupa2, bins=15, alpha=0.6, label='Grupa 2', color='salmon')
plt.title('Histogram danych (rozkład wykładniczy)')
plt.xlabel('Wartość')
plt.ylabel('Liczebność')
plt.legend()
plt.show()

# Test parametryczny: test t-Studenta
t_stat, p_t = ttest_ind(grupa1, grupa2)
print(f"Test t-Studenta: statystyka t = {t_stat:.4f}, p = {p_t:.4f}")

# Test nieparametryczny: test Manna-Whitneya
u_stat, p_u = mannwhitneyu(grupa1, grupa2, alternative='two-sided')
print(f"Test Manna-Whitneya: statystyka U = {u_stat:.4f}, p = {p_u:.4f}")

# Wniosek ogólny
print("\nPorównanie testów:")
if p_t < 0.05:
    print("- Test t: różnica ISTOTNA statystycznie.")
else:
    print("- Test t: brak istotnej różnicy.")

if p_u < 0.05:
    print("- Test Manna-Whitneya: różnica ISTOTNA statystycznie.")
else:
    print("- Test Manna-Whitneya: brak istotnej różnicy.")
