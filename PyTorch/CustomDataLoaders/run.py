from PyTorch.CustomDataLoaders.btc_custom_dataset import BTCCustomDataset
from torch.utils.data import DataLoader
from time import sleep

dataset = BTCCustomDataset(data_path="PyTorch/CustomDataLoaders/data")


dataloader = DataLoader(dataset, batch_size=4, shuffle=True, num_workers=4)

for x in dataloader:
    print(x)
    sleep(5)


