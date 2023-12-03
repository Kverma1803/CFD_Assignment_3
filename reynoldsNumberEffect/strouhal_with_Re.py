import numpy as np
import matplotlib.pyplot as plt

St = [ 0.195,0.586,0.938 ]
Re = [0.8,2,3]

plt.plot(Re,St)
plt.title('Re v/s St')
plt.grid()
plt.ylabel('Strouhal Number')
plt.xlabel('Reynolds Number (1×10⁶)')
plt.show()
