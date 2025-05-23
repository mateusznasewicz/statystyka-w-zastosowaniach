import numpy as np
from scipy import stats

# Funkcja do przeprowadzania testu t dla jednej próby
def test_t_jednej_proby(srednia_populacji, srednia_proby, rozrzut, liczebnosc):
    # Generowanie danych
    proba = np.random.normal(loc=srednia_proby, scale=rozrzut, size=liczebnosc)

    # Hipotezy:
    # H0: Średni wzrost w próbie = 170 cm
    # H1: Średni wzrost w próbie ≠ 170 cm

    # Test t-Studenta dla jednej próby
    t_stat, p_value = stats.ttest_1samp(proba, popmean=srednia_populacji)

    # Wyniki
    print(f"Średnia próbki: {np.mean(proba):.2f} cm")
    print(f"Statystyka t: {t_stat:.4f}")
    print(f"Wartość p: {p_value:.4f}")

    # Decyzja
    alpha = 0.05
    if p_value < alpha:
        print("Odrzucamy hipotezę zerową: średnia różni się istotnie od 170 cm.\n")
    else:
        print("Brak podstaw do odrzucenia hipotezy zerowej: średnia nie różni się istotnie od 170 cm.\n")

# Przypadek 1: średnia próbki = 170 (powinno nie być różnicy)
print("Przypadek 1: Średnia próbki = 170")
test_t_jednej_proby(srednia_populacji=170, srednia_proby=170, rozrzut=6, liczebnosc=30)

# Przypadek 2: średnia próbki = 172 (niewielka różnica)
print("Przypadek 2: Średnia próbki = 172")
test_t_jednej_proby(srednia_populacji=170, srednia_proby=172, rozrzut=6, liczebnosc=30)

# Przypadek 3: średnia próbki = 175 (większa różnica)
print("Przypadek 3: Średnia próbki = 175")
test_t_jednej_proby(srednia_populacji=170, srednia_proby=175, rozrzut=6, liczebnosc=30)
