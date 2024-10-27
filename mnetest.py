# ChatGPT

import mne
import matplotlib.pyplot as plt

plt.ion()

# Load the sample dataset
sample_data_path = mne.datasets.sample.data_path()
fwd_fname = str(sample_data_path) + '/MEG/sample/sample_audvis-meg-oct-6-fwd.fif'
evoked_fname = str(sample_data_path) + '/MEG/sample/sample_audvis-ave.fif'
cov_fname = str(sample_data_path) + '/MEG/sample/sample_audvis-cov.fif'

try:
    # Read the forward solution, evoked data, and noise covariance matrix
    fwd = mne.read_forward_solution(fwd_fname)
    evoked = mne.read_evokeds(evoked_fname, condition='Left Auditory')
    noise_cov = mne.read_cov(cov_fname)

    # Create the inverse operator using the noise covariance matrix
    inverse_operator = mne.minimum_norm.make_inverse_operator(
        evoked.info, fwd, noise_cov=noise_cov, loose=0.2, depth=0.8
    )

    # Apply the inverse operator to obtain a source time course
    stc = mne.minimum_norm.apply_inverse(evoked, inverse_operator, lambda2=1.0 / 9.0, method='dSPM')

    # Visualize the result
    subjects_dir = str(sample_data_path) + '/subjects'
    stc.plot(subject='sample', subjects_dir=subjects_dir, initial_time=0.1)
    plt.show(block=True)

finally:
    input("Return to close the plot window")