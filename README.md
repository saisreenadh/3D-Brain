# 3D Brain Project (In Progress)

The **3D Brain Project** is an interactive, real-time visualization of brain activity using EEG data. This project places an EEG headset on a participant and analyzes their brain's responses to prompts. If certain brain activity thresholds are exceeded, lights on a 3D model of the brain illuminate to represent activated regions.

## Project Overview

The project consists of three main components:
1. **Data Processing**: Filtering and preprocessing EEG signals to reduce noise.
2. **Activation Detection**: Detecting significant brain activity above a specified threshold.
3. **3D Brain Model Visualization**: Mapping detected brain activations to a 3D model with corresponding LEDs that light up in response to specific activations.

## Project Structure

- **`processing.py`**: Contains functions for loading, filtering, and analyzing EEG data.
- **`display.py`**: Manages the interface with the 3D brain model, controlling LEDs based on detected activation.

## How It Works

1. **Load EEG Data**: Raw EEG data is loaded from a sample file or live EEG headset feed.
2. **Data Preprocessing**: Data is filtered to isolate relevant frequency bands and reduce noise.
3. **Activation Detection**: Specific channels are monitored, and when activity exceeds a set threshold, activation is detected.
4. **3D Model Visualization**: Detected activations light up specific regions on the 3D brain model, illustrating areas of heightened activity in real-time.

## Getting Started

### Prerequisites

- Python 3.x
- [MNE Library](https://mne.tools/stable/index.html) (for EEG data processing)
- NumPy (for numerical operations)
- Matplotlib (for optional visualizations)

### Installation

1. Clone this repository:
   ```bash
   git clone git@github.com:saisreenadh/3D-Brain.git
   cd 3D-Brain
   ```
2. Install required libraries:
   ```bash
   pip install mne numpy matplotlib
   ```

### Running the Project

To test the functionality with sample EEG data:
1. Run the processing code:
   ```bash
   python3 processing.py
   ```

2. Follow the prompts or modify `processing.py` to set up different thresholds or test specific channels.

### Example Usage

Here’s a quick example of how the functions work together:
```python
from processing import load_file, filter_data, detect_activation

file_path = 'path/to/eeg_data_file.fif'  # Update with your file path
raw_data = load_file(file_path)
filtered_data = filter_data(raw_data)

if detect_activation(filtered_data, electrode='Fp1', threshold=1e-13):
    print("Activation detected!")
```

## Configuration

- **EEG Threshold**: Adjust the `threshold` parameter in `detect_activation()` to set the desired sensitivity for activation.
- **Electrodes**: Change the `electrode` parameter to monitor different brain regions (e.g., `'Fp1'`, `'C3'`, etc.).
- **Duration**: Modify `duration` to alter the window of time considered for activation.

## Future Enhancements

- Integrate with real-time EEG hardware for live data streaming.
- Add more brain regions and map more granular activity to the 3D model.
- Implement machine learning for adaptive thresholding based on user baseline data.
