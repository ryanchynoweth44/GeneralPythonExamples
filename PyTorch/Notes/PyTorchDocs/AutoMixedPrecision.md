# Automatic Mixed Precision Examples

Mixed precision is the combined use of different numerical precisions in a computational method in order to achieve the same accuracy in some as single-precision training using the same hyper-parameters. Memory requirements are also reduced, allowing larger models and minibatches.

Please reference the folloiwng PyTorch [documentation](https://pytorch.org/docs/stable/notes/amp_examples.html).


## Typical Training Loop

**Essentially, allows for a better optimized training procedure without losing any accuracy of your model**.  

In PyTorch we can use the `torch.cuda.amp.autocast` module to enable autocasting for chosen regions. Autocasting automatically chooses the precision for GPU operations to improve performance while maintaining accuracy. `torch.cuda.amp.GradScaler` can be used to improve convergence for networks with `float16` gradients by minimizing gradient underflow.  

My current training loop for PyTorch networks typically look like the following:
```python
net = Net() # an extension of nn.Module

loss_func = nn.MSELoss()
optimizer = optim.Adam(net.parameters(), lr=0.001)

for i in range(0, 10):
    for x, y in dataloader:
        optimizer.zero_grad()
        output = net(x))
        loss = loss_func(output, y)
        loss.backward()
        optimizer.step()
```


## Mixed Precision Example
The main items to call out in the code snippet above:
- `optimizer.step()` performs a parameter update based on the current gradient. 
- `loss.backward()` accumulates the gradient for each parameter. This is the reason why we call `optimizer.zero_grad()` before each of our forward passes (or after each the `optimizer.step()`).  

By altering the training loop to have the following, we are able to implement a standard mixed precision process with practically the same amount of code. The main difference is that we are wrapping our `loss.backward()` and `optimizer.step()` calls in a scaler object to allow for mixed precision.  
```python
net = Net()  # an extension of nn.Module
optimizer = optim.SGD(net.parameters(), lr=0.001)

# Creates a GradScaler once at the beginning of training.
scaler = GradScaler()

for i in range(0, 10):
    for x, y in dataloader:
        optimizer.zero_grad()

        # Runs the forward pass with autocasting.
        with autocast():
            output = model(input)
            loss = loss_fn(output, target)

        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()
```

Few notes on the above:
- `scaler.scale(loss).backward()` calls `backward()` on a scaled loss to create scaled gradients. Please note how this call is not under the `with autocast()` since that is not recommended. 
    - There are scenarios for unscaling your gradients i.e. gradient_clipping so you may want to use `scaler.unscale_(optimizer)`. 
    - **Gradient Clipping** is used mostly in recurrent neural networks to avoid exploding gradients in deep neural networks. Gradient clipping sets a pre-determined gradient threshold and when gradients exceed this threshold they are scaled down to match the norm.  This prevents any gradient to have norm greater than the threshold and thus the gradients are clipped.  
- `scaler.step(optimizer)` will first unscale the gradients of the optimizer to assign weights. If the gradients do not contain `infs` or `NaNs` then `optimizer.step()` is called, otherwise it is skipped. 
- `scaler.update()` updates the scale for the next iteration. 


**Gradient accumulation** is the process of adding gradients over a number of iterations which effectively increases the batch size by allowing microbatches to accumulate into larger batches before updating the network parameters. 

NOTE - **Batch Size** controls the accuracy of the estimate of the error gradient when training neural networks. As a general rule of thumb, small batch sizes usually result in faster learning but a volatile learning process with higher variance in the classification accuracy. Larger batch sizes slow down the learning process but the final stages result in a convergence to a more stable model exemplified by lower variance in classification accuracy.

**Gradient penalty** is a process that helps avoid exploding gradients. 