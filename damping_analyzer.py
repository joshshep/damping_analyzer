#! /usr/bin/env python

'''

Created by:	Joshua Shepherd
Started:	2017-09-19


Helpful links
wiki
    https://en.wikipedia.org/wiki/Harmonic_oscillator
    https://en.wikipedia.org/wiki/Damping_ratio

hyperphysics
    http://hyperphysics.phy-astr.gsu.edu/hbase/oscda.html
    http://hyperphysics.phy-astr.gsu.edu/hbase/oscda2.html
    http://hyperphysics.phy-astr.gsu.edu/hbase/shm2.html

other
    https://ocw.mit.edu/courses/mathematics/18-03sc-differential-equations-fall-2011/unit-ii-second-order-constant-coefficient-linear-equations/damped-harmonic-oscillators/MIT18_03SCF11_s13_2text.pdf
'''


from __future__ import print_function
from math import sin, pi, cos, exp, sqrt

import numpy as np
import matplotlib.pyplot as plt

class Wave:
    """
    Waves with magnitudes and damping ratios and stimulation points?
    
    Input angles are in Hz (they are immediately translated to radians)
    """
    
    def __init__(self,
                    mag=1.0,
                    undamped_freq=1.0,
                    damping_ratio=0.0,
                    start_t=0.0,
                    phase=0.0,
                    color=None):
        assert(mag>=0)
        assert(undamped_freq>=0)
        assert(damping_ratio>=0)
        self.mag = mag
        self.undamped_freq = undamped_freq * 2 * pi
        self.damping_ratio = damping_ratio
        self.start_t = start_t
        self.phase = phase * 2 * pi
        self.color = color
        
        # the frequency when underdamped is *not* the same as the resonance freq
        if self.damping_ratio <= 1:
            # thank you wikipedia: https://en.wikipedia.org/wiki/Harmonic_oscillator#Damped_harmonic_oscillator
            self.underdamped_freq = self.undamped_freq * sqrt(1 - self.damping_ratio**2)


    '''
    Get the value of the wave at t seconds
    '''
    def at(self, t):
        if t >= self.start_t:
            t -= self.start_t
            if self.damping_ratio <= 1:
                #underdamped
                #https://sites.math.washington.edu/~king/coursedir/m308a01/Projects/m308a01-pdf/reed.pdf
                #return exp(-1.0*self.undamped_freq*self.damping_ratio*t) * self.mag * cos( (self.underdamped_freq*t + self.phase)*2.0*pi )
                return exp(-1.0*self.undamped_freq*self.damping_ratio*t) * self.mag * cos( self.underdamped_freq*t + self.phase )
            else:
                #critcally or over damped
                return self.mag * exp(-1.0*(self.phase +(1/self.damping_ratio))*t)
        return 0.0
    def xdot_at(self, t):
        if t >= self.start_t:
            t -= self.start_t
            if self.damping_ratio <= 1:
                #underdamped
                w_0  = self.undamped_freq
                w_d  = self.underdamped_freq
                A    = self.mag
                zeta = self.damping_ratio
                phi  = self.phase
                return -1.0 * A * exp(-1.0*w_0*zeta*t) * ( zeta*cos(w_d*t + phi) + w_d*sin(w_d*t + phi) )
            else:
                #critcally or over damped
                return self.mag * exp(-1.0*(self.phase +(1/self.damping_ratio))*t)
        return 0.0
        
    def ats(self, ts):
        y = np.ndarray(ts.shape[0])
        for i in range(ts.shape[0]):
            y[i] = self.at(ts[i])
        return y

    def get_latex_eq(self):
        pass
        #return r'$e^-1$'

class Waves:
    """
    A collection of waves
    """
    waves = []
    
    def __init__(self, waves):
        self.waves += waves
    
    '''
    Get the superposition of all of the waves at t seconds
    '''
    def at(self, t):
        tot = 0.0
        for wave in self.waves:
            tot += wave.at(t)
        return tot
    
    def rm_dead_waves(self):
        pass
    
    '''
    
    Plotting functions
    
    '''
    def plot_dft(self, t0=0.0, t1=5.0, sampling_rate=20.0, color=None):
        x = np.arange(t0, t1, 1.0/sampling_rate)
        y = np.ndarray(x.shape)
        for i in range(x.shape[0]):
            y[i] = self.at(x[i])
        s = np.fft.fft(y)
        #np.fft.fftfreq tells you the frequencies associated with the coefficients
        freqs = np.fft.fftfreq(len(y), d=1.0/sampling_rate)
        #t = np.arange(0, s.real.shape[0]/sampling_rate, 1.0/sampling_rate)
        #plt.plot(, s.real, label='real')
        plt.plot(freqs, s.real, 'b-', label='real')
        plt.plot(freqs, s.imag, 'r--', label='imaginary')

    def plot_super(self, t0=0.0, t1=5.0, sampling_rate=20.0, color=None):
        x = np.arange(t0, t1, 1.0/sampling_rate)
        y = np.ndarray(x.shape)
        for i in range(x.shape[0]):
            y[i] = self.at(x[i])
        plt.plot(x,y, color=color, label='super')
    
    def plot_indi(self, ax, t0=0.0, t1=5.0, sampling_rate=20.0):
        x = np.arange(t0, t1, 1.0/sampling_rate)
        y = np.ndarray(x.shape)
        for wave in self.waves:
            for i in range(x.shape[0]):
                y[i] = wave.at(x[i])
            ax.plot(x, y,
                     color=wave.color,
                     label=r'$\zeta = $'+str(wave.damping_ratio))

    def plot_indi_xdot(self, ax, t0=0.0, t1=5.0, sampling_rate=20.0):
        x = np.arange(t0, t1, 1.0/sampling_rate)
        y = np.ndarray(x.shape)
        for wave in self.waves:
            for i in range(x.shape[0]):
                y[i] = wave.xdot_at(x[i])
            ax.plot(x, y,
                     color=wave.color,
                     label=r'$\zeta = $'+str(wave.damping_ratio))
    
    
    
    
    
    
    
    