import os
import numpy as np
import h5py
import matplotlib.pyplot as plt

## Reference: https://pythontic.com/visualization/charts/sinewave

np.random.seed(2)
os.makedirs("PyTorch/LSTMWithCustomDataset/data", exist_ok=True)

data_length = 2000
t_time = np.arange(0, data_length, 0.1)
amplitude = np.sin(t_time)

plt.plot(t_time, amplitude)
plt.show()


# our observed values are the "amplitude" array
# save these values to an array
f = h5py.File("PyTorch/LSTMWithCustomDataset/data/sine_wave_data.hdf5", 'w')
dset = f.create_dataset("default", data=amplitude)
f.close()


