import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from PIL import Image, ImageFilter

image = Image.open(r'')
#median filter is optional 
image = image.filter(ImageFilter.MedianFilter(3))
pixels = image.load()
x_axis, y_axis, z_axis = [], [], []
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for x in range(image.width):
    for y in range(image.height):
        x_axis.append(x)
        y_axis.append(y)
        z_axis.append(sum(pixels[x, y]))
ax.scatter(x_axis, y_axis, z_axis, c=z_axis, cmap=cm.jet)
fig.colorbar(ax.scatter(x_axis, y_axis, z_axis, c=z_axis, cmap=cm.jet))
plt.show()