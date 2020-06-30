from torch.utils.data import Dataset
from numpy import genfromtxt
import os


class BTCCustomDataset(Dataset):
    """ BTC OHLCV Dataset """ 

    def __init__(self, data_path):
        """
        Args:
            data_path (string): Path to the folder containing csv files.
                    - we expect CSV files to be in order and the rows within those files to be in order as well. 
        """
        self.data_path = data_path
        self.length = None
        self.indicies = {} # tracks which csv files contain which index values
        self.__len__()

    def __len__(self):
        if self.length is None:
            files = os.listdir(self.data_path)
            row_count = 0 

            for f in files:
                with open("{}/{}".format(self.data_path, f)) as fp:
                    for _ in fp:
                        row_count += 1
                    row_count-=2 # headers and last row
                    self.indicies[row_count] = "{}/{}".format(self.data_path, f)
            self.length = row_count
        return self.length

    def __get_file(self, idx):
        keys = sorted(self.indicies.keys())
        file_path = ""
        key = 0
        for i in range(0, len(keys)):
            if idx <= keys[i]:
                key = keys[i]
                file_path = self.indicies.get(keys[i])
                break
        
        return file_path, key-idx


    def __getitem__(self, idx):
        file_path, file_idx = self.__get_file(idx)
         
        data = genfromtxt(file_path, delimiter=',', skip_header=1)
        return data[file_idx, :]



    def __format_datapoint(self, data):
        """ While it may slow down training you can easily format your tensors lazily instead of having to preprocess data """

        return "Not Yet Implemented"