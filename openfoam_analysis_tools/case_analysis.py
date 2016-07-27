import pylab
import numpy as np
import matplotlib.pyplot as plt


def get_data(case_id, end_time, variable):

    with open("{}_{}_data.txt".format(case_id, variable), "a") as f1:
        for i in np.arange(0.1, end_time, 0.1):
            time = str(i)
            file = '/home/evankielley/OpenFOAM/evankielley-3.0.1/run/300/{}/{}/uniform/sixDoFRigidBodyMotionState'.format(case_id, time)
            with open(file) as f:
                for line in f:
                    if variable in line:
                        s = line.split('(', 1)[1].split(')')[0]
                        s1 = s.split()
                        x = float(s1[0])
                        y = float(s1[1])
                        z = float(s1[2])
                        f1.write("{} {} {} {}\n".format(time, x, y, z))

def make_plot(case_id, variable):

    data = np.genfromtxt('/home/evankielley/OpenFOAM/evankielley-3.0.1/run/300/{}/{}_{}_data.txt'.format(case_id, case_id, variable), delimiter=' ', names=['t', 'x', 'y', 'z'])
    plt.plot(data['t'], data['x'])
    plt.plot(data['t'], data['y'])
    plt.plot(data['t'], data['z'])
    pylab.savefig('{}_{}_plot.png'.format(case_id, variable))
    plt.cla()  # clears subplots

if __name__ == "__main__":
    
    get_data("case308", 3.0, "centreOfRotation")
    make_plot("case308", "centreOfRotation")

    get_data("case308", 3.0, "velocity")
    make_plot("case308", "velocity")

    get_data("case308", 3.0, "acceleration")
    make_plot("case308", "acceleration")
