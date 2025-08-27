import matplotlib.pyplot as plt
import numpy as np

x =np.arange(5, 30)
y = 2*x+7

plt.title("plot")
plt.xlabel("X-axis")
plt.ylabel("y-axis")

plt.plot(x,y ,'ob' ,  markerfacecolor = 'black' )  #ob is used for circles represntattion

plt.show()