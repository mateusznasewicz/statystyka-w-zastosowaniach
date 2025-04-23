import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# a) Wczytanie danych
data = sns.load_dataset("tips")

# b) Obliczanie statystyk opisowych
stats = data.describe()

# c) Wizualizacja
plt.figure(figsize=(12, 8))

# Histogram
plt.subplot(2, 2, 1)
plt.hist(data['total_bill'], bins=30, alpha=0.7)
plt.title('Histogram')

# Boxplot
plt.subplot(2, 2, 2)
sns.boxplot(x=data['total_bill'])
plt.title('Boxplot')

# Wykres rozrzutu
plt.subplot(2, 2, 3)
sns.scatterplot(x=data['total_bill'], y=data['tip'])
plt.title('Wykres rozrzutu')

plt.tight_layout()
plt.show()

# d) Interpretacja
print(stats)
