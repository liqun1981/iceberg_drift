import pylab
import numpy as np
import matplotlib.pyplot as plt

for i in range(1,30):
    time = str(i/10.0)
    file = '/home/evankielley/OpenFOAM/evankielley-3.0.1/run/300/case308/'+ time + '/uniform/sixDoFRigidBodyMotionState'
    with open(file) as f:
        with open("centreOfRotation.txt", "a") as f1:
            for line in f:
                if "centreOfRotation" in line:
                    s = line.split('(', 1)[1].split(')')[0]
                    s1 = s.split()
                    x = float(s1[0])
                    y = float(s1[1])
                    z = float(s1[2])
                    f1.write("{} {} {} {}\n".format(time, x, y, z))

data = np.genfromtxt('/home/evankielley/OpenFOAM/evankielley-3.0.1/run/300/case308/centreOfRotation.txt', delimiter=' ', names=['t', 'x', 'y', 'z'])
plt.plot(data['t'], data['x'])
plt.plot(data['t'], data['y'])
plt.plot(data['t'], data['z'])
pylab.savefig('centreOfRotation_plot.png')
