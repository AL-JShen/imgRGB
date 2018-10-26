import numpy as np
import cv2

filepath = ''

img = cv2.imread(filepath)
img = img[...,::-1]

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

R = []
G = []
B = []
for row in img:
    rRow = []
    gRow = []
    bRow = []
    for pixel in row:
        rRow.append(pixel[0])
        gRow.append(pixel[1])
        bRow.append(pixel[2])
    R.append(rRow)
    G.append(gRow)
    B.append(bRow)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(R[0], G[0], B[0])
plt.show()


