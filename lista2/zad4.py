import numpy as np


# a) Generowanie populacji
population_size = 100000
population = np.random.normal(50, 10, population_size)

# b) Próba losowa prosta
sample_simple = np.random.choice(population, 1000)

# c) Próba warstwowa (losowanie z dwóch grup)
group1 = population[population < 50]
group2 = population[population >= 50]
sample_stratified = np.concatenate([np.random.choice(group1, 500), np.random.choice(group2, 500)])

# d) Próba systematyczna
sample_systematic = population[::10][:1000]

# e) Porównanie wyników
sample_means = {
    'Prosta': np.mean(sample_simple),
    'Warstwowa': np.mean(sample_stratified),
    'Systematyczna': np.mean(sample_systematic)
}

sample_stds = {
    'Prosta': np.std(sample_simple, ddof=1),
    'Warstwowa': np.std(sample_stratified, ddof=1),
    'Systematyczna': np.std(sample_systematic, ddof=1)
}

print("Średnie próbek:")
print(sample_means)

print("\nOdchylenia standardowe próbek:")
print(sample_stds)
