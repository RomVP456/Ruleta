import numpy as np
import matplotlib.pyplot as plt
width=500
image=255*np.ones([width,width])
center=np.round(width/2)
r=np.round(center*0.75)
for x in range(width):
    for y in range(width):
        r1=(x-center)**2+(y-center)**2
        if r1<=r**2:
               image[x,y]=0

plt.imshow(image,cmap='gray')
plt.show()