from PyTorch.LSTMWithCustomDataset.sine_dataset import SineWaveDataset
from PyTorch.LSTMWithCustomDataset.lstm import LSTMNetwork
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


sequence_length = 40
forecast = 1
sine_data = SineWaveDataset(data_path="PyTorch/LSTMWithCustomDataset/data/sine_wave_data.hdf5", sequence_length=sequence_length, forecast=forecast)
dataloader = DataLoader(sine_data, batch_size=128, shuffle=False, num_workers=2)
net = LSTMNetwork(batch=True)
net.float()



loss_func = nn.MSELoss()
optimizer = optim.Adam(net.parameters(), lr=0.0001)

training_loss = []
epochs = 25
for i in range(0, epochs):
    print("{}: Epoch {} our of {}".format(datetime.utcnow(), i, epochs))
    net.hidden = net.reset_hidden()
    epoch_loss = 0
    for x, y in dataloader:
        x = x.reshape(x.shape[0], sequence_length, -1)
        y = y.reshape(y.shape[0], 1)
        optimizer.zero_grad()
        output = net(x.float())
        loss = loss_func(output, y)
        loss.backward()
        optimizer.step()
        epoch_loss+=loss.item()

    training_loss.append(epoch_loss)

torch.save(net.state_dict(), "PyTorch/LSTMWithCustomDataset/trained_lstm.pt")


plt.plot(range(0, epochs), training_loss)
plt.show()


### Test our network
# Provide only the last data point from our model and predict for 1000 time steps
prediction_length = 100
x, y = sine_data.__getitem__(len(sine_data))
x_data = torch.from_numpy(x)

# load weights
net = LSTMNetwork(batch=True)
net.load_state_dict(torch.load("PyTorch/LSTMWithCustomDataset/trained_lstm.pt"))
net.float()


for i in range(0, prediction_length):
    with torch.no_grad():
        x_input = x_data[i:i+sequence_length].reshape(1,-1,1).float()
        out = net(x_input)

    x_data = torch.cat((x_data.float(), out.flatten()), dim=0)


plt.plot(range(0, x_data.shape[0]), np.array(x_data.flatten()))
plt.show()


