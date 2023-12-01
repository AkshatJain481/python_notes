class student:
  
    def __init__(self,N,A,R): #constructor
        self.Name = N # Name variable will be created and 'N' will be passed into it (same for below two variables)
        self.Age = A
        self.Rollno = R


a = student('Akshat',18,2211009)
print(a.Name)
print(a.Rollno)
print(a.Age)

# Decorators
def modification(x):
    def fun_to_be_returned(*xy,**xyz):
        print("do some task before the function is executed")
        x(*xy,**xyz)
        print("Tasks after execution of the function")
    return fun_to_be_returned

@modification
def fun(x,y):
    print(f"sum is {x+y}")

fun(10,21)    

#getters and setters
#getter can help you use the variables in the object for calculation and return when called without having to make any other variable and store it
class example:
    def __init__(self ,value):
        self.val = value
    def display(self):
        print(f"this is the value:- {self.val}")
    @property
    def value_multiplication_by_10(self):
        return (self.val *10)
    @value_multiplication_by_10.setter
    def value_multiplication_by_10(self,value):
        self.val = self.val*value


obj_of_example = example(21)
obj_of_example.display()
print(obj_of_example.value_multiplication_by_10) # it will only get it,NOT set any value 
obj_of_example.value_multiplication_by_10  = 2 #it will set the value in the object
print(obj_of_example.val) 
# all variables and methods are public in python in classes
# self.__variableName can not be accessed directly
# class inheritance
#syntax:- 
# class class_name(inherited_class_name):
# now you can use the methods and init of the 'inherited_class_name' by making an object of 'class_name'
class access_modifiers:
    def __init__(self, n, ag):
        self.__name = n
        self.__age = ag
    def show(self):
        print(f"{self.__name} \n {self.__age}")
    @staticmethod # '@staticmethod' before function declaration will make the function a normal function and will not need 'self' variable passed in it.
    def add(a,b):
        return a+b
        
x = access_modifiers('Akshat', 18)
x.show()
try:
    print(x.__name) # cannot be accessed as the __name variable is private
except:
    print(x._access_modifiers__name) # private variable can be accessed outside the class in python using this method
print(access_modifiers.add(10,20))  
print(x.add(19,21))  

                  




        