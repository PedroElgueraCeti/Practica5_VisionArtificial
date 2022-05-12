from matplotlib import pyplot as plt
from matplotlib import pylab 
import cv2
import imutils

img1 = cv2.imread('manto.jpg', 1)
ret,img1 = cv2.threshold(img1, 125, 255 , cv2.THRESH_BINARY)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
fig = plt.figure(figsize=(10,7), constrained_layout=True)
plt.imshow(img1)
plt.axis('off')
plt.title("Imagen 1")
plt.show()