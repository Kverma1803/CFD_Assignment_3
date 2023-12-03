import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('./straightDiamond_6397/postProcessing/forceCoeffs/0/forceCoeffs.dat', skiprows=0)
data2 = np.loadtxt('./straightDiamond_8711/postProcessing/forceCoeffs/0/forceCoeffs.dat', skiprows=0)
data3 = np.loadtxt('./straightDiamond_14708/postProcessing/forceCoeffs/0/forceCoeffs.dat', skiprows=0)
data4 = np.loadtxt('./straightDiamond_25879/postProcessing/forceCoeffs/0/forceCoeffs.dat', skiprows=0)

# use this to understand the forceCoeffffs file: https://www.openfoam.com/documentation/guides/latest/doc/guide-fos-forces-force-coeffs.html

plt.plot(data1[:,0],data1[:,3],label='N = 6397')
# plt.plot(data2[:,0],data2[:,3],label='N = 8711')
plt.plot(data3[:,0],data3[:,3],label='N = 14708')
# plt.plot(data4[:,0],data4[:,3],label='N = 25879')
plt.xlabel('time (s)')
plt.legend()
plt.grid() 
plt.show()
