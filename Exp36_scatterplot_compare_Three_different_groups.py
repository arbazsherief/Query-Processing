import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

group_1_heights = np.random.normal(160, 10, 30)
group_1_weights = np.random.normal(60, 5, 30)

group_2_heights = np.random.normal(170, 8, 30)
group_2_weights = np.random.normal(70, 6, 30)

group_3_heights = np.random.normal(155, 12, 30)
group_3_weights = np.random.normal(50, 8, 30)

plt.scatter(group_1_heights, group_1_weights, color='blue',
            label='Group 1', alpha=0.7, edgecolor='black')
plt.scatter(group_2_heights, group_2_weights, color='green',
            label='Group 2', alpha=0.7, edgecolor='black')
plt.scatter(group_3_heights, group_3_weights, color='red',
            label='Group 3', alpha=0.7, edgecolor='black')

plt.title('Scatter Plot: Heights vs Weights for Three Groups')
plt.xlabel('Heights (cm)')
plt.ylabel('Weights (kg)')

plt.legend()

plt.show()
