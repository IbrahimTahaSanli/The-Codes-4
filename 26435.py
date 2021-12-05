import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def histogram(data):
    hisArr = [ 0 for i in range(-4,12,1)]

    for i in range(0,len(data),1):
        for j in range(0,len(data[1]),1):
            hisArr[int(data[i][j]//(1/16))] += 1

    return hisArr
  

img = mpimg.imread('cicek.png')


hisArr = histogram(img)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.bar([ i for i in range(-4,12,1)],hisArr)

plt.show()

