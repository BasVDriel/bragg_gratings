import os
import numpy as np
import matplotlib.pyplot as plt
from fbg_utils.loading import data_validation, read_files
from fbg_utils.format import calc_uncer

directory = 'data'

n_peaks = 8
n_exp = range(1,5)
n_meas = range(0,10) # number of weights + zero measurement

# Run a quick data validation first
for exp in n_exp:
    for meas in n_meas: 
        file_name = '{}-{}.txt'.format(exp, meas)
        file_path = os.path.join(directory, file_name)
        measurement = data_validation(file_path, n_peaks=n_peaks)

# Now we start reading in data, we make an n_exp x weight_idx x FBG/n_peaks
complete_data = []

for exp in n_exp:
    for meas in n_meas: 
        file_name = '{}-{}.txt'.format(exp, meas)
        file_path = os.path.join(directory, file_name)
        measurement = data_validation(file_path, n_peaks=n_peaks)
        uncert_meas = calc_uncer(measurement)
        complete_data.append(uncert_meas)

print(complete_data)