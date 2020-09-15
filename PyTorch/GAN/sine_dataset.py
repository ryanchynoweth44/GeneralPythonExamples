from torch import rand
from torch.utils.data import Dataset
import h5py


class SineWaveDataset(Dataset):
    """ Sine Wave Dataset """ 

    def __init__(self, data_path, identifier='default', sequence_length=5, forecast=1):
        """
        Args:
            data_path (string): Path to the folder containing csv files.
                    - we expect CSV files to be in order and the rows within those files to be in order as well. 
            identifier: the dataset name we are loading
            sequence_length: the length of our training batches
            forecast: this determines our y label. If forecast == 5 then we will produce an output  sequnce of 5

        """
        self.__data_path = data_path
        self.__identifier = identifier
        self.__length = None
        self.__sequence_length = sequence_length 
        self.__forecast = forecast



    def __len__(self):
        if self.__length is None:
            hf = h5py.File(self.__data_path, 'r')
            data = hf.get(self.__identifier)
            self.__length = len(data)-self.__sequence_length-self.__forecast
            hf.close()

        return self.__length


    def __getitem__(self, idx):
        hf = h5py.File(self.__data_path, 'r')
        X = hf.get(self.__identifier)[idx:idx+self.__sequence_length]
        y = hf.get(self.__identifier)[idx+self.__sequence_length:idx+self.__sequence_length+self.__forecast] 
        hf.close()
        return X, y

