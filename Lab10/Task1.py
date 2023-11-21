import numpy as np
import matplotlib.pyplot as plt

def f1(x,y):
    return x**2-y**2

def f2(x,y):
    return x*y**2*(np.sin(x)+np.sin(y))
x = np.linspace(-np.pi,np.pi)
y = np.linspace(-np.pi,np.pi)

X, Y = np.meshgrid(x, y)

Z1 = f1(X, Y)
Z2 = f2(X,Y)

fig = plt.figure(1)

ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z1, cmap='viridis')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.show()
plt.figure(2)
ax.plot_surface(X, Y, Z2, cmap='viridis')

# Add labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Show the plot
plt.show()