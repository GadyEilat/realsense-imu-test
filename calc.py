import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_counter=1
#i=0           
#for p in Path('Proccessed Data').glob('*.csv'):
with open('Proccessed Data\Proccessed_41.csv', mode='r') as csv_file:
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
    ax_test=[]
    ay_test=[]
    az_test=[]
    for line in csv_reader:
        if (line_count<10):
            line_count+=1
        else:
            ax_test.append(float(line[4]))
            ay_test.append(float(line[5]))
            az_test.append(float(line[6]))
    line_count=0
    ax_avg=np.average(ax_test)
    ay_avg=np.average(ay_test)
    az_avg=np.average(az_test)
    csv_file.seek(0)
    for line in csv_reader:
    #skip first 10 rows.
        if (line_count==9):
            proccessed_data_timeStamp[line_count]=float(line[0])
        if (line_count>=10):
            #ax = np.array((float)(line[4])) - (float)(line[4]).mean()
            proccessed_data_timeStamp[line_count]=float(line[0])
            dt =  (proccessed_data_timeStamp[line_count]-proccessed_data_timeStamp[line_count-1])/1000000
            v0x = v0x + (float(line[4])-ax_avg)*dt
            vx.append(v0x)
            v0y = v0y + (float(line[5])-ay_avg)*dt
            vy.append(v0y)
            v0z = v0z + (float(line[6])-az_avg)*dt
            vz.append(v0z)
        line_count+=1
    proccessed_data_timeStamp2=proccessed_data_timeStamp[10:]
    vx = np.array(vx)
    plt.plot(proccessed_data_timeStamp2[250:],vx[250:])
    plt.title("Velocity in X-direction(m/s)")
    plt.xlabel("time step")
    plt.ylabel("Velocity")
    plt.show()
    vy = np.array(vy)
    plt.plot(proccessed_data_timeStamp2[250:],vy[250:])
    plt.title("Velocity in Y-direction(m/s)")
    plt.xlabel("time step")
    plt.ylabel("Velocity")
    plt.show()
    vz = np.array(vz)
    plt.plot(proccessed_data_timeStamp2[250:],vz[250:])
    plt.title("Velocity in Z-direction(m/s)")
    plt.xlabel("time step")
    plt.ylabel("Velocity")
    plt.show()
    file_counter+=1
    