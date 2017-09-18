#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from damping_analyzer import Wave, Waves

if __name__ == '__main__':
	waves = Waves([
		Wave(freq=1.3),
		Wave(freq=7, mag=0.25)
	])
	waves.plot(sampling_rate=100)