'''
Name: Angelina Patterson
Start Date: 7/16/25
Description: This program is for the modeling of the Lotka-Volterra predator-prey system.This model a predator-prey system of
rabbits vs foxes vs cougars with a growth of grass each week
Reference: "Python Code for Predator-Prey Model" by Mike Saint-Antoine on YouTube
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# stating initial condition such as the population size
# [grass,rabbits, foxes, Cougars]
y0 = [250, 40, 10, 5]
# starting time at 0 to 50 and time points will be at 1000 for weeks
t = np.linspace(0, 150, 4000)
# define the parameters [ ; means the older parameters from pervious results]
r = 0.10        # grass growth rate; 0.09
mue = 0.0012     # grass consumed by rabbits
alpha = 0.0012   # rabbit birth rate; 0.002
beta = 0.0012   # rate in which the rabbits are eaten by foxes
delta = 0.0015  # rate in which fox reproduce as they eat rabbits; 0.005
gamma = 0.0011  # natural death rate of foxes; 0.001
theta = 0.01  # rate in which cougars eat rabbits; 0.001
kappa = 0.01   # rate in which cougars eat foxes; 0.002
espilon = 0.0005  # the rate at which cougars reproduce after consuming rabbit and foxes; 0.0005
zeta = 0.08     # cougar natural death rate; 0.004

# set values into an array
variables = [r, mue, alpha, beta, delta, gamma,theta, kappa, espilon, zeta]
# in this function will be used to pass through the ODE functions
def solver(var, t, variables):
    # grass population
    g = var[0]
    # rabbit population
    x = var[1]
    # population of foxes
    y = var[2]
    # population of cougars
    z = var[3]
    # re define the variables with in this function
    # for stating what will be a part of the first array
    r = variables[0]
    mue = variables[1]
    alpha = variables[2]
    beta = variables[3]
    delta = variables[4]
    gamma = variables[5]
    theta = variables[6]
    kappa = variables[7]
    espilon = variables[8]
    zeta = variables[9]
    # defining the ODE; based on the Excel sheet
    # keeping the grass rising expoetianly
    dgdt = r * g - mue * g * x  # grass growing - the rate in which grass in consumed by the rabbits
    dxdt = alpha * g * x - beta * x * y - theta * x * z    # the ODE for which the growth of rabbit - rabbits that are eaten by foxes
    dydt = delta * x * y - gamma * y - kappa * y * z       # the ODE for which the foxes eat rabbits - the death rate of foxes
    dzdt = espilon * (x * z + y * z) - zeta * z # rate in which Cougars eat both rabbits and foxes
    # for returning the ODEs
    return([dgdt, dxdt, dydt, dzdt])

# for running the simulaiton
y = odeint(solver, y0, t, args=(variables,))

# Plot the results
f,(ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=(10, 6))
# creating the plot
line1, = ax1.plot(t, y[:, 0], color="green")
line2, = ax2.plot(t, y[:, 1], color="blue")
line3, = ax3.plot(t, y[:, 2], color="orange")
line4, = ax4.plot(t, y[:, 3], color="pink")
# Labels for the plot
ax4.set_xlabel("Time counted in weeks")
ax1.set_ylabel("Grass")
ax2.set_ylabel("Rabbits")
ax3.set_ylabel("Foxes")
ax4.set_ylabel("Cougars")
# add grid lines
for ax in [ax1, ax2, ax3, ax4]:
    ax.grid(True)
# print the plot
plt.show()







