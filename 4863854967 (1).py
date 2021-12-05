import numpy as np
import matplotlib.pyplot as plt
letters=np.load("letters.npy")
er=np.array([(0,1,0),(1,1,1),(0,1,0)])
pd_lt=np.copy(letters)
pd_ls=np.copy(letters)
                   
plt.imshow(pd_lt,cmap='gray',interpolation='none')          
for t in range (1,30):
   for r in range (1,60):
       x=letters[t-1:t+2,r-1:r+2]
       for y in range (0,3):
           for z in range (0,3):
               if (er[y,z]==1 and x[y,z]==1):
                   pd_ls[t,r]=1            
                   
plt.imshow(pd_ls,cmap='gray',interpolation='none')
