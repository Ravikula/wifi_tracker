#IMPORT LIBRARIES 

import pandas as pd
import numpy as np

#Importing data set

file_path=r'D:\DataUsage.csv'
data=pd.read_csv(file_path)

        #Describing data
#print(data_points)
#print(data)
#data.describe()



columns=['Hour','Download','Upload']                                #extracting necessary columns
down_data=data[columns]
data_points=int((len(data)))

usage_anytime=0                                                     #variables to store total data amount
usage_nighttime=0

          #GETTING THE SUM OF NIGHT AND DAY TIMR DATA SEPERATELY USING iloc FUNCTION
          #Here data is seperated as day and night using the hour. If hour is >7 then its considerd as day time. If the hour is <7 its
          #it's considerd night. According to that, sum is calculated in the for loop

for i in range(data_points):
    if down_data.iloc[i,0]>=7:
        usage_anytime=usage_anytime+down_data.iloc[i,1]+down_data.iloc[i,2]
    else:
        usage_nighttime=usage_nighttime+down_data.iloc[i,1]+down_data.iloc[i,2]
        
          #Getting the giga byte value rounded up to three decimal places.
        
usage_anytime=round(usage_anytime/1000,3)
usage_nighttime=round(usage_nighttime/1000,3)

#PRINTING OUT RESULTS
    
total_usage=usage_anytime+usage_nighttime
print('Day time data usage: ', usage_anytime,'GB',sep='')
print('Night time data usage: ',usage_nighttime,'GB',sep='')
print('Total Usage: ',total_usage,'GB',sep='')

