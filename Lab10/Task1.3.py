import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sy

# Define the symbols
x, y = sy.symbols('x y')

# Define the scalar function
f = ((x**2 - 1) + (y**2 - 4) + (x**2 - 1)*(y**2 - 4))/(x**2 + y**2 + 1)**2
f = sy.Matrix([f])
X = sy.Matrix([x,y])
Df = f.jacobian(X)

# Compute partial derivatives symbolically
df_dx = sy.diff(f, x)
df_dy = sy.diff(f, y)

# Convert symbolic expressions to lambdified functions
scalar_function = sy.lambdify((x, y), f, 'numpy')
gradient_x = sy.lambdify((x, y), Df[0], 'numpy')
gradient_y = sy.lambdify((x, y), Df[1], 'numpy')

# Generate data points
x_vals = np.linspace(-5, 5, 100)
y_vals = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x_vals, y_vals)
Z = scalar_function(X, Y)

# Create the surface plot
fig = plt.figure(figsize=(12, 6))

# Surface plot
ax_surface = fig.add_subplot(121, projection='3d')
ax_surface.plot_surface(X, Y, Z, cmap='viridis')
ax_surface.set_title('Surface Plot of Scalar Function')
ax_surface.set_xlabel('X-axis')
ax_surface.set_ylabel('Y-axis')
ax_surface.set_zlabel('Z-axis')

# Create the quiver plot for the gradient
U = gradient_x(X, Y)
V = gradient_y(X, Y)

ax_quiver = fig.add_subplot(122)
ax_quiver.quiver(X, Y, U, V, scale=20, color='blue', width=0.007)
ax_quiver.set_title('Gradient Field')
ax_quiver.set_xlabel('X-axis')
ax_quiver.set_ylabel('Y-axis')

plt.show()