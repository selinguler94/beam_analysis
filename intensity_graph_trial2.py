import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageFilter



# Open the image and apply a median filter
image = Image.open(r'')
image = image.filter(ImageFilter.MedianFilter(3))
pixels = image.load()



# Calculate the irradiance and distance data
y_axis = int(image.height/2)
irradiance, distance = [], []



for i in range(image.width):  
    irradiance.append((sum(pixels[i, y_axis]))/100)
        distance.append((i + 1)/100)

        

# Find the 1/e^2 point
max_irradiance = max(irradiance)
one_over_e_squared = max_irradiance / np.exp(2)
one_over_e_squared_index = np.argmin(np.abs(irradiance - one_over_e_squared))
one_over_e_squared_distance = distance[one_over_e_squared_index]



# Calculate the x = 1/e^2 function
x = np.linspace(0, one_over_e_squared_distance, 50)
y = one_over_e_squared * np.ones(x.shape)
plt.plot(distance, irradiance)
plt.plot(y,x)



peak_irradiance = np.max(irradiance)
print('Peak irradiance:', peak_irradiance, 'W/m^2')



#beam_diameter (no unit since not a real value calculated from a valid equation or set of data)
beam_diameter = 2 * np.sqrt(peak_irradiance / (1/(np.e)**2 * peak_irradiance)) * 1/(np.e)**2
print(beam_diameter)



plt.ylabel('irradiance (W/m^2)')
plt.xlabel('distance (m)')
plt.title('Irradiance Distance Graph for He-Ne Laser')
plt.show()
