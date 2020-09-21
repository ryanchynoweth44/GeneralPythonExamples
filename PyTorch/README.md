# PyTorch Examples

In this directory I will maintain a set of PyTorch examples to highlight features of the package in basic applications. These features can easily be extended to handle much more complex modelling solutions.  

- [CustomDataLoaders](CustomDataLoaders)
    - An explaination on how to create your own custom dataset and use the data loader module for efficient data transformations and network training. I also give a brief overview of hdf5 files using the [h5py](http://www.h5py.org/) package. 

- [HelloWorld_LSTM](HelloWorld_LSTM)
    - An official PyTorch example for timeseries data. 

- [LSTMWithCustomDataset](LSTMWithCustomDataset)
    - Based off the HelloWorld_LSTM example from PyTorch, I create my own custom dataset and train an LSTM to predict the sine wave.  

- [Generative Adversarial Networks](GAN)
    - Using the sine wave dataset used in other examples, we train a generator network (LSTM) to produce data and a discriminator network (CNN) to judge the accuracy of the predictions.  

- [Notes](Notes/README.md)
    - Various notes about PyTorch best practices or neural network trips for better performing networks. 