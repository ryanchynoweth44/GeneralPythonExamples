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
dataloader = DataLoader(sine_data, batch_size=64, shuffle=False, num_workers=2)


lstm_net = LSTMGenerator(batch=True, output_size=forecast)
lstm_net.float()
lstm_net.to(device)
gen_optim = optim.SGD(lstm_net.parameters(), lr=0.001, momentum=0.9)
lstm_loss_func = nn.MSELoss()

# output size is 1 for a probability between 0 and 1
cnn_net = CNNDiscriminator(input_size=forecast,output_size=1)
cnn_net.float()
cnn_net.to(device)
dis_optim = optim.SGD(cnn_net.parameters(), lr=0.001, momentum=0.9)
cnn_loss_func = nn.BCELoss()

EPOCHS = 10

cnn_training_loss, lstm_training_loss = [], []
cnn_validation_loss, lstm_validation_loss = [], []
for epoch in range(EPOCHS):
    print("{}: Starting Epoch {}.".format(datetime.utcnow(), epoch))
    lstm_epoch_loss, cnn_epoch_loss = 0, 0 
    for i, data in enumerate(dataloader, 0):
        ######### Discriminator
        ####
        # (1) Train cnn_net with real data
        ####
        # zero gradients
        cnn_net.zero_grad()
        # get x and y - y is all 1's
        real_seq = data[1]
        real_seq = real_seq.reshape(real_seq.shape[0], forecast, 1, 1).to(device) # (batch_size, height, width, depth)
        real_y = torch.full((real_seq.size(0),), 1, dtype=torch.float, device=device).reshape(-1,1)
        # forward pass
        output = cnn_net(real_seq.float())
        cnn_real_loss = cnn_loss_func(output, real_y)
        cnn_real_loss.backward(retain_graph=True)
        ####
        # (2) Train cnn_net with fake data
        ####
        # create fake data with generator
        noise = torch.randn(real_seq.shape[0], sequence_length, 1, device=device)
        fake_y = torch.full((real_seq.size(0),), 0, dtype=torch.float, device=device).reshape(-1,1)
        # generate fake data with lstm
        noise_output = lstm_net(noise)
        noise_output = noise_output.reshape(noise_output.shape[0], noise_output.shape[1], 1,1)
        # classify output with 
        fake_output = cnn_net(noise_output.float())
        # calculate loss
        cnn_fake_loss = cnn_loss_func(output, fake_y)
        # backward pass
        cnn_fake_loss.backward()
        dis_optim.step()
        cnn_epoch_loss += (cnn_fake_loss+cnn_real_loss)

        ######### Generator
        ####
        # (3) Train lstm_net
        ####
        lstm_net.zero_grad()
        x, y = data[0], data[1]
        x = x.reshape(x.shape[0], x.shape[1], 1).to(device)
        y = y.to(device)
        # forward pass
        output = lstm_net(x.float())
        # calculate loss
        lstm_loss = lstm_loss_func(output.float(), y.float())
        # backward pass
        lstm_loss.backward()
        gen_optim.step()
        lstm_epoch_loss += lstm_loss

    cnn_training_loss.append(cnn_epoch_loss)
    lstm_training_loss.append(lstm_epoch_loss)
    
    plt.cla()
    _ = plt.plot(range(0, len(cnn_training_loss)), cnn_training_loss, color='blue')
    plt.tight_layout()
    plt.savefig('PyTorch/GAN/cnn_training_loss.png')
    plt.cla()
    _ = plt.plot(range(0, len(lstm_training_loss)), lstm_training_loss, color='green')
    plt.tight_layout()
    plt.savefig('PyTorch/GAN/lstm_training_loss.png')


