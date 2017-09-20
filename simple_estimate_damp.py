#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from damping_analyzer import Wave, Waves
from math import pi
from scipy import signal

if __name__ == '__main__':
    '''
    waves = Waves([
        Wave(freq=1.3),
        Wave(freq=7, mag=0.25)
    ])
    '''
    '''
    waves = Waves([
        Wave(freq=1,   damping_ratio=1),
        Wave(freq=1.0, damping_ratio=1),
        Wave(freq=0.2, damping_ratio=1),
    ])
    '''
    wave = Wave(undamped_freq=1, damping_ratio=0.145)
    sampling_rate = 100
    t1 = 5
    x = np.arange(0, 5, 1.0/sampling_rate)
    y = wave.ats(x)
    peakind = signal.find_peaks_cwt(y, np.arange(1,100))
    print ('peakind: {}'.format(peakind))
    print ('x[peakind]: {}'.format(x[peakind]))
    print ('y[peakind]: {}'.format(y[peakind]))
    waves = Waves([
        wave
        #Wave(undamped_freq=1.0, damping_ratio=0),
    ])
    waves.plot_indi(sampling_rate=100, t1=t1)
    #waves.plot_super(sampling_rate=100, t1=1.6)
    #waves.plot_dft()
    plt.xlabel(r'$\omega t$')
    plt.ylabel(r'$x(t)\//\/x(0)$')
    plt.axhline(y=0, linewidth=0.5, color='black')
    plt.legend()
    
    plt.savefig('peakfind.png')
    plt.show()