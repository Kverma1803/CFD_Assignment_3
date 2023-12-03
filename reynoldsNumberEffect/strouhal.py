import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
#from matplotlib.ticker import AutoMinorLocator

data1 = np.loadtxt('./straightDiamond_76100/postProcessing/forceCoeffs/0/forceCoeffs.dat', skiprows=0)
data2 = np.loadtxt('./straightDiamond_7.61e5/postProcessing/forceCoeffs/0/forceCoeffs.dat', skiprows=0)
data3 = np.loadtxt('./straightDiamond_1.9e6/postProcessing/forceCoeffs/0/forceCoeffs.dat', skiprows=0)
data4 = np.loadtxt('./straightDiamond_3.044e6/postProcessing/forceCoeffs/0/forceCoeffs.dat', skiprows=0)
def frequency(data):
	L       = 1           # L = D - Diameter
	V       = 1           # Velocity
	time    = data[:,0]
	Cd      = data[:,2]
	Cl      = data[:,3]

	# FFT

	N       = len(time)
	dt      = time[2] - time[1]

	nmax=512                       # no. of points in the fft
	freq, Cl_amp = signal.welch(Cl, 1./dt, nperseg=nmax)
#	plt.plot(freq, Cl_amp)         
#	plt.show() 

	# # Strouhal Number
	# Find the index corresponding to max amplitude
	Cl_max_fft_idx = np.argmax(abs(Cl_amp))  
	freq_shed      = freq[Cl_max_fft_idx ]
	St             = freq_shed * L / V
	L=[freq_shed,St,freq, Cl_amp]
	return L
name = [frequency(data2),frequency(data3),frequency(data4)]
#fig, ax = plt.subplots(layout='constrained')
plt.plot(name[0][2],name[0][3],label = 'Re = 7.61e5', color = 'green')
plt.xlabel('frequency (Hz)')
plt.ylabel('Cl_Amp')
plt.legend()
plt.grid() 
plt.show()
plt.plot(name[1][2],name[1][3],label = 'Re = 1.9e6', color = 'red')
plt.plot(name[2][2],name[2][3],label = 'Re = 3.044e6',color = 'blue')   
plt.xlabel('frequency (Hz)')
plt.ylabel('Cl_Amp')
#secax = ax.secondary_yaxis('right', functions=(name[0][2],name[0][3]))      
plt.legend()
plt.grid() 
plt.show() 
#print("Vortex shedding freq: %.3f [Hz]",frequency(data1)[0])
#print("Strouhal Number: %.3f", frequency(data1)[1])

print("Vortex shedding freq: %.3f [Hz]",frequency(data2)[0])
print("Strouhal Number: %.3f", frequency(data2)[1])

print("Vortex shedding freq: %.3f [Hz]",frequency(data3)[0])
print("Strouhal Number: %.3f", frequency(data3)[1])

print("Vortex shedding freq: %.3f [Hz]",frequency(data4)[0])
print("Strouhal Number: %.3f", frequency(data4)[1])
