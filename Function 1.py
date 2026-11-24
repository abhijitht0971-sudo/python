# Functions

# definition
# def greet():
#     print("heyy")

# calling
# greet()
    
# parameters:variables listed in the function definitions
# def greet(name):
#     print(f"hey {name}")
# # arguments:value passed when function is called
# greet("vishnu")
# greet("ajay")

# types of arguments

# positional arguments
# def greet(name,age,city):
#     print(f"hey {name} your age is {age} and your city is {city}")

# greet("ajay",22,"newyork")

# keyword argument
# def greet(name,age,city):
#      print(f"hey {name} your age is {age} and your city is {city}")

# greet(city="venue",name="ajay",age=21)

# default arguments
# 
# variable length arguments
# arbitrary arguments
# def num(*a):
#     print(a)

# num(1,2,3,43,4,5,6,7,77,8,88,0)

# arbitrary keyword arguments
# def detail(**dic):
#     print(dic)
# detail(name="siya",age=21,city="aster",country="denmark")

# def details(name,*args,**kwargs):
#     print(name)
#     print(args)
#     print(kwargs)
# details("eby",2,3,4,2,4,0,9,"leno",a=21,n=11,o=90)

# def less(a,b):
#     return a-b
# sub=less(20,10)
# print(sub)

# adding

# def sum(*n):
#     total=0
#     for i in n:
#         total+=i

#     return total 
# print(sum(1,2,3,4,5,6,7,8,9))