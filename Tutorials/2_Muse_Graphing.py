# 2024-11-10
# Minoo J
# FROM CHATGPT, DOES NOT WORK

from muselsl import MuseHub, MuseStream
import matplotlib.pyplot as plt
from collections import deque
import numpy as np
import time

# Connect to the Muse 2 device via LSL (Lab Streaming Layer)
muse_hub = MuseHub()
muse_hub.start()

# Create a stream to receive data
stream = MuseStream(muse_hub)
stream.start()

# Assuming `eeg_data` is a 1D array of EEG values from the Muse device (?)
eeg_data_queue = deque(maxlen=100)

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_ylim(-100, 100)  # Adjust to the scale of your data
ax.set_xlim(0, 100)

while True:
    i = 0
    eeg_data = stream.pull_data() # I think this is a numpy array; columns are channels, rows are timestamps
    
    eeg_data_queue.append(eeg_data[i])
    line.set_xdata(np.arange(len(eeg_data_queue)))  # num rows
    line.set_ydata(np.array(eeg_data_queue))  # channel data
    
    plt.pause(0.01)  # Update plot
    time.sleep(0.01)  # Simulate real-time data stream
    i += 1