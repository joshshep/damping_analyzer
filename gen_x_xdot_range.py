#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from damping_analyzer import Wave, Waves
from math import pi
from scipy import signal
import matplotlib.gridspec as gridspec
from utils import ensure_path_exists
from os.path import join

if __name__ == '__main__':

    sampling_rate = 200
    t1 = 5
    IMG_DIR = 'imgs/'
    ensure_path_exists(IMG_DIR)
    
    freqs = [0.5, 1, 1.5, 2, 2.5, 3, 3.3, 4, 5, 8]
    
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
    
    
    #freqs = [0.5, 1, 1.5, 2, 2.5, 3, 3.3, 4, 5, 8]
    
    fig = plt.figure()
    fig.set_size_inches(18.5, 10.5)
    
    ax0 = fig.add_subplot(2,1,1)
    ax1 = fig.add_subplot(2,1,2, sharex=ax0)
    
    legend_loc = 'upper right'
    
    
    for undamped_freq in freqs:
        print('freq (w_0): {:1.1f} Hz'.format(undamped_freq))
        waves = Waves([
            Wave(undamped_freq=undamped_freq, damping_ratio=0),
            Wave(undamped_freq=undamped_freq, damping_ratio=0.05),
            Wave(undamped_freq=undamped_freq, damping_ratio=0.2),
            Wave(undamped_freq=undamped_freq, damping_ratio=0.5),
            Wave(undamped_freq=undamped_freq, damping_ratio=0.8)
        ])

        waves.plot_indi(     ax0, sampling_rate=sampling_rate, t1=t1)
        waves.plot_indi_xdot(ax1, sampling_rate=sampling_rate, t1=t1)
        
        w0_label = r'$ \omega_0 = {} Hz $'.format(undamped_freq)
        fig.suptitle(w0_label, fontsize=20)
        
        ax0.set_title(x_fmt_gen_eq, fontsize=18)
        #ax0.set_xlabel(r'$\omega t$', fontsize=14)
        ax0.set_ylabel(r'$ x(t) $', fontsize=14)
        ax0.axhline(y=0, linewidth=0.5, color='black')
        ax0.legend(fontsize=12, loc=legend_loc)
        ax0.get_xaxis().set_visible(False)
        
        
        ax1.set_title(xdot_fmt_gen_eq, fontsize=18)
        ax1.set_xlabel(r'$ t $', fontsize=14)
        ax1.set_ylabel(r'$ \dot{x}(t) $', fontsize=14)
        ax1.axhline(y=0, linewidth=0.5, color='black')
        ax1.legend(fontsize=12, loc=legend_loc)
        
        
        
        pic_bname = join(IMG_DIR, 'plt_indi_w0_{:1.1f}Hz'.format(undamped_freq))
        fig.savefig(pic_bname+'.png')
        fig.savefig(pic_bname+'.pdf')
        
        ax0.cla()
        ax1.cla()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    