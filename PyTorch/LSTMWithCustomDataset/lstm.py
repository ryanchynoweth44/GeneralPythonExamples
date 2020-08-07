import torch
import torch.nn as nn



class LSTMNetwork(nn.Module):
    def __init__(self, input_size=1, hidden_size=128, num_layers=2, output_size=1, bias=True, batch=False, dropout=0, bidirectional=False):
        """ 

        :param num_layers: the number of lstm layers 
        :param batch: If set to true then the network expects tensors of size (batch, seq, feature)
        """
        super(LSTMNetwork, self).__init__()
        
        self.input_size=input_size 
        self.hidden_size=hidden_size 
        self.num_layers=num_layers 
        self.output_size=output_size 
        self.batch=batch 

        # https://pytorch.org/docs/stable/nn.html#lstm
        self.lstm = nn.LSTM(self.input_size, hidden_size=self.hidden_size, num_layers=self.num_layers, bias=bias, batch_first=self.batch, dropout=dropout, bidirectional=bidirectional)
        
        # https://pytorch.org/docs/stable/nn.html#linear
        self.fc1 = nn.Linear(in_features=self.hidden_size, out_features=self.output_size)


    def reset_hidden(self):
        return (torch.zeros(1, 1, self.hidden_size), torch.zeros(1, 1, self.hidden_size))

    def forward(self, t):
        # Set initial hidden and cell states 
        h0 = torch.zeros(self.num_layers, t.size(0), self.hidden_size)
        c0 = torch.zeros(self.num_layers, t.size(0), self.hidden_size)
        
        # Forward propagate LSTM
        t, _ = self.lstm(t, (h0, c0))  # out: tensor of shape (batch_size, seq_length, hidden_size)
        
        # Decode the hidden state of the last time step
        # t = torch.tanh(self.fc1(t[:, -1, :]))
        t = self.fc1(t[:, -1, :])
        return t


