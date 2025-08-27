import matplotlib.pyplot as plt
import numpy as np

x =np.arange(5, 30)
y = 2*x+7

plt.title("plot")
plt.xlabel("X-axis")
plt.ylabel("y-axis")

s=plt.plot(x,y ,'s' ,  markerfacecolor = 'black' )  # s for square
p=plt.plot(x,y ,'+' ,  markerfacecolor = 'black' ) # + means plus sign
o=plt.plot(x,y ,'ob' ,  markerfacecolor = 'black' ) #ob represnt circle 


#ob is used for circles represntattion

plt.show()