#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from damping_analyzer import Wave, Waves
from math import pi

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
    waves = Waves([
        Wave(undamped_freq=10/(2*pi), damping_ratio=1, color='black'),
        Wave(undamped_freq=10/(2*pi), damping_ratio=.5),
        Wave(undamped_freq=10/(2*pi), damping_ratio=.1),
        Wave(undamped_freq=10/(2*pi), damping_ratio=2),
        #Wave(undamped_freq=1.0, damping_ratio=0),
    ])
    ax = plt.gca()
    waves.plot_indi(ax, sampling_rate=100, t1=1.6)
    #waves.plot_super(sampling_rate=100, t1=1.6)
    #waves.plot_dft()
    ax.set_xlabel(r'$\omega t$')
    ax.set_ylabel(r'$x(t)\//\/x(0)$')
    ax.axhline(y=0, linewidth=0.5, color='black')
    ax.legend()
    
    plt.savefig('hyperphysics_similar.png')
    plt.show()