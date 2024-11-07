# 2024-11-06
# Minoo J
# https://mne.tools/stable/auto_tutorials/intro/10_overview.html 

import numpy as np
import mne


### LOAD DATA ###

sample_data_folder = mne.datasets.sample.data_path()    # load sample dataset from mne
sample_data_raw_file = (
    sample_data_folder / "MEG" / "sample" / "sample_audvis_filt-0-40_raw.fif"
)
raw = mne.io.read_raw_fif(sample_data_raw_file)


### STATISTICS ###

# print(raw)
# print(raw.info)

raw.compute_psd(fmax=50).plot(picks="data", exclude="bads", amplitude=False)    # low pass filter, power spectral density graph
raw.plot(duration=5, n_channels=30)     # plot 30 channels' raw data over 5 seconds

# explore future pre-processing techniques: maxwell filtering, signal-space projection, independent components analysis, filtering, downsampling
# read mne.preprocessing, mne.filter documentation



# set up and fit the ICA
ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
ica.fit(raw)
ica.exclude = [1, 2]  # details on how we picked these artifacts are omitted in this tutorial
ica.plot_properties(raw, picks=ica.exclude)
