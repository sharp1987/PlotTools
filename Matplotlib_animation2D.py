########################################################################
# Name:
#	Matplotlib_animation2D
#-----------------------------------------------------------------------
# Description:
#	Animation contour plot for the specific data.
########################################################################

import sys							#Python 2.7 Standard Library
import numpy as np 					#NumPy 1.11.1
import matplotlib.pyplot as plt 	#matplotlib 1.5.1
import matplotlib.animation as animation

### Input ##############################################################
#Give the file name (Absolute or relative path)
FileName="./.../....DAT"
#Give the colum number of the data (x,y,s), starting from 0
DataPosition=[0,1,2]
#Give the contour levels
PlotLevel=10
#Give the minimum level
PlotLevelMin=0.0
#Give the maximum level
PlotLevelMax=1.0
#Give the plot title
PlotTitle='A Title'
#Give the size of data in axis-X
DataSizeX=0
#Give the size of data in axis-Y
DataSizeY=0
#Lines with titles and description for the whole data file
LineJumpedTitle=2
#Lines with marks and description for every time step
LineJumpedMark=3
### End Input ##########################################################

DataMark=0		#0=Jump the line
				#1=Read plot time
				#2=Read plot data
DataMarkZip=0	#0=Jump; 1=extract data
DataTemp=[]		#List to store the temp data
DataSave=[]		#List to store the plot time
DataNumber=0	#number of the dataset/time step
LineNo=0		#number of lines
#-----------------------------------------------------------------------
s=[]	#List to store the contour dataset
t=[]	#List to store the time step
#-----------------------------------------------------------------------
#Read the data file
for line in open(FileName,'r'):
	#Count the number of lines
	LineNo+=1

	#Determine the DataMark
	###Lines with titles and description for the whole data file
	if(LineNo<=LineJumpedTitle):
		DataMark=0
	###Lines with description for every time step
	if(LineNo>LineJumpedTitle+DataNumber*(LineJumpedMark+DataSizeX*DataSizeY) \
		and \
		LineNo<LineJumpedTitle+LineJumpedMark+DataNumber*(LineJumpedMark+DataSizeX*DataSizeY)):
		DataMark=0
	###Lines with marks for every time step, for getting the plot time
	if(LineNo==LineJumpedTitle+LineJumpedMark+DataNumber*(LineJumpedMark+DataSizeX*DataSizeY)):
		DataMark=1
		DataNumber+=1	#Count the number of the dataset/time step
	###Lines with data for the current time step, except the last one
	if(DataNumber>0 \
		and \
		LineNo>LineJumpedTitle+LineJumpedMark+(DataNumber-1)*(LineJumpedMark+DataSizeX*DataSizeY) \
		and \
		LineNo<LineJumpedTitle+DataNumber*(LineJumpedMark+DataSizeX*DataSizeY)):
		DataMark=2
	###Lines with data for the current time step, the last one
	if(DataNumber>0 \
		and \
		LineNo==LineJumpedTitle+DataNumber*(LineJumpedMark+DataSizeX*DataSizeY)):
		DataMark=2
		DataMarkZip=1

	#Read Data
	###Jump to the next line
	if(DataMark==0):
		continue
	###Get the plot time
	if(DataMark==1):
		#Extract the line data to a list
		DataTemp=map(str,line.split())
		#Get the time for the current set of data
		t.append(float(DataTemp[4]))
	###Get the plot data for the current time step
	if(DataMark==2):
		#Extract and append the line data to a list
		DataSave.append(map(str,line.split()))
	###Extract the data
	if(DataMarkZip==1):
		#Extract the (x,y) data, and (s) in the first time step
		if(DataNumber==1):
			#Turn the list to a NumPy array
			PlotData=np.array(DataSave,dtype=np.float32)
			#Get the data in axis-X
			X=PlotData[:,DataPosition[0]]
			#Get the data in axis-Y
			Y=PlotData[:,DataPosition[1]]
			#Get the data for contour
			S=PlotData[:,DataPosition[2]]
			#Generate the mesh data according to the data size
			x=X.reshape(DataSizeY,DataSizeX)
			y=Y.reshape(DataSizeY,DataSizeX)
			#Append the contour data to the animation list
			s.append(S.reshape(DataSizeY,DataSizeX))
			#Reset the DataMarkZip to 0
			DataMarkZip=0
			#Clear the list to store the plot data
			del DataSave[:]
		#Just extract the contour data (s)
		if(DataNumber>1):
			#Turn the list to a NumPy array
			PlotData=np.array(DataSave,dtype=np.float32)
			#Get the data for contour
			S=PlotData[:,DataPosition[2]]
			#Generate the mesh data and append it to the animation list
			s.append(S.reshape(DataSizeY,DataSizeX))
			#Reset the DataMarkZip to 0
			DataMarkZip=0
			#Clear the list to store the plot data
			del DataSave[:]

#-----------------------------------------------------------------------
#Set up a figure
fig=plt.figure(PlotTitle)
ax=plt.axes()
#Assign the levels of the contour plot
PlotLevelAtrribute=np.linspace(PlotLevelMin,PlotLevelMax,PlotLevel)
#-----------------------------------------------------------------------
#Initial function
def init():
	cont.set_data([],[],[])
	return cont,
#-----------------------------------------------------------------------
#Animation function for updating the plot
def animate(i):
	#Assign the plot data for one time step by given "i"
	z=s[i]
	#Clear the graph
	plt.clf()
	#Plot the contour
	cont=plt.contour(x,y,z,levels=PlotLevelAtrribute,extend='both')
	#Assign the plot title
	plt.title('t='+str(t[i])+'s')
	#Assign the limit in axis-X
	plt.xlim()
	#Assign the limit in axis-Y
	plt.ylim()
	#Show the color bar for the contour
	plt.colorbar()
	return cont
#-----------------------------------------------------------------------
#Animation
anim=animation.FuncAnimation(fig,animate, \
							frames=DataNumber,interval=500,repeat=False)
#-----------------------------------------------------------------------
#Show the plot figure in Matplotlib window
plt.show()
#Save the plot figure as a ".avi" file in the given path
#anim.save('./.../'+PlotTitle+'avi')