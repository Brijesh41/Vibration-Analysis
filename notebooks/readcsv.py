"""
Module for reading the csv file

"""


import pandas as pd
import time

class readcsv():

	def __init__(self,file_path =None):
		"""
		This module returns the pandas dataframe after efficiently reading the csv in chunks

		:param file_path: str

			    the path of the csv file

		"""
		if(file_path==None):
			print("No file specified")

		self.file_path = file_path



	def getDataFrame(self,chunks=1000):
		"""
		This function loads the csv file and return pandas dataframe

		:param chunks: integer

					   specify the number of chunks in which the csv is to be loaded. Default value is 1000.

		"""

		self.chunks = chunks

		if(self.file_path==""):
			print("No file specified")
			return None

		self.df = pd.DataFrame()

		for chunk in pd.read_csv(self.file_path,chunksize = self.chunks):
			self.df = pd.concat([chunk,self.df])

		self.df.columns = ['Date','Vibration']

		self.df.Date = pd.to_datetime(self.df.Date[:])
		print(self.df.dtypes)
		return self.df

	def viewcsv(self,df=None,rows = 100):
		"""
		This function is used to view the dataframe

		:param  df: ArrayLike

					dataframe instance to view the file
					
		:param		rows: int

					 Number of rows to be displayed in the dataframe

		"""
		if(len(df)==0):
			print("df is empty")
			return None

		print(df[:rows])


