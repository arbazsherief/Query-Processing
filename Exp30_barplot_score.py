import matplotlib.pyplot as plt
import numpy as np

men_means = [22, 30, 35, 35, 26]
women_means = [25, 32, 30, 35, 29]

N = len(men_means)

ind = np.arange(N)

width = 0.35

plt.figure(figsize=(8, 6))
plt.bar(ind, men_means, width, label='Men')
plt.bar(ind + width, women_means, width, label='Women')

plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(ind + width / 2, ('Group1', 'Group2', 'Group3', 'Group4', 'Group5'))
plt.legend()

plt.tight_layout()
plt.show()
