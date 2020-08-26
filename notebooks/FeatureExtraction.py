"""
Feature extraction class to implement the following functions
1)rolling mean
2)variance
3)standard deviation
4)skewness & kurtosis

"""
import numpy as np
from readcsv import readcsv
import matplotlib.pyplot as plt

class featureextraction:

	def __init__(self,df):
		"""
		Performs implementation of functions specified in the function 1

		:param None

		"""
		if(len(df)==0):
			print("Please enter a valid dataframe")
			return None 
		else:
			self.df = df


		


	def rollingmean(self,n=3,showplot=0):
		"""
		Performs rolling mean on dataframe

		:params n: the window size of the rolling mean
		:params boolean showplot: if boolean is 1 displays the plotting of the dataframe(default = 1 slow plot)



		:return pandas.dataframe 

		"""
		rm =  self.df.Vibration.rolling(n).mean()
		
		if(showplot==1):
			
			plt.figure(figsize=[15,10])
			plt.grid(True)
			plt.plot(rm)
			plt.xlabel('Time')
			plt.ylabel('Amplitude')
			plt.title('Rolling mean with n {}'.format(n))
			plt.show()
		return rm



	def standarddeviation(self):
		"""
		Finds Standard Deviation on dataframe Column

		:params None

		:return float 

		"""
		return self.df.Vibration.std()


	def variance(self):
		"""
		Find Variance on dataframe Column

		:params dataframe

		:return float 

		"""
		return self.df.Vibration.var()



	def skewness(self):
		"""
		Finds the skewness of the dataframe 

		measures if the data is inclined towards either side



		:return Integer

		"""
		return self.df.Vibration.skew()


	def kurtosis(self,slowplot = 0):
		"""
		Finds the kurtosis of the data 

		:param dataframe

		:return dataframe

		"""

		return self.df.Vibration.kurtosis()









