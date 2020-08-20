# AutoGrad Mechanics

[PyTorch Documentation.](https://pytorch.org/docs/stable/notes/autograd.html) 

The ability to freeze gradients is important for fine-tuning neural networks. For example if you want to finetune a pretrained CNN, it’s enough to switch the requires_grad flags in the frozen base, and no intermediate buffers will be saved, until the computation gets to the last layer, where the affine transform will use weights that require gradient, and the output of the network will also require them.


It is important to understand that every Tensor has a flag: requires_grad that allows for fine grained exclusion of subgraphs from gradient computation and can increase efficiency.
```python
x = torch.randn(5, 5)  # requires_grad=False by default
y = torch.randn(5, 5)  # requires_grad=False by default
z = torch.randn((5, 5), requires_grad=True)
a = x + y
a.requires_grad
>>> False
b = a + z
b.requires_grad
>>> True
```


User could train their model with multithreading code (e.g. Hogwild training), and does not block on the concurrent backward computations, example code could be:
```python
# Define a train function to be used in different threads
def train_fn():
    x = torch.ones(5, 5, requires_grad=True)
    # forward
    y = (x + 3) * (x + 4) * 0.5
    # backward
    y.sum().backward()
    # potential optimizer update


# User write their own threading code to drive the train_fn
threads = []
for _ in range(10):
    p = threading.Thread(target=train_fn, args=())
    p.start()
    threads.append(p)

for p in threads:
    p.join()
```

If you are using the multithreading approach to drive the whole training process but using shared parameters, user who use multithreading should have the threading model in mind and should expect gradient accumulation to become non-deterministic on backward calls across threads to happen. User could use the functional API `torch.autograd.grad()` to calculate the gradients instead of `backward()` to avoid non-determinism.

