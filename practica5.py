from matplotlib import pyplot as plt
from matplotlib import pylab 
import cv2
import imutils

fila = 3
columna = 3

img1 = cv2.imread('manto.jpg', 1)
fig = plt.figure(figsize=(10,7), constrained_layout=True)
fig.add_subplot(fila,columna,1)
plt.title("Imagen Original")
plt.imshow(img1)

fig.add_subplot(fila,columna,2)
img1 = cv2.imread('manto.jpg', 1)
ret,img1 = cv2.threshold(img1, 125, 255 , cv2.THRESH_BINARY)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.axis('off')
plt.title("Imagen: THRESH_BINARY")

fig.add_subplot(fila,columna,3)
img1 = cv2.imread('manto.jpg', 1)
ret,img1 = cv2.threshold(img1, 125, 255 , cv2.THRESH_BINARY_INV)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.axis('off')
plt.title("Imagen: THRESH_BINARY_INV")

fig.add_subplot(fila,columna,4)
img1 = cv2.imread('manto.jpg', 1)
ret,img1 = cv2.threshold(img1, 125, 255 , cv2.THRESH_TRUNC)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.axis('off')
plt.title("Imagen: THRESH_TRUNC")


fig.add_subplot(fila,columna,5)
img1 = cv2.imread('manto.jpg', 1)
ret,img1 = cv2.threshold(img1, 125, 255 , cv2.THRESH_TOZERO)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.axis('off')
plt.title("Imagen: THRESH_TOZERO")

fig.add_subplot(fila,columna,6)
img1 = cv2.imread('manto.jpg', 1)
ret,img1 = cv2.threshold(img1, 125, 255 , cv2.THRESH_TOZERO_INV)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.axis('off')
plt.title("Imagen: THRESH_TOZERO_INV")

fig.add_subplot(fila,columna,7)
img1 = cv2.imread('manto.jpg', 1)
ret,img1 = cv2.threshold(img1, 125, 255 , (cv2.THRESH_BINARY+cv2.THRESH_OTSU))
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.axis('off')
plt.title("Imagen: THRESH_OTSU")
plt.show()
