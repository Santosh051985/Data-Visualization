import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10)
y = x ^ 2
z = x ^ 3
t = x ^ 4
plt.xlabel('Distance')
plt.ylabel('Time')
plt.title("Graph Drawing")
plt.plot(x , y)
plt.show()
