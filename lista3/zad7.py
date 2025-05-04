import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(42)

x_skorelowane = np.random.normal(0, 1, 100)
y_skorelowane = 2 * x_skorelowane + np.random.normal(0, 0.5, 100)

x_nieskorelowane = np.random.normal(0, 1, 100)
y_nieskorelowane = np.random.normal(0, 1, 100)

pearson_corr_skorelowane, pearson_p_value_skorelowane = stats.pearsonr(x_skorelowane, y_skorelowane)
spearman_corr_skorelowane, spearman_p_value_skorelowane = stats.spearmanr(x_skorelowane, y_skorelowane)

pearson_corr_nieskorelowane, pearson_p_value_nieskorelowane = stats.pearsonr(x_nieskorelowane, y_nieskorelowane)
spearman_corr_nieskorelowane, spearman_p_value_nieskorelowane = stats.spearmanr(x_nieskorelowane, y_nieskorelowane)

print("Dane skorelowane:")
print(f"Współczynnik korelacji Pearsona: {pearson_corr_skorelowane:.4f}, p-value: {pearson_p_value_skorelowane:.4f}")
print(f"Współczynnik korelacji Spearmana: {spearman_corr_skorelowane:.4f}, p-value: {spearman_p_value_skorelowane:.4f}")

print("\nDane nieskorelowane:")
print(f"Współczynnik korelacji Pearsona: {pearson_corr_nieskorelowane:.4f}, p-value: {pearson_p_value_nieskorelowane:.4f}")
print(f"Współczynnik korelacji Spearmana: {spearman_corr_nieskorelowane:.4f}, p-value: {spearman_p_value_nieskorelowane:.4f}")

alpha = 0.05

print("\nInterpretacja wyników dla danych skorelowanych:")
if pearson_p_value_skorelowane < alpha:
    print("Odrzucamy hipotezę zerową: Korelacja Pearsona jest istotna statystycznie.")
else:
    print("Nie odrzucamy hipotezy zerowej: Korelacja Pearsona nie jest istotna statystycznie.")

if spearman_p_value_skorelowane < alpha:
    print("Odrzucamy hipotezę zerową: Korelacja Spearmana jest istotna statystycznie.")
else:
    print("Nie odrzucamy hipotezy zerowej: Korelacja Spearmana nie jest istotna statystycznie.")

print("\nInterpretacja wyników dla danych nieskorelowanych:")
if pearson_p_value_nieskorelowane < alpha:
    print("Odrzucamy hipotezę zerową: Korelacja Pearsona jest istotna statystycznie.")
else:
    print("Nie odrzucamy hipotezy zerowej: Korelacja Pearsona nie jest istotna statystycznie.")

if spearman_p_value_nieskorelowane < alpha:
    print("Odrzucamy hipotezę zerową: Korelacja Spearmana jest istotna statystycznie.")
else:
    print("Nie odrzucamy hipotezy zerowej: Korelacja Spearmana nie jest istotna statystycznie.")

plt.figure(figsize=(12, 6))

# Skorelowane dane
plt.subplot(1, 2, 1)
plt.scatter(x_skorelowane, y_skorelowane)
plt.title("Dane skorelowane")
plt.xlabel("X")
plt.ylabel("Y")

# Nieskorelowane dane
plt.subplot(1, 2, 2)
plt.scatter(x_nieskorelowane, y_nieskorelowane)
plt.title("Dane nieskorelowane")
plt.xlabel("X")
plt.ylabel("Y")

plt.tight_layout()
plt.show()
