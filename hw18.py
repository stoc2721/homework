import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('data_tasks.csv')
print(df)
print(df.values[:,1])
timePoint=df.values[:,0]
temp=df.values[:,1]
stDev=df.values[:,2]
plt.figure(1)
plt.errorbar(timePoint,temp,yerr=stDev,fmt="r8--",linewidth=2,elinewidth=0.75,ecolor='k',capsize=3,capthick=1)
plt.legend(["Temperature with Standard Deviation"],numpoints=1,loc=("upper left"))
plt.xlim((0,10))
plt.xticks([1,2,3,4,5,6,7,8,9])
plt.yticks([0,5,10,15,20])
plt.title("Temperature Over Time",fontsize=24)
plt.xlabel('Time(Minutes)',fontweight = 'bold')
plt.ylabel('Temperature (C)', fontweight = 'bold')
plt.show()
#plt.savefig('filename.png',dpi=600)

plt.figure(2)
plt.bar(timePoint,temp,yerr=stDev,align="center",ecolor='k',capsize=8)
plt.xticks([1,2,3,4,5,6,7,8,9])
plt.yticks([0,5,10,15,20])
plt.title("Temperature Over Time",fontsize=24)
plt.xlabel('Time(Minutes)',fontweight = 'bold')
plt.ylabel('Temperature (C)', fontweight = 'bold')
plt.show()
#plt.savefig('filename.png',dpi=600)

#### accidently split the file when I turned it into a csv, so have to read in twice, one for each sheet. This can be fixed by adding df=pd.read_excel('data_task.xlsx',sheet_name=...)
dr=pd.read_csv('data_tasks2.csv')
print(dr)
def strToInt(lst):
    newLst=[]
    for i in lst:
        i = int(i)
        newLst.append(i)
    return newLst
time=strToInt(dr.values[1:,0])
lvTemp=strToInt(dr.values[1:,1])
lvStDev=strToInt(dr.values[1:,2])
dgTemp=strToInt(dr.values[1:,3])
dgStDev=strToInt(dr.values[1:,4])
dTemp=strToInt(dr.values[1:,5])
dStDev=strToInt(dr.values[1:,6])
plt.figure(3)
plt.errorbar(time,lvTemp,yerr=lvStDev,fmt="r8--",linewidth=2,elinewidth=0.75,ecolor='k',capsize=3,capthick=1)
plt.errorbar(time,dgTemp,yerr=dgStDev,fmt="g8--",linewidth=2,elinewidth=0.75,ecolor='k',capsize=3,capthick=1)
plt.errorbar(time,dTemp,yerr=dStDev,fmt="b8--",linewidth=2,elinewidth=0.75,ecolor='k',capsize=3,capthick=1)
plt.legend(["Las Vegas","Durango","Denver"],numpoints=2,loc=("upper left"))
plt.xlim((0,7))
plt.xticks([1,2,3,4,5,6])
plt.yticks([0,5,10,15,20,25,30,35,40,45,50])
plt.title("Temperature Over Time",fontsize=24)
plt.xlabel('Time(Hours)',fontweight = 'bold')
plt.ylabel('Temperature (C)', fontweight = 'bold')
plt.show()
#plt.savefig('filename.png',dpi=600)
plt.figure(4)
barWidth = 0.25
r1= np.arange(len(lvTemp))
r2= [x+barWidth for x in r1]
r3= [x+barWidth for x in r2]
plt.bar(r1,lvTemp, color='#7f6d5f', width = barWidth, edgecolor = 'white', label = 'Las Vegas',yerr=lvStDev,capsize=5)
plt.bar(r2,dgTemp, color='#557f2d', width = barWidth, edgecolor = 'white', label = 'Durango',yerr=dgStDev,capsize=5)
plt.bar(r3,dTemp, color='#2d7f5e', width = barWidth, edgecolor = 'white', label = 'Denver',yerr=dStDev,capsize=5)
plt.title('Temperature Over Time', fontsize=24)
plt.xlabel('Time(Hours)',fontweight='bold')
plt.ylabel('Temperature (C)', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(lvTemp))],[1,2,3,4,5,6])
plt.legend()
plt.show()
#plt.savefig('filename.png',dpi=600)





