# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:33:32 2023

@author: ashas
"""

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt


# def f(t,y):
#     return -y
# t_eval = np.arange(-5,5,0.1)
# y0= np.exp(5)
# #Task 1

# #y' = -y, t[-5,5],y0 = y(-5) = exp(5)

# sol = solve_ivp(f, [-5,5], [y0],method='RK45',t_eval=t_eval)

# print(sol)

# plt.plot(sol.t,sol.y[0], 'k--s')


# y_exact = np.exp(-t_eval)
# print("bla",y_exact)

#task 1.1
y0 = 3.018
t0 = 1960

def f2(t):
    return (y0*np.exp((0.02*(t-t0))))
t = np.arange(1800,2200,5)

data_1 = np.array([1800, 1850, 1900])
data_2 = np.arange( 1950, 2015,5)
data_t = np.append(data_1,data_2)
data_p = np.array([1, 1.262, 1.650, 2.525, 2.758, 3.018, 3.322,3.682, 4.061, 4.440, 4.853, 5.310, 5.735, 6.127, 6.520,6.930, 7.349])
plt.plot(t,f2(t),data_t,data_p,'ro')
plt.xlabel('Time[yr]')
plt.ylabel('Population[bn]')
plt.xlim([1800,2200])
plt.ylim([0,15])
plt.grid()
plt.legend('exp growth', 'est world pop data')

#task 1.2

def f(t,y):
    return 0.02 * y

sol = solve_ivp(f,[t0,2200],[y0],method='RK45')
plt.plot(sol.t,sol.y[0],'k--s')


