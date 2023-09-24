# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:33:32 2023

@author: ashas
"""

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

#%%

#Task 1 
t_eval = np.arange(-5,5,0.1)
y0= np.exp(5)

def f(t,y):
    return -y

sol = solve_ivp(f, [-5,5], [y0],method='RK45',t_eval=t_eval)
print("Numerical solution:",sol)

y_exact = np.exp(-t_eval)
print("exact:",y_exact)

plt.plot(sol.t,sol.y[0],'r+')
plt.plot(t_eval,y_exact,color='green')
plt.xlim(-6,5)
plt.show()

#%%
#Task 1.1
y0 = 3.018
t0 = 1960

def f2(t):
    return (y0*np.exp((0.02*(t-t0))))
t = np.arange(1800,2200,5)

data_1 = np.array([1800, 1850, 1900])
data_2 = np.arange( 1950, 2020,5)
data_t = np.append(data_1,data_2)
data_p = np.array([1, 1.262, 1.650, 2.525, 2.758, 3.018, 3.322,3.682, 4.061, 4.440, 4.853, 5.310, 5.735, 6.127, 6.520,6.930, 7.349])
plt.plot(t,f2(t),data_t,data_p,'ro')
plt.xlabel('Time[yr]')
plt.ylabel('Population[bn]')
plt.xlim([1800,2200])
plt.ylim([0,15])
plt.grid()
plt.legend('exp growth', 'est world pop data')
plt.show()

#%%
#Task 1.2
y0= 3.018
t0 = 1960
t_eval = np.arange(t0,2200,1)

def f3(t,y):
    return 0.02 * y

sol = solve_ivp(f3,[t0,2200],[y0],method='RK45', t_eval=t_eval)

plt.plot(t,f2(t),'b.',data_t,data_p,'ro',sol.t,sol.y[0],'r--')
plt.xlabel('Time [yr')
plt.ylabel('Populatin [bn')
plt.title('Exponential Growth')
plt.xlim([1800,2200])
plt.ylim([0,15])
plt.grid()
plt.legend(['Exponential growth (exact)', 'Estimated World Population Data', 'Exponential growth(solve_ivp)'])
plt.show()

#%%
#Task 1.3
y0 = 3.018
t0 = 1960
t_eval = np.arange(t0,2200,1)
g = 0.029
p = 2.941*10**-3

def f4(t,y):
    return (g-p*y)*y

sol2 = solve_ivp(f4, [t0,2200], [y0], method='RK45',t_eval=t_eval)
plt.plot(t,f2(t),'b.',data_t,data_p,'ro',sol.t,sol.y[0],'r--',sol2.t,sol2.y[0],'k--')
plt.xlabel('Time[yr]')
plt.ylabel('Population[bn]')
plt.title('Exponential Growth')
plt.xlim([1800,2200])
plt.ylim([0,15])
plt.grid()
plt.legend(['Exponential growth (exact)', 'Estimated World Population Data', 'Exponential growth(solve_ivp)','Verhulst (solove_ivp)'])
plt.show()

#%%
#Task 1.4
y0 = 3.018
t0 = 1960
t_eval = np.arange(t0,2200,1)
g = np.arange(0.01,0.06,0.01)

p = np.arange(0.001,0.006,0.001)

for i,j in zip(g,p):
    def f5(t,y):
        return (i-j*y)*y
    
    sol3 = solve_ivp(f5, [t0,2200], [y0], method='RK45',t_eval=t_eval)
    plt.plot(t,f2(t),'b.',data_t,data_p,'ro',sol.t,sol.y[0],'r--',sol3.t,sol3.y[0],'k--')
    plt.xlabel('Time[yr]')
    plt.ylabel('Population[bn]')
    plt.title('Exponential Growth')
    plt.xlim([1800,2200])
    plt.ylim([0,15])
    plt.grid()
    plt.legend(['Exponential growth (exact)', 'Estimated World Population Data', 'Exponential growth(solve_ivp)','Verhulst (solove_ivp) with g {} and p {}'.format(i,j)])
    plt.show()

#%%
#Task 1.5
y0 = np.array([50,30])
y0_reshaped = y0.reshape(2,)
g1 = 0.5
g2 = 0.8
g3 = 0.008
t_eval = np.arange(0,40,0.001)

def f6(t,y):
    return np.array([g1*y[0]-g3*y[0]*y[1], -g2*y[1]+g3*y[0]*y[1]])



sol4 = solve_ivp(f6, [0,40], y0,  method='RK45',t_eval=t_eval)

plt.plot(sol4.t,sol4.y[0],sol4.t,sol4.y[1])
plt.xlabel('Time[yr]')
plt.ylabel('Population[bn]')
plt.legend(['prey','predator'])
plt.title('Time Series Prey & Predator')
plt.show()
    
y1 = g2 / g3
y2 = g1 / g3

plt.plot(sol4.y[1],sol4.y[0],[y1,y1],[y2,y2],[20,200])
plt.xlabel('Predator')
plt.ylabel('Prey')
plt.text(y2 + 5,y1 + 10,'Fixed Point')
plt.title('Phase Space')
plt.show()

'''
Observation: There seems to be no intersection, so no stabilisation for both populations
'''

#%%
#Task 1.6
y0 = np.array([50,30])
y0_reshaped = y0.reshape(2,)
g1 = 0.5
g2 = 0.8
g3 = 0.008
g4 = 0.0005
t_eval = np.arange(0,200,0.001)

def f7(t,y):
    return np.array([g1*y[0]-g3*y[0]*y[1]-g4*y[0]**2, -g2*y[1]+g3*y[0]*y[1]])



sol4 = solve_ivp(f7, [0,200], y0,  method='RK45',t_eval=t_eval)

plt.plot(sol4.t,sol4.y[0],sol4.t,sol4.y[1])
plt.xlabel('Time[yr]')
plt.ylabel('Population[bn]')
plt.legend(['prey','predator'])
plt.title('Time Series Prey & Predator')
plt.show()
    
y1 = g2 / g3
y2 = g1 / g4

plt.figure(figsize=(10,6))
plt.plot(sol4.y[1], sol4.y[0], [y2, y2], [y1, y1])
plt.xlim(0, 500)
plt.ylim(0, 500)
plt.xlabel('Predator')
plt.ylabel('Prey')
plt.text(y2, y1, 'Fixed Point')
plt.title('Phase Space')
plt.show()


