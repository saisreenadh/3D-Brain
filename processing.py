import mne
import numpy as np
import os

def load_file(file):
    """Loading EEG data from a file"""
    try:
        raw_data = mne.io.read_raw_fif(file, preload = True)
        return raw_data
    except Exception as e:
        print("Error loading data: " + str(e))
        return None

def filter_data(raw_data, low_freq = 0.1, high_freq = 30.0):
    """Applying a filter to the raw data to remove noise"""
    raw_data.filter(low_freq, high_freq)
    return raw_data

def detect_activation(raw_data, electrode, threshold, duration=1.0):
    """
    Detect activation above a threshold.
    
    Parameters:
    - raw_data: Filtered EEG data
    - electrode: Electrode channel name (e.g., 'Fp1')
    - threshold: Threshold level for activation detection
    - duration: Duration in seconds for averaging signal amplitude
    
    Returns:
    - Boolean indicating whether activation is above threshold.
    """
    if electrode not in raw_data.ch_names:
        print(f"Electrode {electrode} not found in data.")
        return False

    data, times = raw_data[electrode]
    mean_amplitude = np.mean(data[:int(duration * raw_data.info['sfreq'])])
    print(f"Mean amplitude for {electrode}: {mean_amplitude}")
    return mean_amplitude > threshold