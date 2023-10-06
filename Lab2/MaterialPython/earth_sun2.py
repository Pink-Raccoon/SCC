import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import auxiliary_methods as am

ce = [5.0, 0.0]  # start coordinates of earth
sun = [0.0, 0.0]  # coordinates of the sun

n_per_day = 1
n_days = 365
n = n_days * n_per_day  # number of iterations
phi_rotate = 2 * np.pi / n_days / n_per_day  # angular velocity earth - sun

side_len = 0.8
tHori = np.array([side_len/2, 0])
tVerti = np.array([0, side_len/2])

s1 = ce - tHori - tVerti
s2 = ce + tHori - tVerti
s3 = ce + tHori + tVerti
s4 = ce - tHori + tVerti

ce = np.append(ce, 1)
sun = np.append(sun, 1)
s1 = np.append(s1, 1)
s2 = np.append(s2, 1)
s3 = np.append(s3, 1)
s4 = np.append(s4, 1)

ce_list = []
for i in range(n):
    ce = am.rotate_around_point(ce, sun[0], sun[1], phi_rotate)
    s1 = am.rotate_around_point(s1, sun[0], sun[1], phi_rotate)
    s2 = am.rotate_around_point(s2, sun[0], sun[1], phi_rotate)
    s3 = am.rotate_around_point(s3, sun[0], sun[1], phi_rotate)
    s4 = am.rotate_around_point(s4, sun[0], sun[1], phi_rotate)
    ce_list.append((ce, s1, s2, s3, s4))  # generate coordinates

# Initialize the figure and axis
fig, ax = plt.subplots()
plt.plot(sun[0], sun[1], '*b')
center_dot, = plt.plot([], [], '.r')
earth_plot, = plt.plot([],[],'r')

def init():
    ax.set_aspect('equal', 'box')
    ax.axis([-10, 10, -10, 10])
    return center_dot,

def update(frame):
    cs, s1, s2, s3, s4 = ce_list[frame]
    square = np.stack([s1,s2,s3,s4,s1])
    x_data,y_data = square[:,0],square[:,1]
    earth_plot.set_data(x_data,y_data)
    center_dot.set_data(cs[0], cs[1])
    
    return center_dot,

ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)
plt.show()
