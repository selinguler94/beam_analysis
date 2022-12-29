import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageFilter


#upload the image
image = Image.open(r'')
image = image.filter(ImageFilter.MedianFilter(3))
pixels = image.load()


#the irradiance and distance data
y_axis = int(image.height/2)
irradiance, distance = [], []


for i in range(image.width):
    irradiance.append((sum(pixels[i, y_axis]))/100)
    distance.append((i + 1)/100)

    
#the 1/e^2 point
max_irradiance = max(irradiance)
one_over_e_squared = max_irradiance / np.exp(2)
one_over_e_squared_index = np.argmin(np.abs(irradiance - one_over_e_squared))
one_over_e_squared_distance = distance[one_over_e_squared_index]


#the x = 1/e^2 function
x = np.linspace(0, one_over_e_squared_distance, 50)
y = one_over_e_squared * np.ones(x.shape)


plt.plot(distance, irradiance)
plt.plot(y,x)


#peak irradiance
peak_irradiance = np.max(irradiance)


#the peak irradiance of the beam
peak_irradiance = np.max(irradiance)
peak_irradiance_index = np.argmax(irradiance)
peak_irradiance_distance = distance[peak_irradiance_index]
plt.plot([peak_irradiance_distance, peak_irradiance_distance], [0, peak_irradiance], '--')


#beam_diameter (no unit since not a real value calculated from a valid equation or set of data)
beam_diameter = 2 * np.sqrt(peak_irradiance / (1/(np.e)**2 * peak_irradiance)) * 1/(np.e)**2


plt.text(0.03, 0.91, f'Peak irradiance: {peak_irradiance:.2f}' ' W/m^2', transform=plt.gca().transAxes, fontsize = 8)
plt.text(0.03, 0.95, f'Beam diameter: {beam_diameter:.2f}', transform=plt.gca().transAxes, fontsize = 8)
plt.text(0.16, 0.56, f'1/e^2 point', transform=plt.gca().transAxes, fontsize = 8)


plt.ylabel('irradiance (W/m^2)')
plt.xlabel('distance (m)')
plt.title('Irradiance Distance Graph for He-Ne Laser')
plt.show()
