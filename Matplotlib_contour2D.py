########################################################################
# Name:
#	Matplotlib_contour2D
#-----------------------------------------------------------------------
# Description:
#	Single contour plot for the specific data at the given time.
########################################################################

import sys							#Python 2.7 Standard Library
import numpy as np 					#NumPy 1.11.1
import matplotlib.pyplot as plt 	#matplotlib 1.5.1

### Input ##############################################################
#Give the file name (Absolute or relative path)
FileName="./.../....DAT"
#Give the size of data in axis-X
DataSizeX=0
#Give the size of data in axis-Y
DataSizeY=0
#Give the column number of the data (x,y,s), starting from 0
DataPosition=[0,1,2]
#Give the plot time
PlotTime=0.0
#Give the contour levels
PlotLevel=10
#Give the minimum level
PlotLevelMin=0.0
#Give the maximum level
PlotLevelMax=1.0
#Give the plot title
PlotTitle='A Title'
### End Input ##########################################################

#Function for read the data file
def _ReadData(filename,plottime):
	DataMark=0		#0=Read temp data
					#1=Read plot data
	DataTemp=[]		#List to store the temp data
	DataSave=[]		#List to store the plot data

	for line in open(filename,'r'):
		if(DataMark==0 and line[0]=='#'):	#Read time data
			#Extract the line data to a list
			DataTemp=map(str,line.split())
			#Get the time for the current set of data
			ReadTime=float(DataTemp[4])
			if(ReadTime==plottime):		#Set DataMark=1 when right time
				DataMark=1
			continue	#Continue to the next line
		if(DataMark==1):	#Read data
			if(line[0]==' '):	#Read while the current line is data
				#Extract and append the line data to a list
				DataSave.append(map(str,line.split()))
			else:				#Stop reading when getting right data
				break
	#Turn the list to a NumPy array and then return it as the output
	return np.array(DataSave,dtype=np.float32)

#-----------------------------------------------------------------------
#Read the plot data
PlotData=_ReadData(FileName,PlotTime)

#Get the data in axis-X
X=PlotData[:,DataPosition[0]]
#Get the data in axis-Y
Y=PlotData[:,DataPosition[1]]
#Get the data for contour
S=PlotData[:,DataPosition[2]]

#Generate the mesh data according to the data size
x=X.reshape(DataSizeY,DataSizeX)
y=Y.reshape(DataSizeY,DataSizeX)
s=S.reshape(DataSizeY,DataSizeX)
#-----------------------------------------------------------------------
#Assign the levels of the contour plot
PlotLevelAtrribute=np.linspace(PlotLevelMin,PlotLevelMax,PlotLevel)
#Set up a figure
plt.figure("Matplotlib Contour")
#Plot the contour
CS=plt.contourf(x,y,s,levels=PlotLevelAtrribute,extend='both')
#Assign the plot title
plt.title(PlotTitle+'(t='+str(PlotTime)+'s)')
#Assign the axis-X label
plt.xlabel("x")
#Assign the axis-Y label
plt.ylabel("y")
#Show the color bar for the contour
plt.colorbar()
#-----------------------------------------------------------------------
#Show the plot figure in Matplotlib window
plt.show()
#Save the plot figure as a ".jpg" file in the given path
#plt.savefig("./.../"+PlotTitle+'(t='+str(PlotTime)+'s)'+".jpg")