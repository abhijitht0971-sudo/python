# # DAY-1

# # integer
# a=12
# print(type(a),a)
# # float
# b=12.2
# print(type(b),b)
# # string
# c="world"
# print(type(c),c)
# # complex
# d=2+2j+11j+17j+54
# print(type(d),d)
# # bool 
# e=True
# f=False
# print(type(e),e)
# print(type(f),f)
# # none
# g=None
# print(type(g),g)
# # list
# h=["iron","lid","tin","copper"]
# print(type(h),h)
# # tuple
# i=("apple","orange","mango")
# print(type(i),i)
# # set
# j={"alpha","beta","gamma","12"}
# print(type(j),j)
# # dictionary
# k={"alpha":"12","beta":"35","gamma":"71"}
# print(type(k),k)

# # DAY-2

# #arithemetic operator
# a=60
# b=40
# print(a+b)
# print(a-b)
# print(a/b)
# print(a*b)
# print(a**b)
# print(a//b)
# print(a%b)
# # assignment operators
# a=11
# a+=14
# print(a)
# a=16
# a-=14
# print(a)
# a=24
# a*=3
# print(a)
# a=6
# a**=3
# print(a)
# a=15
# a//=4
# print(a)
# a=45
# a%=8
# print(a)
# a=6
# a/=4
# print(a)
# #comparison operator
# a=1000
# b=1000
# print(a==b)
# print(a!=b)
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# # loical operator
# a=True
# b=False
# print(a and b)
# print(a or b)
# print(not b)
# print(not a)
# # membership operator 
# a=["win","loss","move","slow"]
# print("loss" in a)
# print("rare" in a)
# #identity operator
# a=[10,12,14,15,20,45]
# b=[10,12,14,15,20,45]
# print(a==b)
# print(a is b)
# print(a is not b)
# # slicing
# a="membership operator"
# print(a[1:8])
# print(a[0:])
# print(a[4:16])
# print(a[-10:-1])
# print(a[::-1])
# print(a[0:18:2])
# print(a[0:18:4])
# print(a[-1:-18:-2])
# # replacing
# a="identity oPERAtors"
# s=a.replace("identity","membeRSHIP")
# print(s)
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.capitalize())
# print(s.swapcase())

# DAY -3

# PYTHON LIST
# accessing list items
a=["add","me","up"]
print(a[1])
print(a[-1])
print(a[1:3])
a[1:3]=["b","c"]
print(a)
# adding items
# append
b=["add","me","up"]
b.append("again")
print(b)
# insert
b.insert(3,"again")
print(b)
# extend
c=["you"]
b.extend(c)
print(b)
# removing items
#remove
a=["sun","moon","star","sky","light","dark"]
a.remove("sky")
print(a)
#pop
b=a.pop(4)
print(b)
# del
del a[2]
print(a)
# clear 
b=a.clear()
print(a)
# list methods
d=["new","old","first","last","first"]
print(d.count("first"))
print(d.index("last"))
d.reverse()
print(d)
d.sort()
print(d)
cpy=d.copy()
print(cpy)
# sort list 
a=[2,8,3,4,1,4,3,6,4]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
# joining list 
g=["as","per","none","off"]
h=["should","i","leave"]
v=g+h
print(v)
# extend
g.extend(h)
print(g)