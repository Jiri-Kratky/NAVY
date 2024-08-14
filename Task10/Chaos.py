import matplotlib.pyplot as plt
import numpy as np

a_values = np.linspace(1, 4, 100000)
m = 0.005       # Initial value
X = []
Y = []

for value in a_values:
    X.append(value)
    m = value*m*(1-m)
    Y.append(m)

plt.plot(X,Y,ls='',marker=',')
plt.savefig('Chaos.png',dpi=600)
plt.show()
