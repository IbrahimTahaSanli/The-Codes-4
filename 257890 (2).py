import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


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

needToCheck = [seedPoint]
Checked = []
currentPoint = 0
count = 0



while(len(needToCheck) != 0):
    (x, y) = needToCheck[0]


    if( 85.5 < mean(x, y) and labelMap[x,y] != 1):
        Checked.append(needToCheck[0])

        count += 1
        
        needToCheck.pop(0)
        
        labelMap[x][y] = 1

        if(not((x-1, y) in Checked and (x-1, y) in needToCheck)):
            needToCheck.append((x-1,y))

        if(not((x+1, y) in Checked and (x+1, y) in needToCheck)):
            needToCheck.append((x+1,y))

        if(not((x, y-1) in Checked and (x, y-1) in needToCheck)):
            needToCheck.append((x,y-1))

        if(not((x, y+1) in Checked and (x, y+1) in needToCheck)):
            needToCheck.append((x,y+1))
    else:
        Checked.append(needToCheck[0])
        needToCheck.pop(0)
        

for i in range(0,pngNP.shape[0],1):
    for j in range(0,pngNP.shape[1],1):
        if(labelMap[i,j] == 1):
            png[i,j,0] = 255

png[seedPoint[0],seedPoint[1]] = [0,0,255,255]

plt.imshow(png)
plt.show()
        

