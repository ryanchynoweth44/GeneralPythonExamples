# Using Parent and Child Classes in Python 

All software development projects will result in some number of classes being created to support the solution and there is bound to be some sort of inheritance that takes place. For me, I often use a super class and sub class in my python projects in order to obtain the following functionality. 
- The ability to substitute attributes and functions of a specific class based on functionality
- The ability to utilize functions and attributes from a superclass in a subclass
- The ability to override functions and attributes in a superclass from a subclass 


In this short example I have created two classes:
- [`superClass.py`](superClass.py): the parent class that I intend to augment with a child class. 
- [`subClass.py`](subClass.py): the child class that I intend to extend the parent class with. 


In order to run the `main.py` code you should be in the root repository so that the class imports execute as expected. You will notice the following code. Please reference the detailed comments in order to learn more about the set up of the classes. 

```python
## import ONLY the subclass as we will utilize the parent class
## variables and functions through the inheritance. 
from superClass.subClass import SubClass

## create a subclass object. Note that the subclass will pass the required variables/parameters
## to the parent class
s = SubClass(1, 2, 3, 4)

## the "superFunction" is only available in the parent class. 
## you will notice that we are able to call a parent clas function with a child class object. 
s.superFunction(addition=20)

## the "overwriteFunction" is present in both the parent and child classes. 
## you will notice that there is a difference in what values will be ommited 
s.overwriteFunction()

## This function is only available in the subclass 
## however this function is dependent on a parent class function
s.anotherfunction(addition=40)

```


There is a quick overview of class inheritance in python! 