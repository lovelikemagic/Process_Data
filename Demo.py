import numpy as np
arr=np.loadtxt('./features3.txt',delimiter=' ')

print(np.shape(arr))
leftA=np.zeros([4563,1])

for i in range(0,4563):
    leftA[i,0]=i
newA=np.hstack((leftA,arr))
np.savetxt('./features3.txt',newA,delimiter=' ',fmt='%d')
