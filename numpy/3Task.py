import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.animation as animation
data=[]
with open("./data.txt", "r") as f:
    data = [float(i.strip()) for i in f.readlines()]
data = np.array(data)
fig, ax = plt.subplots()
A = np.diag([1]*len(data))
A[:,:-1]-=A[:,1:]
A[0,-1]=-1
p, = ax.plot(data)
def funk(i):
    global data
    data = data - 0.5 * A @ data
    # print((1-0.5*A)**i @ data)
    # p.set_ydata((1-0.5*A)**i @ data)
    p.set_ydata(data)
    return p

anim = animation.FuncAnimation(fig, funk, repeat=True,
                                    frames=255, interval=50)
anim.save("./3.gif", writer="imagemagick", fps=15)
# plt.show()