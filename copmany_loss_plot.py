import matplotlib.pyplot as plt 
import numpy as np

x=[11,12,13,14]
y=[15,16,17,18]

x1=[13,14,17,21]
y1=[13,16,17,20]

plt.plot(x, y, label="loss per month " , color ="red" , linestyle = "dotted" , linewidth = 5)
plt.plot(x1, y1, label="profit per moneth" , color= "blue" , linestyle = "dashed" , linewidth=6)

plt.xlabel("month")
plt.ylabel("loss/profit" , )
plt.title("company loss and profit" , color="green")
plt.legend()
plt.show()
