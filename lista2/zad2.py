import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# a) Generowanie populacji
population_size = 100000
population = np.random.normal(100, 15, population_size)

# b) Wybieranie próbek o różnych liczebnościach
sample_sizes = [10, 50, 500]
confidence_intervals = []

for size in sample_sizes:
    means = [np.mean(np.random.choice(population, size=size)) for _ in range(1000)]
    stds = [np.std(np.random.choice(population, size=size), ddof=1) for _ in range(1000)]
    
    ci_95 = [stats.t.interval(0.95, len(np.random.choice(population, size=size))-1, loc=m, scale=s/np.sqrt(size)) for m, s in zip(means, stds)]
    confidence_intervals.append(ci_95)

# c) Wizualizacja przedziałów ufności
plt.figure(figsize=(12, 8))

for i, size in enumerate(sample_sizes):
    lower = [ci[0] for ci in confidence_intervals[i]]
    upper = [ci[1] for ci in confidence_intervals[i]]
    plt.fill_between(range(1000), lower, upper, alpha=0.3, label=f'n={size}')

plt.axvline(np.mean(population), color='red', linestyle='dashed', label='Średnia populacji')
plt.legend()
plt.title('Przedziały ufności dla różnych rozmiarów próbki')
plt.show()
