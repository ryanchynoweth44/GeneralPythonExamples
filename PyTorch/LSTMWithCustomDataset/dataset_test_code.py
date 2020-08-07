from PyTorch.LSTMWithCustomDataset.sine_dataset import SineWaveDataset
from torch.utils.data import DataLoader
import h5py

sine_data = SineWaveDataset(data_path="PyTorch/LSTMWithCustomDataset/data/sine_wave_data.hdf5")



sine_data.__getitem__(994)
f = h5py.File("PyTorch/LSTMWithCustomDataset/data/sine_wave_data.hdf5", 'r')
data = f['default']
print(data[5])


dataloader = DataLoader(sine_data, batch_size=4, shuffle=False, num_workers=2)



for X, y in dataloader:
    print("--------- x: {}".format(X))
    print("--------- y: {}".format(y))


len(sine_data)