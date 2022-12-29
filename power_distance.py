import matplotlib.pyplot as plt
from scipy import special
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import numpy as np

#pull the data
power, distance = [], []
with open("power.txt", "r") as power_values:
    power_lines = power_values.readlines()
with open("distance.txt", "r") as distance_values:
    distance_lines = distance_values.readlines()
for i in range(len(power_lines)):
    power.append(float(power_lines[i]))
    distance.append(float(distance_lines[i]))

# Define the function to fit to the data
def power_func(x, a, b):
    return a * np.exp(-b * x)

# Use curve_fit to fit the function to the data
params, covar = curve_fit(power_func, distance, power)
a, b = params

# Generate a range of x values for the curve
x_curve = np.linspace(0, 2, 50)

# Calculate the curve values
y_curve = power_func(x_curve, a, b)

# Plot the data and the curve
plt.plot(distance, power, 'o', x_curve, y_curve, '-')
plt.xlabel('Distance (m)')
plt.ylabel('Power (mW)')
plt.show()