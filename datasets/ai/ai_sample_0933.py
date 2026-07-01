import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define cube
a = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], 
 [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])

# Set up graph
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)
ax.set_zlim(-1, 2)

# Plot cube
ax.scatter(a[:, 0], a[:, 1], a[:, 2])

# Connect the dots
for i in range(4):
 ax.plot([a[i, 0], a[i+4, 0]], [a[i, 1], a[i+4, 1]], 
 [a[i, 2], a[i+4, 2]])
for i in range(4):
 ax.plot([a[i, 0], a[(i+1)%4, 0]], [a[i, 1], 
 a[(i+1)%4, 1]], [a[i, 2], a[(i+1)%4, 2]])
ax.plot([a[4, 0], a[7, 0]], [a[4, 1], a[7, 1]], 
 [a[4, 2], a[7, 2]])
ax.plot([a[5, 0], a[6, 0]], [a[5, 1], a[6, 1]], 
 [a[5, 2], a[6, 2]])

# Show plot
plt.show()