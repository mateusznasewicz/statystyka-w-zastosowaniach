import numpy as np
from scipy import stats

pop_mean_1 = 50
pop_mean_2 = 55
std_dev_1 = 5
std_dev_2 = 5
n1 = 30
n2 = 30
alpha = 0.05

np.random.seed(0)
próbka_1 = np.random.normal(loc=pop_mean_1, scale=std_dev_1, size=n1)
próbka_2 = np.random.normal(loc=pop_mean_2, scale=std_dev_2, size=n2)

mean_1 = np.mean(próbka_1)
mean_2 = np.mean(próbka_2)
std_dev_1 = np.std(próbka_1, ddof=1)
std_dev_2 = np.std(próbka_2, ddof=1)

t_statystyka, p_value = stats.ttest_ind(próbka_1, próbka_2)

print(f"Średnia pierwszej próbki: {mean_1:.2f}")
print(f"Średnia drugiej próbki: {mean_2:.2f}")
print(f"t-statystyka: {t_statystyka:.2f}")
print(f"Wartość p: {p_value:.4f}")

if p_value < alpha:
    print("Odrzucamy hipotezę zerową: Średnie próbki różnią się istotnie.")
else:
    print("Nie odrzucamy hipotezy zerowej: Średnie próbki nie różnią się istotnie.")
