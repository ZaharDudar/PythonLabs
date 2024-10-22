import matplotlib.pyplot as plt
import numpy as np
dataRow = []

with open("./2step.dat", 'r') as f:
    for line in f.readlines():
        dataRow.append([float(i) for i in line.strip().split()])
    
data = []
maxX = 0
minX = 0
maxY = 0
minY = 0
for dot_id in range(len(dataRow)//2):
    data_x = dataRow[2*dot_id]
    data_y = dataRow[2*dot_id+1]
    maxX = max(max(data_x), maxX) 
    minX = min(min(data_x), minX) 
    maxY = max(max(data_y), maxY) 
    minY = min(min(data_y), minY) 
    data.append([data_x, data_y])


maxX = int(maxX)+2
minX = int(minX)-1
maxY = int(maxY)+2
minY = int(minY)-1

for curve in range(len(data)):
    plt.plot(data[curve][0], data[curve][1])
    plt.xticks(np.arange(minX, maxX, 1))
    plt.yticks(np.arange(minY, maxY, 1))
    # plt.yticks(np.arange(int(min(data[curve][1])), int(max(data[curve][1]))+1, 1))
    plt.grid()
    plt.title(f"Frame {curve}")
    plt.savefig(f"./2ndTaskOut/frame{curve}.png")
    plt.close()