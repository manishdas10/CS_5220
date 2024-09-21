import numpy as np
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt

plt.style.use('~/modified.mplstyle')

file1 = 'timing-basic.csv'
file2 = 'timing-blocked.csv'
file3 = 'timing-blas.csv'

files = [file1]

# x1,x2,x3 = [],[],[]
# y1,y2,y3 = [],[],[]

data_all = []

for file in files:

    data = pd.read_csv(file)
    data_all.append(data)

data1 = data_all[0]
#data2 = data_all[1]
#data3 = data_all[2]

plt.figure(figsize = (10,6))
plt.plot(data1['size'],data1['mflop']/1000,color='b',linewidth=1.5,label = 'Basic')
#plt.plot(data2['size'],data2['mflop']/1000,color='r',linewidth=1.5,label = 'Blocked')
#plt.plot(data3['size'],data3['mflop']/1000,color='g',linewidth=1.5,label = 'Blas')

plt.legend(fontsize=20)
plt.tight_layout()
plt.savefig('timings1_all.jpg',dpi=500)

#plt.figure(figsize = (10,6))
#plt.plot(data1['size'],data1['mflop']/1000,color='b',linewidth=1.5,label = 'Basic')
#plt.plot(data2['size'],data2['mflop']/1000,color='r',linewidth=1.5,label = 'Blocked')
#plt.plot(data1['size'],data1['mflop']/1000,color='g',linewidth=1.5,label = 'Blas')

