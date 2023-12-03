import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('./straightDiamond_76100/postProcessing/forceCoeffs/0/forceCoeffs.dat', skiprows=0)
data2 = np.loadtxt('./straightDiamond_7.61e5/postProcessing/forceCoeffs/0/forceCoeffs.dat', skiprows=0)
data3 = np.loadtxt('./straightDiamond_1.9e6/postProcessing/forceCoeffs/0/forceCoeffs.dat', skiprows=0)
data4 = np.loadtxt('./straightDiamond_3.044e6/postProcessing/forceCoeffs/0/forceCoeffs.dat', skiprows=0)

# use this to understand the forceCoeffffs file: https://www.openfoam.com/documentation/guides/latest/doc/guide-fos-forces-force-coeffs.html
plt.title("Drag Coefficeient Comparison wrt Reynolds Number")
#plt.plot(data1[:,0],data1[:,2],label='Re = 76100')
mean_Drag =[float(np.mean(data2[:,2])),float(np.mean(data3[:,2])),float(np.mean(data4[:,2]))]
Re = [0.8,2,3]
plt.plot(Re,mean_Drag)
plt.title("Re v/s Mean_Drag")
#plt.plot(data2[:,0],data2[:,2],label='Re = 7.61e5')
#plt.plot(data3[:,0],data3[:,2],label='Re = 1.9e6')
#plt.plot(data4[:,0],data4[:,2],label='Re = 3.044e6')
plt.xlabel('Reynolds Number (1×10⁶)')
plt.ylabel('Mean Drag')
#plt.legend()
plt.grid() 
plt.show()

#plt.title("Lift Coefficeient Comparison wrt Reynolds Number")
##plt.plot(data1[:,0],data1[:,3],label='Re = 76100')
#plt.plot(data2[:,0],data2[:,3],label='Re = 7.61e5')
#plt.plot(data3[:,0],data3[:,3],label='Re = 1.9e6')
#plt.plot(data4[:,0],data4[:,3],label='Re = 3.044e6')
#plt.xlabel('time (s)')
#plt.legend()
#plt.grid() 
#plt.show()
plt.title("Lift Coefficeient Comparison wrt Reynolds Number")
mean_Lift =[float(np.mean(data2[:,3])),float(np.mean(data3[:,3])),float(np.mean(data4[:,3]))]
Re = [0.8,2,3]
plt.plot(Re,mean_Lift)
plt.title("Re v/s Mean_Lift")
plt.xlabel('Reynolds Number (1×10⁶)')
plt.ylabel('Mean Lift')
plt.grid() 
plt.show()
