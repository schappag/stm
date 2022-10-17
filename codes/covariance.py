import numpy as np
import matplotlib.pyplot as plt


s = np.matrix([[0,1,2],
              [0,-1,-2]])
x1 = s[0,:].mean()
x2 = s[1,:].mean()

std_x1 = s[0,:].std()
std_x2 = s[1,:].std()

print('Mean x:'+str(x1)+', STD x:'+str(std_x1))
print('Mean y:'+str(x2)+', STD y:'+str(std_x2))

plt.plot(s[0,:],s[1,:],
         color='b',
         marker='o')
plt.show()
rows, columns = s.shape

M = np.multiply((s[0,:]-x1),(s[1,:]-x2))

cov = sum(M.transpose())/(columns-1)
print(f'Covariance = {cov} ')
