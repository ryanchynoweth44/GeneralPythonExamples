from PyTorch.CustomDataLoaders.btc_hdf5_custom_dataset import BTCCustomDataset
from torch.utils.data import DataLoader
from time import sleep

dataset = BTCCustomDataset(data_path="PyTorch/CustomDataLoaders/data/btc_hdf5_data.hdf5")
dataset2 = BTCCustomDataset(data_path="PyTorch/CustomDataLoaders/data/btc_hdf5_data.hdf5", transform_data=True)

len(dataset)

dataset.get_item(0)
type(dataset.get_item(0))


### HDF5 file cannot be pickled so number of workers must be 0. Otherwise we get an error
dataloader = DataLoader(dataset, batch_size=4, shuffle=True, num_workers=2)
dataloader2 = DataLoader(dataset2, batch_size=40, shuffle=True, num_workers=2)

for x in dataloader:
    print(x)
    sleep(0.5)




for x in dataloader2:
    print(x)
    sleep(0.5)


