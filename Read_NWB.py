# -*- coding: utf-8 -*-
"""
Created on 21/8/2024

@author: Sarah Tennant
"""

# import packages
from pynwb import NWBHDF5IO, NWBFile, TimeSeries


filepath = "SCN_477.nwb"
# Open the file in read mode "r",
io = NWBHDF5IO(filepath, mode="r")
nwbfile = io.read()
nwbfile

# check the data is there etc
nwbfile.TimeSeries.to_dataframe()

# plot the time series data



io.close() # this stops it from corrupting the file