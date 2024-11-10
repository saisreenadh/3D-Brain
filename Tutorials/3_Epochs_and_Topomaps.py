# 2024-11-10
# Minoo J
# https://mne.tools/stable/auto_tutorials/intro/10_overview.html 

import numpy as np
import mne
import matplotlib.pyplot as plt
mne.set_config('MNE_PLOT_BACKEND', 'matplotlib')
plt.ion()

### LOAD DATA ###

sample_data_folder = mne.datasets.sample.data_path()    # load sample dataset from mne
sample_data_raw_file = (
    sample_data_folder / "MEG" / "sample" / "sample_audvis_filt-0-40_raw.fif"
)
raw = mne.io.read_raw_fif(sample_data_raw_file)

### PRE-PROCESSING ###

# set up and fit the ICA
ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
ica.fit(raw)
ica.exclude = [1, 2]  # details on how we picked these artifacts are omitted in this tutorial

orig_raw = raw.copy()
raw.load_data() # loads data into memory
ica.apply(raw) # applies pre-processing, artifact removal to data


### TOPOMAPS ###

# Create epochs without relying on events, using fixed windows from the start of data
epochs = mne.make_fixed_length_epochs(raw, duration=1, overlap=0.5, preload=True)  
# I don't really know what changing duration, overlap parameters does
# overlap means that each epoch overlaps with the previous by 0.5 seconds
# Epochs have a get_data() function which returns a Numpy array with dimension (n_epochs, n_channels, n_times)


evoked = epochs[0].average()
evoked.plot_topomap(times=[0.1, 0.3, 0.5, 0.7], ch_type="eeg", extrapolate="head", sensors=True)
plt.show(block=True)

times = np.arange(0.0, 0.992, 0.01)
fig, anim = evoked.animate_topomap(times=times, ch_type="eeg", frame_rate=16, blit=False)
plt.show(block=True)