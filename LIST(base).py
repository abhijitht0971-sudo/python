# # python list 
# a=[1,2,3,4,5]
# print(type(a),a)
# # accessing list item 
# b=["me","you","us"]
# print(b[1])
# print(b[-1])
# print(b[1:3])
# a[1:3]=["b","c"]
# print(a)
# # adding items
# # append
# c=["grapes","orange","papaya"]
# c.append("fig")
# print(c)
# # insert
# c.insert(2,"guava")
# print(c)
# # extend
# d=["apple"]
# c.extend(d)
# print(c)
# # removing items 
# # remove
# a=["abac","def","ghi"]
# a.remove("def")
# print(a)
# # pop
# a=["abc","def","ghi"] 
# b=a.pop(1)
# print(b)
# print(a)
# # del 
# a=["abc","def","ghi"]
# del a[0]
# print(a)
# # clear
# a=["abc","def","ghi"]
# a.clear()
# print(a)
# # list methods 
# a=["abc","def","ghi"]
# print(a.count("abc"))
# print(a.index("ghi"))
# a.reverse()
# print(a)
# a=[2,3,1]
# a.sort()
# print(a)
# a=[2,3,1]
# b=a.copy()
# print(b)
# # sorting list 
# a=[1,3,5,4,7]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# # joining list 
# a=["abc","def","ghi"] 
# b=['1,2,3,4,5']
# c=a+b 
# print(c)
# # extend
# a.extend(b)
# print(a)

# list comprehension

# n= 10
# even=[]
# odd=[]
# for i in range(1,n+1):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(even)
# print(odd)

# n=10
# a=[x**2 for x in range(1,n+1) if x%2==0]
# b=[x for x in range(1,n+1) if x%2!=0]
# print(a)
# print(b)

# a=["jane","roy","ben"]
# b=[i.upper() for i in a]
# print(b)