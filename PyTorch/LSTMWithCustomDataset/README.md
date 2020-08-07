# LSTM with Custom Dataset

In this example, I am going to reproduce the LSTM time series example that is predicting the values in a sine wave. This example was taken from this [PyTorch Example](https://github.com/pytorch/examples/blob/master/time_sequence_prediction/train.py). Often users will create sequences prior to training a network, this code can be cumbersome when it comes to iterating over your experiment and testing our different parameters on how to structure our data. For example, you may want to adjust your sequence length to test how that effects the performance of your network. This can generally be done in your training script before you actually start training, however, this can get a little messy. In this example, we will leverage a custom dataset that will allow us to offload and parameterize data transformations to make our training script cleaner and easier to read. Additionally, parameterizing our dataset transformations will make it easier to adjust our training dataset using different parameter values. 


## Steps
1. In our example we will need to [create our sine wave dataset](create_dataset.py). In our case we will store our data as an hdf5 data file. 
1. Next we will use our dataset in our [training script](train.py), and within our training script we also generate a plot of predictions. 



Check out the following code snippet to view the custom dataset data directly. 
```python
from PyTorch.LSTMWithCustomDataset.sine_dataset import SineWaveDataset
from torch.utils.data import DataLoader
import h5py

sine_data = SineWaveDataset(data_path="PyTorch/LSTMWithCustomDataset/data/sine_wave_data.hdf5")



sine_data.__getitem__(994)
f = h5py.File("PyTorch/LSTMWithCustomDataset/data/sine_wave_data.hdf5", 'r')
data = f['default']
print(data[5])


dataloader = DataLoader(sine_data, batch_size=4, shuffle=False, num_workers=2)



for X, y in dataloader:
    print("--------- x: {}".format(X))
    print("--------- y: {}".format(y))


len(sine_data)

```
