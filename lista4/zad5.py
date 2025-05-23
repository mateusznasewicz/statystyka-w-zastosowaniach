import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

mean1 = 0
mean2 = 0.1
std = 1
max_sample_size = 1000
step = 10

sample_sizes = range(10, max_sample_size + 1, step)
p_values = []

for n in sample_sizes:
    group1 = np.random.normal(loc=mean1, scale=std, size=n)
    group2 = np.random.normal(loc=mean2, scale=std, size=n)
    stat, p = ttest_ind(group1, group2)
    p_values.append(p)

plt.figure(figsize=(10,6))
plt.plot(sample_sizes, p_values, marker='o')
plt.axhline(y=0.05, color='r', linestyle='--', label='Poziom istotności 0.05')
plt.title('Wpływ liczności próby na wartość p (test t-Studenta)')
plt.xlabel('Liczność próby')
plt.ylabel('Wartość p')
plt.legend()
plt.grid(True)
plt.show()
