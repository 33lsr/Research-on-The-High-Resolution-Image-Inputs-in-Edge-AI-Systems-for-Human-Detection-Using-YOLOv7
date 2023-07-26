'''

import matplotlib.pyplot as plt
import numpy as np
 
x = []
y = []
z1 = np.polyfit(x, y, 3) #拟合
p1 = np.poly1d(z1) 
y_pre = p1(x)
 
plt.plot(x,y,'.')
plt.plot(x,y_pre)
plt.xlabel("human_size(pixels)")
plt.ylabel("AP")
plt.show()
