import matplotlib.pyplot as plt
from scipy import special
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import numpy as np

# data
power, distance = [], []


with open("power.txt", "r") as power_values:
    power_lines = power_values.readlines()
with open("distance.txt", "r") as distance_values:
    distance_lines = distance_values.readlines()
for i in range(len(power_lines)):
    power.append(float(power_lines[i]))
    distance.append(float(distance_lines[i]))

    
# the function to fit to the data
def power_func(x, a, b):
    return a * np.exp(-b * x)


# fit
params, covar = curve_fit(power_func, distance, power)
a, b = params


# generated data
x_curve = np.linspace(0, 2, 50)
y_curve = power_func(x_curve, a, b)


plt.plot(distance, power, '-', color='g')
plt.plot(x_curve, y_curve, '--', color='b')


plt.xlabel('Distance (m)')
plt.ylabel('Power (mW)')
plt.show()
