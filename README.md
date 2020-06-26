# GeneralPythonExamples
This repository contains example Python code for various patterns, functions, and libraries. This repository is mostly anote keeping repository so that I can easily reference pieces of code that I have written in the past. I make the repository public in case anyone finds it useful for a "hello world" walkthrough of a topic. 

## Examples

- Threading
    - Python does experience a global interpretter lock, meaning that only one workflow can execute at a time. However, there are specific tasks or applications that can benefit from the [thread python library](https://docs.python.org/3/library/threading.html). 
    - [Write Up](threadingExample/README.md)

- Singleton Software Pattern
    - Often times in software we have objects that we share across different classes and functions. While we still need to intialize classes with these shared objects, it can become a nusiance to allows have to update values between the classes that share it's properties. A singleton pattern allows objects to share and broadcast updates to all classes that have an instance of the shared object. 
    - [Write Up](singletonExample/README.md)

- LSTM Neural Network (Timeseries)
    - [Write Up](LSTM/README.md)

- Multiprocessing
    - When developers need to get around the global interpretter lock, the [base multiprocessing library](https://docs.python.org/3/library/multiprocessing.html) and python will solve your problems, 
    - [Write Up](multiprocessingExample/README.md)

- Super/Child Classes
    - [Write Up](superClass/README.md)


## Contact 

I do not claim to be an expert in the above topics; however, if there are any questions, updates, or comments please feel free to contact me at ryanachynoweth@gmail.com. 
