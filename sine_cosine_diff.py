import matplotlib.pyplot as plt
import numpy as np

x= np.arange(0, 3*np.pi, 0.1)

y_sin= np.sin(x)
y_cos= np.cos(x)

plt.title("sin cos wave")

plt.plot(x,y_sin , color='green',linestyle='dotted')
plt.show()

plt.plot(x, y_cos , color='red', linestyle='dashed')
plt.show()