import csv
import pandas as pd
import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt

file_counter=1
#i=0           
#for p in Path('Proccessed Data').glob('*.csv'):
with open('Proccessed Data\Proccessed_51.csv', mode='r') as csv_file:
#with p.open() as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    row_count= len(list(csv_reader))
    csv_file.seek(0) #return to the start of the file.
    path=csv_file.name
    proccessed_data_timeStamp=[0]*row_count
    vx = []
    vy = []
    vz = []
    v0x = 0
    v0y = 0
    v0z = 0
    line_count = 0
    for line in csv_reader:
        if (line_count==9):
            proccessed_data_timeStamp[line_count]=float(line[0])
        if (line_count>=10):
            proccessed_data_timeStamp[line_count]=float(line[0])
            dt =  (proccessed_data_timeStamp[line_count]-proccessed_data_timeStamp[line_count-1])/1000000
            v0x = v0x + float(line[4])*dt
            vx.append(v0x)
            v0y = v0y + float(line[5])*dt
            vy.append(v0y)
            v0z = v0z + float(line[6])*dt
            vz.append(v0z)
        line_count+=1
    proccessed_data_timeStamp2=proccessed_data_timeStamp[10:]
    vx = np.array(vx)
    plt.plot(vx,proccessed_data_timeStamp2)
    plt.title("Velocity in X-direction(m/s)")
    plt.xlabel("time step")
    plt.ylabel("Velocity")
    plt.show()
    vy = np.array(vy,proccessed_data_timeStamp2)
    plt.plot(vy)
    plt.title("Velocity in Y-direction(m/s)")
    plt.xlabel("time step")
    plt.ylabel("Velocity")
    plt.show()
    vz = np.array(vz,proccessed_data_timeStamp2)
    plt.plot(vz)
    plt.title("Velocity in Z-direction(m/s)")
    plt.xlabel("time step")
    plt.ylabel("Velocity")
    plt.show()
    file_counter+=1
    