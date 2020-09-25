# Generative Adversarial Networks

Please note that this is my first time training GANs, therefore, most of what I claim to be true in this directory is my current/previous understanding.   

Here are a few great examples that I used to learn:
- This example is created using [DCGAN tutorial](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html#introduction) as a reference. This example is purposed towards using GANs for time series analysis, therefore, we will also leverage some of our code from the [LSTMWithCustomerDataset](../../LSTMWithCustomerDataset/README.md) example. 
- Another great resource from GitHub on using [GANs for Timeseries with PyTorch](https://github.com/proceduralia/pytorch-GAN-timeseries).


## Overview

GANs are a framework for teaching a DL model to capture the training data’s distribution so we can generate new data from that same distribution. They are made of two distinct models, a generator and a discriminator. The job of the generator is to create sequences that appear to be from the training dataset. The job of the discriminator is to look at a sequence and determine whether or not it belongs in the training dataset distribution. The goal of the process is for the generator to create sequences that look as if it came directly from the training dataset. 


Training GANs are a bit different than training other neural networks. The training loop for GANs is split into two parts: training the discriminator and training the generator. 

The goal of training the discriminator is to maximize the probability of correctly classifying a given input as real or fake. The goal of training the generator is to create the best "fake" data as possible so that we can trick the discriminator into thinking it is real data. 


Our training loop completes the following steps.  
1. Forward pass the discriminator with real data and assign "1" as the label. 
2. Calculate loss and perform backward pass on the discriminator. 
3. Take sample input data from our training set and forward pass through the generator. 
4. Forward pass the discriminator using the output of step #3, and assign "0" as the label since the data is "fake". 
5. Calculate loss and perform backward pass on the discriminator. 
6. Forward pass the output of step #3 once more through the discriminator.
    - Technically another forward pass is not required as you can use the same loss from step #5
7. Calculate loss and perform backward pass on the generator 
    - Notice that we are essentially using the discriminator as the loss function for the generator. 


In many cases of GANs we will typically pass in random data into the generator network to produce a random output (i.e. image) to fake out the discriminator (Step #3 and #4). In the case with time series it is important that we pass in real sequences so that when we go too apply the model in practice we can pass in current time series data and produce a forecast. Essentially instead of using a loss function like `nn.MSELoss()` we use the discriminator as our loss function. Often when random input is used for GANs it is because we are attempting to produce fake images, therefore, the random input os required.    


## Steps to reproduce

NOTE: Code should be executed from the root of the repository.  

Run the scripts in the following order:  
- [create_dataset](create_dataset.py): to create the dataset for training.
- [train networks](train.py)
- [test the network](test.py)

### Results

The generator network (LSTM), is forecasting 10 data points at a time. This means that to produce the visual below we provide 42 actual data points from our dataset. Then we would skip 10 points and add our prediction to the input dataset, meaning the second iteration would have 32 actual data points but 10 predictions to follow. As you can see we were able to reproduce the sine wave dataset very accurately (which is not surprising).   


![](imgs/predictions.png)