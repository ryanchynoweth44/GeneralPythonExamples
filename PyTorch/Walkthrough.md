# Creating a PyTorch Custom Dataset

The PyTorch `Dataset` class is extremely flexible as there are only two requirements when writing your own custom dataset class. Developers must override the:
- `__len__` function which returns the size of the dataset (number of rows). 
- `__getitem__` function that returns a sample from the dataset when given an index value. 

