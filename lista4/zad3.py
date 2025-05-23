import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# Przykładowe dane: liczba osób w każdej kategorii (płeć vs. gatunek muzyki)
# Wiersze: Płeć (Kobieta, Mężczyzna)
# Kolumny: Gatunek muzyki (Pop, Rock, Klasyczna)

dane = np.array([
    [20, 15, 5],  # Kobiety
    [10, 25, 5]   # Mężczyźni
])

# Tworzenie tabeli kontyngencji
tabela = pd.DataFrame(dane, 
                      index=['Kobieta', 'Mężczyzna'],
                      columns=['Pop', 'Rock', 'Klasyczna'])

print("Tabela kontyngencji:")
print(tabela)

# Test chi-kwadrat niezależności
chi2_stat, p_value, dof, expected = chi2_contingency(tabela)

# Wyniki testu
print(f"\nStatystyka chi-kwadrat: {chi2_stat:.4f}")
print(f"Wartość p: {p_value:.4f}")
print(f"Liczba stopni swobody: {dof}")
print("\nOczekiwane wartości:")
print(pd.DataFrame(expected, index=tabela.index, columns=tabela.columns))

# Decyzja
alpha = 0.05
if p_value < alpha:
    print("\nOdrzucamy hipotezę zerową: istnieje istotna zależność między płcią a preferowanym gatunkiem muzyki.")
else:
    print("\nBrak podstaw do odrzucenia hipotezy zerowej: brak istotnej zależności między płcią a preferowanym gatunkiem muzyki.")
