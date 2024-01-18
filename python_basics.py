#Creating variables
greeting = 'Hello '
print(greeting + 'Mario')

#Constants. In python there are not explicit constants, the convention is that consants are declared in UPPERCASE
PI = 3.141592

#Data types
    #Basic types
text = "text" #This is a string
integer = 10 #This is an integer
_float = 10.5 #This is a float
complex_number = 8j #This is a complex number
    #Sequence types
people = ['Mario','Luigi'] #This is a list
lotto_numbers = (1,2,3,4,5,6) #This is a tuple. Tuples cannot be changed once created
numbers = range(1,10) #This is a range
users = {'name':'Mario','game':'Mario Bros'} #This is a dictionary
unique_numbers = {1,2,2,3,3,3,4} #This is a set, when executed will only contain the unique values. It does NOT keep the order
boolean = True #This is a boolean, only can have True/False value
_none = None #This is a empty (null) value

#Adding type hints
name: str = 'Mario' #Explicitly tell python what variable type the variable is. It does not constrain the datatype, it can be changed still

#Type conversion
name = 'Mario'
number = 10

print(name + str(number))