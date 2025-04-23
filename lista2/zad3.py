import numpy as np

# a) Generowanie bimodalnej populacji
population = np.concatenate([np.random.normal(40, 5, 50000), np.random.normal(60, 5, 50000)])

# b) Pobieranie próbek
sample_random = np.random.choice(population, 1000)
sample_non_random = np.random.choice(population[population < 50], 1000)

# c) Obliczanie średniej i odchylenia standardowego
mean_population = np.mean(population)
std_population = np.std(population)

mean_random = np.mean(sample_random)
std_random = np.std(sample_random)

mean_non_random = np.mean(sample_non_random)
std_non_random = np.std(sample_non_random)

# d) Wyniki
print(f"Średnia populacji: {mean_population}, Odchylenie standardowe populacji: {std_population}")
print(f"Średnia próbki losowej: {mean_random}, Odchylenie standardowe próbki losowej: {std_random}")
print(f"Średnia próbki nielosowej: {mean_non_random}, Odchylenie standardowe próbki nielosowej: {std_non_random}")
