from torch.utils.data import Dataset
import h5py


class BTCCustomDataset(Dataset):
    """ BTC OHLCV Dataset """ 

    def __init__(self, data_path, identifier='default', transform_data=False):
        """
        Args:
            data_path (string): Path to the folder containing csv files.
                    - we expect CSV files to be in order and the rows within those files to be in order as well. 
        """
        self.__data_path = data_path
        self.__identifier = identifier
        self.__length = None
        self.__transform_data = transform_data



    def __len__(self):
        if self.__length is None:
            hf = h5py.File(self.__data_path, 'r')
            data = hf.get(self.__identifier)
            self.__length = len(data)
            hf.close()

        return self.__length


    def __getitem__(self, idx):
        hf = h5py.File(self.__data_path, 'r')
        data = hf.get(self.__identifier)[:]
        hf.close()
        if self.__transform == False:
            return data[idx]
        else :
            return self.__transform(data[idx])

    def __transform(self, n):
        """ n is a number """
        return n+100000
