import matplotlib.pyplot as plt
import numpy as np

# Total power of the laser beam (W)
power = 1   
# Wavelength of the laser (m)
wavelength = 632.8
# Distance from the source (m)
distance = np.arange(0, 60, 10)
#Beam radius (m) using the equation for a Gaussian beam
beam_radius = wavelength * distance / (np.pi * np.sqrt(2))
#Irradiance (W/m^2) using the equation for a Gaussian beam
irradiance = ((power / (np.pi * beam_radius**2)) * np.exp(-2 * (distance / beam_radius)**2))

#err: the peak irradiance valued as nan W/m^2
beam_radius[beam_radius <= 0] = 1e-10
distance[distance == 0] = 1e-10

#irradiance as a function of distance
plt.plot(distance, irradiance)
plt.xlabel('Distance (m)')
plt.ylabel('Irradiance (W/m^2)')
plt.title('Irradiance distance graph of a Gaussian beam')

#peak irradiance
peak_irradiance = np.max(irradiance)
print('Peak irradiance:', peak_irradiance, 'W/m^2')

#calculating the diameter beam_diameter = beam_radius
e1_irradiance = peak_irradiance * np.e
beam_diameter = 2 * np.sqrt(peak_irradiance / e1_irradiance) * 1/(np.e)**2
plt.show()
