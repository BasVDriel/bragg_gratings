import numpy as np
from uncertainties import unumpy

def calc_uncer(measurement):
    shape = measurement.shape[1]
    std_array = np.zeros(shape)
    mean_array = np.zeros(shape)
    for n in range(measurement.shape[1]):
        grating = measurement[::, n]
        mean_measurement = np.mean(grating)
        std_error = np.std(grating, ddof=1) / np.sqrt(measurement.shape[1])
        std_array[n] = std_error
        mean_array[n] = mean_measurement
    return unumpy.uarray(mean_array, std_array)
