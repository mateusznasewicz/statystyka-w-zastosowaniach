import numpy as np
import seaborn as sns
from scipy import stats

iris = sns.load_dataset('iris')
dane = iris['sepal_length']

print(f"dane: {dane}")
shapiro_stat, shapiro_p_value = stats.shapiro(dane)
print(f"Test Shapiro-Wilka: Statystyka = {shapiro_stat:.4f}, Wartość p = {shapiro_p_value:.4f}")

ks_stat, ks_p_value = stats.kstest(dane, 'norm', args=(np.mean(dane), np.std(dane)))
print(f"Test Kołmogorowa-Smirnowa: Statystyka = {ks_stat:.4f}, Wartość p = {ks_p_value:.4f}")

alpha = 0.05
if shapiro_p_value < alpha:
    print("Odrzucamy hipotezę zerową testu Shapiro-Wilka: Dane nie pochodzą z rozkładu normalnego.")
else:
    print("Nie odrzucamy hipotezy zerowej testu Shapiro-Wilka: Dane pochodzą z rozkładu normalnego.")

if ks_p_value < alpha:
    print("Odrzucamy hipotezę zerową testu Kołmogorowa-Smirnowa: Dane nie pochodzą z rozkładu normalnego.")
else:
    print("Nie odrzucamy hipotezy zerowej testu Kołmogorowa-Smirnowa: Dane pochodzą z rozkładu normalnego.")
