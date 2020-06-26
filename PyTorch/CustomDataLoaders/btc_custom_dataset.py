from torch.utils.data import Dataset
import os


class BTCCustomDataset(Dataset):
    """ BTC OHLCV Dataset """ 

    def __init__(self, data_path):
        """
        Args:
            data_path (string): Path to the folder containing csv files.
        """
        self.data_path = data_path
        self.length = None
        self.indicies = {} # tracks which csv files contain which index values

    def __len__(self):
        if self.length is None:
            files = os.listdir(self.data_path)
            row_count = 0 

            for f in files:
                with open("{}/{}".format(self.data_path, f)) as fp:
                    for _ in fp:
                        row_count += 1
                    self.indicies["{}/{}".format(self.data_path, f)] = row_count
            self.length = row_count
        return self.length


    def __getitem__(self, idx):
        return False