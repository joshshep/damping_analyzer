#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from damping_analyzer import Wave, Waves
from math import pi
from scipy import signal
import matplotlib.gridspec as gridspec

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
    x = np.arange(0, t1, 1.0/sampling_rate)
    y = wave.ats(x)
    peakind = signal.find_peaks_cwt(y, np.arange(1,100))
    print ('peakind: {}'.format(peakind))
    print ('x[peakind]: {}'.format(x[peakind]))
    print ('y[peakind]: {}'.format(y[peakind]))
    
    x_fmt_gen_eq = r'$x(t) = A e^{-\omega_0 \zeta t} \cos( \omega_d t )$'

    #############
    # UNDERdamped x'(t)
    #fmt_gen_eq = r'$\dot{x}(t) = -\omega_0 \zeta A e^{-\omega_0 \zeta t} \cos( \omega_0 \sqrt{1-\zeta^2} t ) - \omega_0 \sqrt{1-\zeta^2} A e^{-\omega_0 \zeta t} \sin( \omega_0 \sqrt{1-\zeta^2} t )$'
    #fmt_gen_eq = r'$\dot{x}(t) = -\omega_0 A e^{-\omega_0 \zeta t} (\zeta \cos( \omega_0 \sqrt{1-\zeta^2} t ) + \omega_0 \sqrt{1-\zeta^2} \sin( \omega_0 \sqrt{1-\zeta^2} t ))$'
    #fmt_gen_eq = r'$\dot{x}(t) = -\omega_0 A e^{-\omega_0 \zeta t} (\zeta \cos( \omega_d t ) + \omega_d \sin( \omega_d t ))$'
    
    xdot_fmt_gen_eq = r'$\dot{x}(t) = -\omega_0 A e^{-\omega_0 \zeta t} (\zeta \cos( \omega_d t ) + \omega_d \sin( \omega_d t ))$'
    
    #############
    # UNDERdamped x(t)
    #fmt_gen_eq = r'$x(t) = A e^{-\omega_0 \zeta t} \cos( \omega_0 \sqrt{1-\zeta^2} t )$'
    
    #############
    # OVERdamped x(t)
    #fmt_gen_eq = r'$ A e^{- \frac{1}{\zeta} t} $'
    
    gs0 = gridspec.GridSpec(2,1)
    tPlot, axes = plt.subplots(nrows=2, ncols=1, sharex=True)
    
    freqs = [0.5, 1, 1.5, 2, 2.5, 3, 3.3, 4, 5, 8]
    
    for undamped_freq in freqs:
        
        waves = Waves([
            Wave(undamped_freq=undamped_freq, damping_ratio=0),
            Wave(undamped_freq=undamped_freq, damping_ratio=0.05),
            Wave(undamped_freq=undamped_freq, damping_ratio=0.2),
            Wave(undamped_freq=undamped_freq, damping_ratio=0.5),
            Wave(undamped_freq=undamped_freq, damping_ratio=0.8)
            #Wave(undamped_freq=1.0, damping_ratio=0),
        ])
        
        waves.plot_indi(axes[0], sampling_rate=sampling_rate, t1=t1)
        
        
        axes[0].set_title(x_fmt_gen_eq, fontsize=18)
        #axes[0].set_xlabel(r'$\omega t$', fontsize=14)
        axes[0].set_ylabel(r'$x(t)\//\/x(0)$', fontsize=14)
        axes[0].axhline(y=0, linewidth=0.5, color='black')
        axes[0].legend(fontsize=12)
        
        waves.plot_indi_xdot(axes[1], sampling_rate=sampling_rate, t1=t1)
        
        
        axes[1].set_title(xdot_fmt_gen_eq, fontsize=18)
        axes[1].set_xlabel(r'$\omega t$', fontsize=14)
        axes[1].set_ylabel(r'$x(t)\//\/x(0)$', fontsize=14)
        axes[1].axhline(y=0, linewidth=0.5, color='black')
        axes[1].legend(fontsize=12)
        
        plt.savefig('plt_indi_w0_{}.png'.format(undamped_freq))
        axes[0].clear()
        axes[1].clear()
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    