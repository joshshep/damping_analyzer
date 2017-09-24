#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from damping_analyzer import Wave, Waves
from math import pi

if __name__ == '__main__':
    waves = Waves([
        Wave(undamped_freq=1), # energy is proportional to freq^2 * mag^2
        Wave(undamped_freq=20, mag=1.0/20, phase=pi/2), #same energy
        #Wave(undamped_freq=1.0, damping_ratio=0),
    ])
    # Nyquist's sampling theorem dictates that for a given sample rate only
    # frequencies up to half the sample rate can be accurately measured
    # https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem
    ax = plt.gca()
    waves.plot_dft(ax, sampling_rate=15, t1=7)
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Amplitude')
    ax.axhline(y=0, linewidth=0.5, color='black')
    ax.legend()
    
    ax.grid()
    
    plt.savefig('fft.png')
    plt.show()