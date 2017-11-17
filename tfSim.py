from scipy import signal
from scipy.signal import tf2ss, lsim, StateSpace

import matplotlib.pyplot as plt


import numpy as np

def tfSim(inputType, mag, wn, zeta, init_xdot, init_x, step_increment, endtime):
    num = [0, 0, wn**2]
    den = [1, 2*zeta*wn, wn**2]

    timesteps = np.arange(0, endtime, step_increment)

    if inputType == "sine":
        u = mag*np.sin(2*np.pi*timesteps)
    elif inputType == "step":
        u = mag*np.ones(timesteps.size)
    else:
        raise ValueException("unrecognized input type")

    [A,B,C,D] = tf2ss(num,den)
    sys = StateSpace(A, B, C, D)
    print("C: {} ; shape: {}".format(C,C.shape))
    
    init_xdot = init_xdot / C[0][1]
    init_x = init_x / C[0][1]
    
    init_cond = np.array([init_xdot,init_x])
    print(init_cond)
    print("initial conditions shape: {}".format(init_cond.shape))

    y = lsim(sys, u, timesteps, init_cond )

    return y

if __name__ == "__main__":
    mag = 20
    w_n = 2*np.pi*3
    zeta = 0.00
    init_x = 20
    init_xdot = 1
    step_increment = 0.01
    endtime = 10

    y = tfSim("step", mag, w_n, zeta, init_xdot, init_x, step_increment, endtime)
    plt.plot(y[0], y[1])

    plt.plot((y[0] - ((y[0][1]-y[0][0])/2))[1:] , np.diff(y[1])/np.diff(y[0]) )
    plt.grid(True)
    plt.show()

