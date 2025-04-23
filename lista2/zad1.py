import numpy as np
import matplotlib.pyplot as plt

# a) Generujemy dużą populację o rozkładzie normalnym
population_size = 100000
population = np.random.normal(50, 10, population_size)

# b) Wybieramy próbki o różnych rozmiarach
sample_sizes = [10, 50, 1000]
sample_means = []
sample_std_devs = []

# c) Obliczamy średnią i odchylenie standardowe dla próbek
for size in sample_sizes:
    samples = [np.random.choice(population, size=size) for _ in range(1000)]
    sample_means.append([np.mean(sample) for sample in samples])
    sample_std_devs.append([np.std(sample, ddof=1) for sample in samples])

# d) Porównujemy wyniki
population_mean = np.mean(population)
population_std = np.std(population)

# Wykresy
plt.figure(figsize=(12, 8))

# Średnia
plt.subplot(2, 2, 1)
plt.hist(sample_means[0], bins=30, alpha=0.7, label='n=10')
plt.hist(sample_means[1], bins=30, alpha=0.7, label='n=50')
plt.hist(sample_means[2], bins=30, alpha=0.7, label='n=1000')
plt.axvline(population_mean, color='red', linestyle='dashed', label='Średnia populacji')
plt.legend()
plt.title('Rozkład średnich próbek')

# Odchylenie standardowe
plt.subplot(2, 2, 2)
plt.hist(sample_std_devs[0], bins=30, alpha=0.7, label='n=10')
plt.hist(sample_std_devs[1], bins=30, alpha=0.7, label='n=50')
plt.hist(sample_std_devs[2], bins=30, alpha=0.7, label='n=1000')
plt.axvline(population_std, color='red', linestyle='dashed', label='Odchylenie standardowe populacji')
plt.legend()
plt.title('Rozkład odchyleń standardowych próbek')

plt.tight_layout()
plt.show()
