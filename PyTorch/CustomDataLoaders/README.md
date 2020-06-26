# PyTorch Custom Data Loaders

PyTorch data loaders are an excellent way to batch and process your data for deep learning algorithms. 

One huge advantage to using Data Loaders is the developers ability to customize and create their own loaders, espcially when data is larger in size or if data is unsually formatted. A custom data loader allows engineers to keep data on disk and load/transform data as needed during training. 

In this example, we will use bitcoin timeseries data and create our own data loader. Please note that this tutorial focuses on how to utilize custom datasets and data loaders in PyTorch for tabular data, and will not implement or train any neural network.  


Demo Steps:
1. Download and install all required Python Libraries. 
    1. Python 3.7
    1. Pip Install using [requirements.txt](requirements.txt)
    1. [PyTorch Installation](https://pytorch.org/) help
1. [Download data](download_data.py) from Coinbase Pro (No API Key required)
1. [Create a custom dataset](btc_custom_dataset.py)


My references:
- [Towards Data Science Blog](https://towardsdatascience.com/building-efficient-custom-datasets-in-pytorch-2563b946fd9f)
- [PyTorch Documentation](https://pytorch.org/tutorials/beginner/data_loading_tutorial.html) 

