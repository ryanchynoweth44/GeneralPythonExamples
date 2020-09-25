# Introduction to Neural Networks

In this basic introduction we will cover Multilayer Perceptrons (MLP), Recurrent Neural Networks (RNN), and Convolutional Neural Networks (CNN) at a high level. We will emphasize key components of each type of network as well. 


## MLP

Multilayer Perceptrons are feedforward networks with a minimum of three layers (input, hidden, and output). Specifically it is common to see these networks as fully connected which means that each node in one layer is connected to every node in the following layer.

Except for the input layer each layer is uses a nonlinear activation function. An activation function is the function used to map the inputs of a neuron to the outputs. The reason for using a non-linear activation function is simply because if linear functions are used then we can theoretically reduce the network to a simple two layer network. 

Each node takes inputs, multiplies the inputs by weights, and sums the values. The summed value is then put through an activation function. 

The most common activation functions are:
- Linear: no activation is applied.  

- Sigmoids: a logistic function, is traditionally a very popular activation function for neural networks. The input to the function is transformed into a value between 0.0 and 1.0. This results in an s-shaped curve with the middle being 0.5. 

- tanh: a nonlinear activation function that is similar to the sigmoid function but maps inputs between -1 and 1, and has a similar curve shape. 

- ReLu (Rectifier Linear Unit): a piecewise linear function that will output the input directly if it is positive, otherwise, it will output zero. This is in contrast to the sigmoid activation function which won't allow values larger that 1, ReLu does. 
    - This has become the default activation function


The issue with the sigmoid and tanh functions is that they tend to saturate output values around the poles i.e. 1 and 0/-1. Therefore, they are really only sensitive to changes in the middle of the function. Once a network is saturated it is difficult for it to continue learning. These functions also suffer greatly from the vanishing gradient problem with deep neural networks. 

ReLu is an activation function acts like a linear function, but is, in fact, a nonlinear function allowing complex relationships in the data to be learned. ReLu is used with MLPs and CNNs. 

An MLP is a connect set of layers the employ activation functions to feed as inputs into the next layer. The input layer is determined by the number of input features, while the output layer is typically use a softmax function for classification or simply a linear activation function for regression problems. Additionally, you will likely use a crossentropy loss function for classification but MSE for regression. 


## RNN 

Great [article](https://towardsdatascience.com/illustrated-guide-to-recurrent-neural-networks-79e5eb8049c9) on RNNs and another one on [LSTMs and GRUs](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21).

RNNs are widely used for problems that can be modelled using a sequential memory technique. As with feed-forward networks we have out input, output, and hidden layers, but our goal is to get the hidden layers to use previous information in the sequence to assist in the output value. 

The ability for an RNN to use previous information in the current time sequence is accomplished using a loop, which we call the hidden state. The hidden state is a representation of the previous inputs. This hidden state weights past observations so that the more recent inputs are taken into account more than the older ones which can be an issue that we call "short-term" memory. This can lead to a vanishing gradients using backpropagation, however, we can solve this using a slightly different technique called backpropagation through time. 

This is where LSTMs and GRUs come into play. Each of these types of neural networks use a gate method to learn which information should be added to the hidden state. 

### Long Short Term Memory (LSTM)
- Cell State: the cell state is the memory of the network which transfers information. The cell state is altered by the gates of the cell which learn which information is relavent and which information is not. 
- Gates: Are different neural networks that decide which information is allowed on the cell state. The gates can learn what information is relevant to keep or forget during training.

Gates contains sigmoid activations. A sigmoid activation is similar to the tanh activation. Instead of squishing values between -1 and 1, it squishes values between 0 and 1. That is helpful to update or forget data because any number getting multiplied by 0 is 0, causing values to disappears or be “forgotten.” Any number multiplied by 1 is the same value therefore that value stay’s the same or is “kept.” The network can learn which data is not important therefore can be forgotten or which data is important to keep.

**Forget Gate**: Takes input from the **previous hidden state and current input** and applies a sigmoid function to determine which information should be kept (1) and which is forgotten (0). 

**Input Gate**: Takes the input from the **previous hidden state and current input** and apply a sigmoid and tanh function separately. The output of these two functions is multiplied to determine what information to keep. 

**Cell State**: first we multiply the cell state by the output of the forget gate. Then the output of the multiplication is added to the output of the input gate. This process gives us our new cell state. 

**Output Gate**: After updating the cell state, we need to determine the what the next hidden state should be. To do so we take the input from the **previous hidden state and current input** and apply a sigmoid function. We take the current cell state and apply a tanh function to which we then multiply these outputs. The output of this multiplication is the new hidden state and the current cell state is kept for the next time step. 

- The Forget gate decides what is relevant to keep from prior steps. 
- The input gate decides what information is relevant to add from the current step. 
- The output gate determines what the next hidden state should be.


### Gated Recurrent Units (GRU): 

GRU networks are very similiar to LSTM and are considered the next evolution of the LSTM. GRU networks got rid of the cell state and used the hidden state to transfer information. It also only has two gates, a reset gate and update gate.

The **update gate** acts similar to the forget and input gate of an LSTM. It decides what information to throw away and what new information to add.

The **reset gate** is another gate is used to decide how much past information to forget.


### Stacking LSTMs or GRUs

LSTMs and GRUs are often efficient enough on their own to have a single LSTM or GRU Network. However, there may be advantages to stacking LSTMs in order to add levels of abstraction of input observations over time. For example, in PyTorch we can use [`torch.nn.LSTM`](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html#torch.nn.LSTM) to create an LSTM network, and we can use the `num_layers` argument to stack LSTMs. 


## CNN 

Helpful Links: 
- https://towardsdatascience.com/convolutional-neural-networks-part-1-2aeb17fc208c
- https://arxiv.org/pdf/1603.07285v1.pdf

Convolutional Neural Networks leverage convolutional layers, prior to processing the data through a set of linear layers to produce the output. 

**Convolutional layers** apply a set of filters to input data to create a feature map that summarizes the presence of detected features. This is essentially a data transformation procedure that can be processed by linear layers. The main components of convolutional layers are: 
- input_channels: the depth of the input data i.e. grayscale = 1 and RGB = 3.
- output_channels: the number of kernels/filters the layer applies to the input data
- kernel_size: the `m x n` size of the matrix used to apply the filter. 
- stride: the step size used when applying filters to input data
- padding: a strategy designed to add zeros to the boarder of input data so that the edges of the data are not weighted less than the rest of the input. 

There are three types of convolutional layers:
- 1-D Convolution:
- 2-D Convolution:
- 3-D Convolution: 