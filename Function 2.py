# def add(a,b):
#     return a+b
# print(add(2,3))

# add=lambda a,b:a+b
# print(add(2,3))

# # function scope
# a=20 #global variabe
# def bb():
#     a=11 #local variable
#     print(a)
# bb()
# print(a)

# user defined module 
# import module.modules as m
# print(dir(modules))
# m.greet("henry")
# from modules import greet
# import modules as m
# print(m.greet1("jake"))

# standard library

# import math

# print(math.pi)
# print(math.pow(2,3))
# print(math.factorial(6))

# import datetime
# now=datetime.datetime.now()
# print(now)

# import calendar
# print(calendar.calendar(2027))
# print(calendar.isleap(2024))
# print(calendar.month(2026,12))

# import random
# a=random.randint(1,20)
# print(a)

# import os
# print(os.getcwd())
# print(os.name)

# shutdown
# os.system("shutdown /s /t 0")

# import sys
# print(sys.version)

# import json 
# a={"name":"kevin","age":21}
# print(a,type(a))
# b=json.dumps(a)
# print(b,type(b))

# a='{"name":"kevin","age":21}'
# print(a,type(a))
# b=json.loads(a)
# print(b,type(b))

# json.dumps :python to json
# json.loads :json to python 

# third party libraries
# numpy
# import numpy as np
# # print(np.__version__)

# a=np.array([[12,1,2,3],[4,3,2],[5,6,7]])
# print(a,type(a))
# print(a.shape)
# print(a[[1],[1]])

# pandas 
# import pandas as pd
# # print(pd.__version__)
# df={'name':['a','b','c','d'],
#     'age':[20,21,22,23],
#     'salaray':[1000,2000,3000,4000]}
# a=pd.DataFrame(df,index=[1,2,3,4])
# print(a)

# matplotlib
# import matplotlib.pyplot as plt

# x=[1,2,3,4]
# y=[8,6,7,4]

# plt.plot(x,y)
# plt.show()

# requests
# import requests
# a=requests.get("https://www.google.com")
# print(a.status_code)
