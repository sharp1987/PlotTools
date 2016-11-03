########################################################################
# Name:
#	Matplotlib_plot
#-----------------------------------------------------------------------
# Description:
#	Comparison of different results from different models.
########################################################################

import sys							#Python 2.7 Standard Library
import numpy as np 					#NumPy 1.11.1
import matplotlib.pyplot as plt 	#matplotlib 1.5.1

### Input ##############################################################
#Lines with titles and descriptions should be jumped until the real data
LineJumped=2

#-----------------------------------------------------------------------
#First set of plot data
#Give the file name (Absolute or relative path)
FileName1="./.../....DAT"
#Give the column number of the data (x,y), starting from 0
DataPosition1=[0,1]

#Second set of plot data
#Give the file name (Absolute or relative path)
FileName2="./.../....DAT"
#Give the column number of the data (x,y), startinf from 0
DataPosition2=[0,1]

#Additional set of plot data can be added here according to the above
#-----------------------------------------------------------------------

#Give the curve label, ordered by the file name above
PlotLabel=['Label 1','Label 2']
#Give the plot title
PlotTitle='A Title'
### End Input ##########################################################

#Function for read the data file
def _ReadData(filename,linejumped):
	DataTemp=[]		#List to store the data
	LineNo=0		#Line number
	for line in open(filename,'r'):
		LineNo+=1	#Count the line
		if(LineNo>linejumped):	#Read data when reaching the data line
			#Extract and append the line data to a list
			DataTemp.append(map(str,line.split()))
	#Turn the list to a NumPy array and then return it as the output
	return np.array(DataTemp,dtype=np.float32)

#-----------------------------------------------------------------------
#Read the first set of plot data
data1=_ReadData(FileName1,LineJumped)
#Read the second set of plot data
data2=_ReadData(FileName2,LineJumped)

#Additional reading data can be added here according to the above
#-----------------------------------------------------------------------

#Set up a figure
plt.figure("Matplotlib: Comparison")
#-----------------------------------------------------------------------
#Plot the first set of plot data
plt.plot(data1[:,DataPosition1[0]],data1[:,DataPosition1[1]], \
	label=PlotLabel[0])
#Plot the second set of plot data
plt.plot(data2[:,DataPosition2[0]],data2[:,DataPosition2[1]], \
	label=PlotLabel[1])

#Additional plot can be added here according to the above
#-----------------------------------------------------------------------
#Assign the plot title
plt.title(PlotTitle)
#Assign the axis-x label
plt.xlabel('t')
#Assign the axis-y label
plt.ylabel('f(t)')
#Assign the limit of axis-x
plt.xlim()
#Assign the limit of axis-y
plt.ylim()
#Grid on
plt.grid()
#Legend on
plt.legend()
#-----------------------------------------------------------------------
#Show the plot figure in Matplotlib window
plt.show()
#Save the plot figure as a ".jpg" file in the given path
#plt.savefig("./.../"+PlotTitle+".jpg")