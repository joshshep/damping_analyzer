#! /usr/bin/env python
from __future__ import print_function
from math import sin, pi

import numpy as np
import matplotlib.pyplot as plt

class Wave:
	"""
	Waves with magnitudes and damping ratios and stimulation points?
	"""
	def __init__(self, mag=1.0, freq=1.0, damping_ratio=0.0, start=0.0, start_angle=0.0):
		self.mag = mag
		self.freq = freq
		self.damping_ratio = damping_ratio
		self.start = start
		self.start_angle = start_angle
	def at(self, t):
		if t >= self.start:
			return self.mag * sin((self.freq)*t*2.0*pi)
		return 0.0

class Waves:
	"""
	A collection of waves
	"""
	waves = []
	def __init__(self, waves):
		self.waves += waves
	def at(self, t):
		tot = 0.0
		for wave in self.waves:
			tot += wave.at(t)
		return tot
	def rm_dead_waves(self):
		pass
	def add_wave(self, w):
		waves.append(w)
	def plot(self, t0=0.0, t1=5.0, sampling_rate=20.0):
		x = np.arange(t0, t1, 1.0/sampling_rate)
		y = np.ndarray(x.shape)
		for i in range(x.shape[0]):
			y[i] = self.at(x[i])
		plt.plot(x,y)
		plt.show()