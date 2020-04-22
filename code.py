import pandas as pd
#import numpy as np

file_path=r'D:\DataUsage.csv'
data=pd.read_csv(file_path)

#print(data_points)
#print(data)
#data.describe()

columns=['Hour','Download','Upload']
down_data=data[columns]
data_points=int((len(data)))
usage_anytime=0
usage_nighttime=0
for i in range(data_points):
    if down_data.iloc[i,0]>=7:
        usage_anytime=usage_anytime+down_data.iloc[i,1]+down_data.iloc[i,2]
    else:
        usage_nighttime=usage_nighttime+down_data.iloc[i,1]+down_data.iloc[i,2]
        

usage_anytime=round(usage_anytime/1000,3)
usage_nighttime=round(usage_nighttime/1000,3)


    
total_usage=usage_anytime+usage_nighttime
print('Day time data usage: ', usage_anytime,'GB',sep='')
print('Night time data usage: ',usage_nighttime,'GB',sep='')
print('Total Usage: ',total_usage,'GB',sep='')
