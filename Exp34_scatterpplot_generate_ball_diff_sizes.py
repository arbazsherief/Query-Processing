import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

num_points = 50
x_values = np.random.rand(num_points)
y_values = np.random.rand(num_points)
colors = np.random.rand(num_points, 3)

sizes = np.random.randint(10, 500, num_points)

plt.scatter(x_values, y_values, color=colors,
            alpha=0.7, s=sizes, edgecolor='black')

plt.title('Scatter Plot with Balls of Different Sizes')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
