"""

Vibration Analysis

Implementation Fast Fourier Transformation


## Reference: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.stft.htm
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy import signal
from readcsv import readcsv
import datetime
import time
from scipy.signal import stft


class vibrationanalysis:

	def __init__(self,df):
		"""

			param: df : Pandas.DataFrame

		"""
		self.df = df

	def plotbeforefft(self):
		"""

			Plotting of the Actual Data 

		"""
		self.time = self.df.Date
		self.Vibration = self.df.Vibration

		plt.figure(figsize= (10,10))
		plt.plot(self.time,self.Vibration)
		plt.xlabel("Time")
		plt.ylabel("Amplitude")

		plt.title("Original Vibration Data")

		plt.show()


	

	def _time_milliseconds(self,Datetime):
		"""
		params: TimeStamp : DateTime


		return: Float (Milliseconds)

		"""

		epoch = datetime.datetime.utcfromtimestamp(0)
		
		return (Datetime - epoch).total_seconds()





	def performfft(self):
		"""
		Performs Fast Fourier Transform and plotting of the graph

		"""


		self.time = self.df.Date
		self.Vibration = self.df.Vibration

		
		N = np.int(np.prod(self.time.shape))
		t1 = self._time_milliseconds(self.df.Date[1])
		t0 = self._time_milliseconds(self.df.Date[0])

		Fs = int(1/(t1-t0)) 	
		T = 1/Fs;
		

		print("N",N)
		print("F {} Hertz".format(Fs))
		print("T {} sec".format(T))

		plt.figure(figsize = (10,10))  
		xf = np.linspace(0, int(1/(2*T)), int(N/2))

		yf = fft(self.Vibration.to_numpy())
		plt.plot(xf, 2.0/N * np.abs(yf[0:np.int(N/2)]))

		plt.xlabel('Frequency (Hz)')
		plt.ylabel('Amplitude')
		plt.title('Fast Fourier Transformation')
		plt.show()


		return yf


	def Short_time_fast_frequency(self,fs=100,nperseg=100,window='hann',cmap='plasma'):

		"""

		params: fs, integer(Optional)

				sampling frequency(Hertz)

		params: nperseg, integer(Optional)

				Length of segment
		
		params: Window, str(Optional)

				(Hann Default)
		
		params: cmap, str(Optional)
				color of heatmap


		"""


		f, t, Z = stft(self.df.Vibration, fs, window=window,nperseg=nperseg)

		plt.pcolormesh(t, f, np.abs(Z)*1000, cmap=cmap)
		plt.title('STFT Magnitude')
		plt.ylabel('Frequency [Hz]')
		plt.xlabel('Time [sec]')
		plt.show()

		return f,t,Z












