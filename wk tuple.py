# # python tuples
# # accessing tuple items
# a=(1,1,2,3,4,"ab","bc")
# print(a[2])
# print(a[-1])
# print(a[2:5])
# # updating a tuple 
# # reassingning
# a=(1,2,3,4)
# a=(8,9,0,1)
# print(a)
# # convert tuple to list 
# a=(99,80,89,77)
# b=list(a)
# b[1]=79
# a=tuple(b)
# print(a)
# # unpacking tuples
# a=("as","an","and","are")
# (w1,w2,w3,w4)=a
# print(w1)
# print(w2)
# print(w3)
# print(w4)
# # using *asterisk
# a=("as","an","and","are")
# (first,*middle,last)=a
# print(first)
# print(middle)
# print(last)
# # joining tuple 
# a=(9,9,0,8,7)
# b=(2,3,1,6,8)
# c=a+b
# print(c)
# # tuple methods
# # count
# a=(9,9,0,8,7)
# print(a.count(9))
# # Index
# b=(2,3,1,6,8)
# print(b.index(8))
# # deleting a tuple 
# b=(2,3,1,6,8)
# del b
# print(b)