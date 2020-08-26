"""
Main page to use the functionality of the program

Module 1) For reading csv file. Enter the file path of the dataset (readcsv.py)

Readcsv 

		Methods
		i) readcsv
		ii) getDataFrame
		iii) Viewcsv

Module 2) Plotting the various types of data 

Module 3) For feature extractions (FeatureExtraction.py)

Feature Extraction

		Methods
		1)rolling mean
		2)variance
		3)standard deviation
		4)skewness & kurtosis


"""

from FeatureExtraction import featureextraction
from readcsv import readcsv

from vibrationanalysis import vibrationanalysis

if __name__ == "__main__":

	filepath = 'E:/twiniot/dataset/Vibration.csv'
	
	## Instance of read csv class initiated
	rc = readcsv(filepath)
	
	##Pandas dataframe
	df = rc.getDataFrame(10000)

	##View dataframe with optional parameter of passing number of rows to be displayed
	rc.viewcsv(df)

	##Feature extraction instance
	fe = featureextraction(df)

	#rolling mean
	n = 4
	print("Rolling Mean\n",fe.rollingmean(n))

	##standard Deviation

	print("Standard Deviation: ",fe.standarddeviation())

	### Variance

	print("Variance: ",fe.variance())

	##skewness

	print("skewness",fe.skewness())

	##Kurtosis
	print("kurtosis",fe.kurtosis())


	##FFT Module

	v = vibrationanalysis(df)

	v.performfft()



