import sys
import pylab
import numpy as np
import matplotlib.pyplot as plt

'''
try:
    case_id = str(sys.argv[1])
except IndexError:
    case_id = "error"
    print ("argument 1 = case_id & argument 2 = end_time")
try:
    end_time = float(sys.argv[2])
except IndexError:
    end_time = 0.0;
    print ("argument 1 = case_id & argument 2 = end_time")
'''

case_id = str(sys.argv[1])
end_time = float(sys.argv[2])

def get_data( variable):
    count = 0
    with open("{}_{}_data.txt".format(case_id, variable), "a") as f1:
        for i in np.arange(0.1, end_time, 0.1):
            count += 1
            time = i
            if count % 10 == 0:
                time = int(time)
            time = str(time)
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


def make_plot(variable):

    data = np.genfromtxt('/home/evankielley/OpenFOAM/evankielley-3.0.1/run/300/{}/{}_{}_data.txt'.format(case_id, case_id, variable), delimiter=' ', names=['t', 'x', 'y', 'z'])
    plt.plot(data['t'], data['x'], 'k--', label='x')
    plt.plot(data['t'], data['y'], 'k:', label='y')
    plt.plot(data['t'], data['z'], 'k', label='z')
    plt.xlabel('time (s)')
    plt.ylabel('{}'.format(variable))
    legend = plt.legend(loc='upper center', shadow=True)

    # The frame is matplotlib.patches.Rectangle instance surrounding the legend.
    frame = legend.get_frame()
    frame.set_facecolor('0.90')

    # Set the fontsize
    for label in legend.get_texts():
        label.set_fontsize('large')

    for label in legend.get_lines():
        label.set_linewidth(1.5)  # the legend line width
    pylab.savefig('{}_{}_plot.png'.format(case_id, variable))
    plt.cla()  # clears subplots


if __name__ == "__main__":
    
    get_data("centreOfRotation")
    make_plot("centreOfRotation")

    get_data("velocity")
    make_plot("velocity")

    get_data("acceleration")
    make_plot("acceleration")
