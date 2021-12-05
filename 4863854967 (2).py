import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

im = cv.imread("cicek.png", cv.IMREAD_GRAYSCALE)

ret, binImg  = cv.threshold(im,127,255,cv.THRESH_BINARY)

era = binImg.copy()

for i in range(0,era.shape[0],1):
    for j in range(0,era.shape[1],1):
        if(binImg[i][j] == 0):
            for l in range(i-1,i+2,1):
                for k in range(j-1,j+2,1):
                    if( l < 0 or k < 0 or l >= binImg.shape[0] or k >= binImg.shape[1]):
                        continue
                    era[l][k] = 0

dele = era.copy()

for i in range(0,dele.shape[0],1):
    for j in range(0,dele.shape[1],1):
        if(era[i][j] == 255):
            for l in range(i-1,i+2,1):
                for k in range(j-1,j+2,1):
                    if( l < 0 or k < 0 or l >= binImg.shape[0] or k >= binImg.shape[1]):
                        continue
                    dele[l][k] = 1

era1 = binImg.copy()

for i in range(0,era1.shape[0],1):
    for j in range(0,era1.shape[1],1):
        if(binImg[i][j] == 0):
            for l in range(i-3,i+4,1):
                for k in range(j-3,j+4,1):
                    if( l < 0 or k < 0 or l >= binImg.shape[0] or k >= binImg.shape[1]):
                        continue
                    era1[l][k] = 0

dele1 = era1.copy()

for i in range(0,dele1.shape[0],1):
    for j in range(0,dele1.shape[1],1):
        if(era1[i][j] == 255):
            for l in range(i-3,i+4,1):
                for k in range(j-3,j+4,1):
                    if( l < 0 or k < 0 or l >= binImg.shape[0] or k >= binImg.shape[1]):
                        continue
                    dele1[l][k] = 1


fig, axs = plt.subplots(2,3)

axs[0][0].imshow(binImg , cmap = plt.cm.gray)
axs[0][0].set_title("rawThreshold")

axs[0][1].imshow(era , cmap = plt.cm.gray)
axs[0][1].set_title("Image Erasion 3x3")

axs[0][2].imshow(dele , cmap = plt.cm.gray)
axs[0][2].set_title("Image Dilation 3x3")

axs[1][1].imshow(era1 , cmap= plt.cm.gray)
axs[1][1].set_title("Image Erasion 5x5")

axs[1][2].imshow(dele1, cmap = plt.cm.gray)
axs[1][2].set_title("Image Dilation 5x5")


plt.show()
