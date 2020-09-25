from PyTorch.GAN.sine_dataset import SineWaveDataset
from PyTorch.GAN.networks import LSTMGenerator, CNNDiscriminator
from torch.utils.data import DataLoader
import torch
import torch.nn as nn
import torch.optim as optim
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


device = 'cuda'  if torch.cuda.is_available() else 'cpu'
torch.device(device)
print("Using {}.".format(device))

sequence_length = 42
forecast = 10
sine_data = SineWaveDataset(data_path="PyTorch/GAN/data/sine_wave_data.hdf5", sequence_length=sequence_length, forecast=forecast)


lstm_net = LSTMGenerator(batch=True, output_size=forecast, device=device)
lstm_net.float()
lstm_net.to(device)




### Test our network
# Provide only the last data point from our model and predict for 1000 time steps
prediction_length = 1500
x, y = sine_data.__getitem__(len(sine_data))
x_data = torch.from_numpy(x)

# load weights
lstm_net.load_state_dict(torch.load("PyTorch/gan/networks/trained_lstm.pt"))


for i in range(0, prediction_length, forecast):
    with torch.no_grad():
        x_input = x_data[i:i+sequence_length].reshape(1,-1,1).float().to(device)
        out = lstm_net(x_input)

    x_data = torch.cat((x_data.float(), out.detach().cpu().flatten()), dim=0)


plt.plot(range(0, x_data.shape[0]), np.array(x_data.flatten()))
plt.savefig("PyTorch/gan/imgs/predictions.png")
plt.show()

