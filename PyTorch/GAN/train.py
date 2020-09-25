from PyTorch.GAN.sine_dataset import SineWaveDataset
from PyTorch.GAN.networks import LSTMGenerator, CNNDiscriminator
from torch.utils.data import DataLoader
import torch
import torch.nn as nn
import torch.optim as optim
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import pickle


device = 'cuda'  if torch.cuda.is_available() else 'cpu'
torch.device(device)
print("Using {}.".format(device))

sequence_length = 42
forecast_length = 10
batch_size = 64
input_size = 1
sine_data = SineWaveDataset(data_path="PyTorch/GAN/data/sine_wave_data.hdf5", sequence_length=sequence_length, forecast=forecast_length)
dataloader = DataLoader(sine_data, batch_size=batch_size, shuffle=False, num_workers=2)

training_params = {'sequence_length': sequence_length, 'forecast_length': forecast_length, 'batch_size': batch_size, 'input_size': input_size}
pickle.dump(training_params, open("PyTorch/GAN/data/training_parameters.pkl", 'wb'))


g_net = LSTMGenerator(input_size=input_size, batch=True, output_size=forecast_length, device=device)
g_net.float()
g_net.to(device)
g_optim = optim.Adam(g_net.parameters(), lr=0.001)


# output size is 1 for a probability between 0 and 1
d_net = CNNDiscriminator(input_size=forecast_length,output_size=1)
d_net.float()
d_net.to(device)
d_optim = optim.Adam(d_net.parameters(), lr=0.001)


loss_func = nn.BCELoss()

EPOCHS = 100



d_training_loss, g_training_loss = [], []
d_validation_loss, g_validation_loss = [], []
for epoch in range(EPOCHS):
    print("{}: Starting Epoch {}.".format(datetime.utcnow(), epoch))
    g_epoch_loss, d_epoch_loss = 0, 0 
    for i, data in enumerate(dataloader, 0):
        # break
        ######### Discriminator
        ####
        # (1) Train d_net with real data
        ####
        # zero gradients
        d_net.zero_grad()
        # get x and y - y is all 1's
        real_seq = data[1]
        real_seq = real_seq.reshape(real_seq.shape[0], forecast_length, 1).to(device) # (batch_size, height, width)
        real_y = torch.full((real_seq.size(0),), 1, dtype=torch.float, device=device).reshape(-1,1)
        # forward pass and calculate loss
        output = d_net(real_seq.float())
        d_real_loss = loss_func(output, real_y)
        # backward pass
        d_real_loss.backward()
        
        ####
        # (2) Train d_net with 'fake' data
        # In our case we will be passing in real data to the g_net 
        # The output of the generator will be passed into d_net with a label of 0
        # We will then update d_net with error
        # 
        ####
        # create fake data with generator
        x = data[0].to(device)
        x = x.reshape(x.size(0), x.size(1), 1).float()
        y_label = torch.full((real_seq.size(0),), 0, dtype=torch.float, device=device).reshape(-1,1)
        # generate fake data with g
        g_output = g_net(x)
        g_output = g_output.reshape(g_output.shape[0], g_output.shape[1], 1)
        # classify output with 
        d_output = d_net(g_output.detach().float())
        # calculate loss
        d_fake_loss = loss_func(d_output, y_label)
        # backward pass
        d_fake_loss.backward()
        d_optim.step()
        d_epoch_loss += (d_fake_loss+d_real_loss)


        ######### Generator
        ####
        # (3) Train g_net
        # Here we need to optimize our g_net using our predictions from (2). 
        # The idea here is that we are using our d_net as the loss_func to improve predictions
        # 
        ####
        g_net.zero_grad()
        y_label = torch.full((g_output.size(0),), 1, dtype=torch.float, device=device).reshape(-1,1)
        # forward pass
        output = d_net(g_output.float())
        # calculate loss
        g_loss = loss_func(output.float(), y_label.float())
        # backward pass
        g_loss.backward()
        g_optim.step()
        g_epoch_loss += g_loss


    d_training_loss.append(d_epoch_loss)
    g_training_loss.append(g_epoch_loss)
    
    plt.cla()
    _ = plt.plot(range(0, len(d_training_loss)), d_training_loss, color='blue')
    plt.tight_layout()
    plt.savefig('PyTorch/GAN/imgs/d_training_loss.png')
    plt.cla()
    _ = plt.plot(range(0, len(g_training_loss)), g_training_loss, color='green')
    plt.tight_layout()
    plt.savefig('PyTorch/GAN/imgs/g_training_loss.png')

# save network states
torch.save(d_net.state_dict(), 'PyTorch/GAN/networks/d_net.pt')
torch.save(g_net.state_dict(), 'PyTorch/GAN/networks/g_net.pt')

