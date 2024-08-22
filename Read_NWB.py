# -*- coding: utf-8 -*-
"""
Created on 21/8/2024

@author: Sarah Tennant
"""

# import packages
from pynwb import NWBHDF5IO, NWBFile, TimeSeries
import matplotlib.pyplot as plt


filepath = "SCN_477.nwb"
# Open the file in read mode "r",
io = NWBHDF5IO(filepath, mode="r")
nwbfile = io.read()
nwbfile

# check the data is there etc
print(nwbfile.acquisition['test_timeseries'])

# plot the time series data
test_swd = nwbfile.acquisition['test_timeseries'].data[:]
plt.plot(test_swd)
plt.show()

# print the subject details


# print electrode details



io.close() # this stops it from corrupting the file