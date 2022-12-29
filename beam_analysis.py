from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import math


#upload the image
image = Image.open(r'')
image = image.filter(ImageFilter.MedianFilter(3))
pixels = image.load()


#irradience of the 'image'
y_axis = int(image.height/2)
irradiance, section = [], []


for i in range(image.width):
    irradiance.append((sum(pixels[i, y_axis])))
    section.append((i + 1))


plt.plot(section, irradiance)
plt.ylabel('irradiance (W/m^2)'), plt.xlabel('distance (m)')
plt.show()
