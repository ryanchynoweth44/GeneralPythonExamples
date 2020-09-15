import torch
import torch.nn as nn
import torch.nn.functional as F


class LSTMGenerator(nn.Module):
    def __init__(self, input_size=1, hidden_size=128, num_layers=2, output_size=1, bias=True, batch=False, dropout=0, bidirectional=False, device="cpu"):
        """ 

        :param num_layers: the number of lstm layers 
        :param batch: If set to true then the network expects tensors of size (batch, seq, feature)
        """
        super(LSTMGenerator, self).__init__()
        
        self.input_size=input_size 
        self.hidden_size=hidden_size 
        self.num_layers=num_layers 
        self.output_size=output_size 
        self.batch=batch 
        self.d = device 

        # https://pytorch.org/docs/stable/nn.html#lstm
        self.lstm = nn.LSTM(self.input_size, hidden_size=self.hidden_size, num_layers=self.num_layers, bias=bias, batch_first=self.batch, dropout=dropout, bidirectional=bidirectional)
        
        # https://pytorch.org/docs/stable/nn.html#linear
        self.fc1 = nn.Linear(in_features=self.hidden_size, out_features=self.output_size)


    def forward(self, t):
        # Set hidden and cell states 
        h0 = torch.zeros(self.num_layers, t.size(0), self.hidden_size).to(self.d)
        c0 = torch.zeros(self.num_layers, t.size(0), self.hidden_size).to(self.d)
        
        t, _ = self.lstm(t, (h0, c0))  # out: tensor of shape (batch_size, seq_length, hidden_size)
        
        t = self.fc1(t[:, -1, :])
        return t



class CNNDiscriminator(nn.Module):
    
    def __init__(self, input_size, output_size=1):
        super(CNNDiscriminator, self).__init__()

        self.conv1 = nn.Conv2d(in_channels=input_size, out_channels=5, kernel_size=1)
        self.conv2 = nn.Conv2d(in_channels=5, out_channels=10, kernel_size=1)
        
        self.fc1 = nn.Linear(in_features=10*1*1, out_features=120)
        self.out = nn.Linear(in_features=120, out_features=output_size)

    def forward(self, t):
        # (0) t is our input layer

        # (1) hidden conv layer 1
        t = self.conv1(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=1, stride=1)

        # (2) hidden conv layer 2
        t = self.conv2(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=1, stride=1)

        # (3) hidden linear layer 5
        t = t.reshape(-1, 10*1*1)
        t = self.fc1(t)
        t = F.relu(t)

        # (4) output layer
        t = self.out(t)
        t = F.relu(t)

        return t