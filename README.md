# GeneralPythonExamples
This repository contains example Python code for various patterns, functions, and libraries. This repository is mostly for personal note keeping so that I can easily reference pieces of code that I have written in the past. I make the repository public in case anyone finds it useful for a "hello world" walkthrough of a topic. 

## Examples

- [Threading](threadingExample)
    - Python does experience a global interpretter lock, meaning that only one workflow can execute at a time. However, there are specific tasks or applications that can benefit from the [thread python library](https://docs.python.org/3/library/threading.html). 


- [Singleton Software Pattern](singletonExample)
    - Often times in software we have objects that we share across different classes and functions. While we still need to intialize classes with these shared objects, it can become a nusiance to allows have to update values between the classes that share it's properties. A singleton pattern allows objects to share and broadcast updates to all classes that have an instance of the shared object. 


- [Multiprocessing](multiprocessingExample)
    - When developers need to get around the global interpretter lock, the [base multiprocessing library](https://docs.python.org/3/library/multiprocessing.html) and python will solve your problems, 


- [Super/Child Classes](superClass/README.md)

- [PyTorch](PyTorch)
    - I use PyTorch a lot in my day to day work. As I get more comfortable with the library I plan on keeping notes/examples here that I took me a while to figure out. I do not plan on keep examples that are easily found on other documentation pages unless I executed the code personally. Examples Include:  
        - LSTM for time series data
        - Hello World Custom Data Loaders  
        - LSTM with Custom Dataset 
        - Generative Adversarial Networks 


## Contact 

I do not claim to be an expert in the above topics; however, if there are any questions, updates, or comments please feel free to contact me at ryanachynoweth@gmail.com. 
