from singletonExample.singletonClass import MySingleton
from singletonExample.environmentClass import environment

# create the singleton object in our entry script
s = MySingleton(1, 2)
print(s.val1)
print(s.val2)

# share the singleton object to the environment class
e = environment(s, a=3, b=4)

# update the val1 and val2 values
e.mySingleton.val1 = 5
e.mySingleton.val2 = 6


# print the values of our object again. 
# notice we updated the e.mySingleton object and we are printing the s object here
print(s.val1)
print(s.val2)


# note that if we have another terminal open sharing the same anaconda virtual environment
# and we create another instance of this class that terminal will share the same values as well.