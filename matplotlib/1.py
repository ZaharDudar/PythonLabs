import matplotlib.pyplot as plt
import numpy as np
data = []

with open("./dead_moroz/001.dat", 'r') as f:
    N = int(f.readline().strip())
    for line in f.readlines():
        data += [float(i) for i in line.strip().split()]

data = data[0:N]
data = np.resize(np.array(data), (len(data)//2,2))
print(data)
rangeX = max(data[:,0]) - min(data[:,0])
rangeY = max(data[:,1]) - min(data[:,1])
mRange = max(rangeY, rangeX)
Size = 20
rangeX = rangeX/mRange * Size
rangeY = rangeY/mRange * Size

plt.figure(figsize=(rangeX, rangeY),dpi=300)
plt.plot(data[:,0],data[:,1],"o")

plt.savefig("./test.png")