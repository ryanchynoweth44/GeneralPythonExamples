# PyTorch Custom Data Loaders

PyTorch data loaders are an excellent way to batch and process your data for deep learning algorithms. 

One huge advantage to using Data Loaders is the developers ability to customize and create their own loaders, espcially when data is larger in size or if data is unsually formatted. A custom data loader allows engineers to keep data on disk and load/transform data as needed during training by leveraging multiple processes to format and load data. 

In this example, we will use bitcoin timeseries data and create our own data loader. Please note that this demo focuses on how to utilize custom datasets and data loaders in PyTorch for tabular data, and will not implement or train any neural network.  

In the future I will provide a better example of using a custom dataset to train a neural network. 


Demo Steps:
1. Download and install all required Python Libraries. 
    1. Python 3.7
    1. Pip Install using [requirements.txt](requirements.txt)
    1. [PyTorch Installation](https://pytorch.org/) help
1. [Download HDF5 data](download_hdf5_data.py)
    - HDF5 files can live on disk but still be accessed like a numpy array (indexing, slicing), which means you can still shuffle batches etc. without loading the whole dataset into ram.
1. [Run `run.py`](run.py)



Blogs I found helpful for learning:
- [Towards Data Science Blog](https://towardsdatascience.com/building-efficient-custom-datasets-in-pytorch-2563b946fd9f)
- [PyTorch Discussion](https://discuss.pytorch.org/t/dataset-class-loading-multiple-data-files/47789/2) 
- [PyTorch Data Loading Tutorial](https://pytorch.org/tutorials/beginner/data_loading_tutorial.html)
- [Standford Blog](https://stanford.edu/~shervine/blog/pytorch-how-to-generate-data-parallel)
- [Tabular Data with PyTorch](https://towardsdatascience.com/better-data-loading-20x-pytorch-speed-up-for-tabular-data-e264b9e34352)
- [Iterative Dataset Documentation](https://pytorch.org/docs/stable/data.html#torch.utils.data.IterableDataset)
- [hdf5 files in python](https://www.pythonforthelab.com/blog/how-to-use-hdf5-files-in-python/)


# Code Notes

After following the demo steps above, you should have a working code base for a hello world example of a PyTorch custom dataset. There is a LOT more capabilities that can be done with this, and I plan to continue this in more PyTorch examples. But I would like to highligh a few pieces of code that are important to know when working with hdf5 files in PyTorch.  

In my custom dataset you will notice that there are three functions that are required for a custom PyTorch Dataset: `__init__`, `__len__` and `__getitem__`. In both of these functions we create an hdf5 file object in Python. This will allow us to interact with our hdf5 file on disk. At first, I wanted to create this object in the `__init__` function so that I only had to load the file a single time, however, I found that hdf5 file objects cannot be shared across processes in Python (which makes total sense due to the GIL). So that means each of the internal functions have the following code: 
```python
hf = h5py.File(self.__data_path, 'r')
data = hf.get(self.__identifier)[:]
hf.close()
```

This allows us to use the `num_workers` argument when we create our DataLoader in our `run.py` file. The `num_workers` allows us to use separate processes to load data efficiently. 
```python
dataloader = DataLoader(dataset, batch_size=4, shuffle=True, num_workers=2)
```

If I had kept the file loading in the `__init__` function like I originally planned I would never be able to have `num_workers` > 0. 



# HDF5 Notes

I have not used HDF5 files a lot, so I took some notes that I found useful. 

The following are my notes taken from this [blog](https://www.christopherlovell.co.uk/blog/2016/04/27/h5py-intro.html#:~:text=Reading%20HDF5%20files,method%20in%20read%20mode%2C%20r.&text=To%20see%20what%20data%20is,method%20on%20the%20file%20object.&text=We%20can%20then%20grab%20each,get%20method%2C%20specifying%20the%20name.&text=This%20returns%20a%20HDF5%20dataset%20object.). 

HDF5 is a binary data format without an upper limit of file size. With parallel IO and other optimizations allow for efficient queries on larger datasets. We will use the [`h5py`](http://www.h5py.org/) package to read and write data in Python. 

To create a hdf5 file in python you must complete the following:
```python
# import libs
import numpy as np
import h5py

# create data
d1 = np.random.random(size = (1000,20))
d2 = np.random.random(size = (1000,200))

# Create the file object in Python
hf = h5py.File('data.h5', 'w')

# save the two datasets to the hdf5 file. 
## IMPORTANT!!!! ## 
# We are saving two datasets to a single file. We access the datasets separately with their names i.e. 'dataset_1' and 'dataset_2'
hf.create_dataset('dataset_1', data=d1)
hf.create_dataset('dataset_2', data=d2)

# close the object write
hf.close()

```


Then to read the data we will need to complete the following:
```python
import numpy as np
import h5py

# create a file object
hf = h5py.File('data.h5', 'r')

# we can get the data using the `get` method
d1 = hf.get("dataset_1")

# format it as numpy array
np_arr = np.array(d1)

# close the dataset
hf.close()
```


## Groups 

Groups are the basic container mechanism in a HDF5 file, allowing hierarchical organisation of the data. Groups are created similarly to datasets, and datsets are then added using the group object.

We can see the groups by use the `keys()` method. 
```python
d1.keys()
>>> <KeysViewHDF5 ['dataset_1', 'dataset_2']>
``` 

By default datasets will be added to their own group, but you can create a data hierarchy using the `create_group` method and adding datasets to that group. 
```python
g2 = hf.create_group('group2/subfolder')

g2.create_dataset('data3',data=d2)
```


## Compression

To reduce the file size on disk we can compress the data. NOTE - this will reduce the speed at which you can read the data. 
```python
hf = h5py.File('data.h5', 'w')

hf.create_dataset('dataset_1', data=d1, compression="gzip", compression_opts=9)
hf.create_dataset('dataset_2', data=d2, compression="gzip", compression_opts=9)

hf.close()
```