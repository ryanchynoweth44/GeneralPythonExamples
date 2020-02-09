from superClass.subClass import SubClass



s = SubClass(1, 2, 3, 4)

## access the parent class function
s.superFunction(addition=20)

## use the subclass function that replaces the superclass function
s.overwriteFunction()

## use the subclass function that calls the parent function 
s.anotherfunction(addition=40)

