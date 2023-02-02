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

def RotarImagen(imagen):
    plt.imshow(imagen,cmap='gray')
    plt.ion()

    for i in range(360):
        imagen = transform.rotate(imagen,i/10,cval=255)
        plt.imshow(imagen,cmap='gray')
        plt.pause(0.1)
        plt.cla()
