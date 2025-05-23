import numpy as np
from scipy import stats

np.random.seed(42)

# Załóżmy, że średni wzrost kobiet to 165 cm (SD=7), a mężczyzn to 175 cm (SD=7)
kobiety = np.random.normal(loc=165, scale=7, size=30)
mezczyzni = np.random.normal(loc=175, scale=7, size=30)

# Sformułowanie hipotez:
# H0: Średni wzrost kobiet i mężczyzn jest taki sam
# H1: Średni wzrost kobiet i mężczyzn różni się

# Test t-Studenta dla dwóch niezależnych prób
t_stat, p_value = stats.ttest_ind(kobiety, mezczyzni)

# Wynik testu
print(f"Statystyka t: {t_stat:.4f}")
print(f"Wartość p: {p_value:.4f}")

# Poziom istotności
alpha = 0.05

# Decyzja
if p_value < alpha:
    print("Odrzucamy hipotezę zerową: średni wzrost różni się istotnie statystycznie.")
else:
    print("Brak podstaw do odrzucenia hipotezy zerowej: średni wzrost nie różni się istotnie statystycznie.")
