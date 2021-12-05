import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(3000)

png = np.array(cv.imread("cicek.png", -1))

pngNP = np.zeros((png.shape[0], png.shape[1]))
labelMap = np.zeros((png.shape[0], png.shape[1]))

for i in range(0,png.shape[0],1):
    for j in range(0,png.shape[1],1):
        pngNP[i][j] = png[i][j][0]
        
seedPoint = (500,635)

def mean(x,y):
    global pngNP
    return (pngNP[x-1][y] + pngNP[x+1][y] + pngNP[x][y-1] + pngNP[x][y+1]) / 4 

def rec(x,y, lastWay):
    global labelMap
    me = mean(x,y)

    print(me)


    if(me > 130):
        labelMap[x][y] = 1
        if(lastWay != "N"):
            if(labelMap[x,y-1] == 1):
                return
            rec(x,y-1,"S")
        if(lastWay != "S"):
            if(labelMap[x,y+1] == 1):
                return
            rec(x,y+1,"N")
        if(lastWay != "W"):
            if(labelMap[x-1,y] == 1):
                return
            rec(x-1,y,"E")
        if(lastWay != "E"):
            if(labelMap[x+1,y] == 1):
                return
            rec(x+1,y, "W")

rec(seedPoint[0],seedPoint[1],"")


for i in range(0,pngNP.shape[0],1):
    for j in range(0,pngNP.shape[1],1):
        if(labelMap[i,j] == 1):
            png[i,j,0] = 255

png[seedPoint[0],seedPoint[1]] = [0,0,255,255]

plt.imshow(png)
plt.show()
        
