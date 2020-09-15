# Distributed Data Parallel 

These notes are for pytorch version 1.4: https://pytorch.org/docs/stable/notes/ddp.html

The `torch.nn.parallel.DistributedDataParallel` (DDP) library can be utilized parallel training of a network. 

The process essentially requires a our training loop to be wrapped in a Python function. Within the training loop there is a local model (i.e. your defined network) that is wrapped around a `DDP` object i.e. `DDP(model)`. This function will complete a forward and backward pass on the local model, then broadcasts the `state_dict()` to the other processes. The parameters are shared between models using buckets to be updated at the same time.  

Here is the simple example from the documentation:
```python
import torch
import torch.distributed as dist
import torch.multiprocessing as mp
import torch.nn as nn
import torch.optim as optim
from torch.nn.parallel import DistributedDataParallel as DDP


def example(rank, world_size):
    # create default process group
    dist.init_process_group("gloo", rank=rank, world_size=world_size)
    # create local model
    model = nn.Linear(10, 10).to(rank)
    # construct DDP model
    ddp_model = DDP(model, device_ids=[rank])
    # define loss function and optimizer
    loss_fn = nn.MSELoss()
    optimizer = optim.SGD(ddp_model.parameters(), lr=0.001)

    # forward pass
    outputs = ddp_model(torch.randn(20, 10).to(rank))
    labels = torch.randn(20, 10).to(rank)
    # backward pass
    loss_fn(outputs, labels).backward()
    # update parameters
    optimizer.step()

def main():
    world_size = 2
    mp.spawn(example,
        args=(world_size,),
        nprocs=world_size,
        join=True)

if __name__=="__main__":
    main()
```