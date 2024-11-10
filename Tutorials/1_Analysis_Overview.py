# 2024-11-06
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


### STATISTICS ###

# print(raw)
# print(raw.info)

raw.compute_psd(fmax=50).plot(picks="data", exclude="bads", amplitude=False)    # low pass filter, power spectral density graph
fig = raw.plot(duration=5, n_channels=30)     # plot 30 channels' raw data over 5 seconds

# explore future pre-processing techniques: maxwell filtering, signal-space projection, independent components analysis, filtering, downsampling
# read mne.preprocessing, mne.filter documentation


### PRE-PROCESSING ###

# set up and fit the ICA
ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
ica.fit(raw)
ica.exclude = [1, 2]  # details on how we picked these artifacts are omitted in this tutorial
# ica.plot_properties(raw, picks=ica.exclude)


orig_raw = raw.copy()
raw.load_data() # loads data into memory
ica.apply(raw) # applies pre-processing, artifact removal to data

# show some frontal channels to clearly illustrate the artifact removal
chs = [
    "MEG 0111",
    "MEG 0121",
    "MEG 0131",
    "MEG 0211",
    "MEG 0221",
    "MEG 0231",
    "MEG 0311",
    "MEG 0321",
    "MEG 0331",
    "MEG 1511",
    "MEG 1521",
    "MEG 1531",
    "EEG 001",
    "EEG 002",
    "EEG 003",
    "EEG 004",
    "EEG 005",
    "EEG 006",
    "EEG 007",
    "EEG 008",
]
chan_idxs = [raw.ch_names.index(ch) for ch in chs]

orig_raw.plot(order=chan_idxs, start=12, duration=4)
raw.plot(order=chan_idxs, start=12, duration=4)

plt.show(block=True)