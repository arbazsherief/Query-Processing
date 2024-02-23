import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)


fig, axs = plt.subplots(2)  
fig.suptitle('Multiple Plots')  

axs[0].plot(x, y1, label='Sine', color='blue')

axs[0].set_ylabel('Sine Function')
axs[0].legend()  


axs[1].plot(x, y2, label='Cosine', color='red')

axs[1].set_xlabel('X-axis')

axs[1].set_ylabel('Cosine Function')
axs[1].legend()  


plt.tight_layout()


plt.show()
