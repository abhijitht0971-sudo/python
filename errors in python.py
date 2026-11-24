# syntax error 
# print("helo"

# zero division error 
# a= 15
# b=0
# print(a/b)

# name error 
# a={name:adam}
# print(a)

# value error 
# a=[1,2,3,4]
# a.remove(7)
# print(a)

# index error 
# a=[1,2,3,4,5]
# a[6]

# key error 
# a={"name":"joel","age":21}
# print(a["city"])

# file not found error 
# file=open("sample.txt")

# exception handling
# syntax 
# try:

#     x=10/0
# except ZeroDivisionError:
#     print("you can't divded by zero")

# a=15
# b=0
# try:
#     c=a/b
# except Exception as e:
#     print(e)
# else:
#     print("the result is",c)
# finally:
#     print("this will always be printed")

# raise Exception
# a=-15
# if a>0:
#     print("positive")
# else:
#     raise ValueError("negative numbers not allowed")

# custom exception 
# class abcderror(Exception):
#     pass

# a=-10
# if a>0:
#     print("positive")
# else:
#     raise abcderror("negative numbers not allowed")