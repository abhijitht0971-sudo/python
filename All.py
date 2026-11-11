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
# a=["add","me","up"]
# print(a[1])
# print(a[-1])
# print(a[1:3])
# a[1:3]=["b","c"]
# print(a)
# # adding items
# # append
# b=["add","me","up"]
# b.append("again")
# print(b)
# # insert
# b.insert(3,"again")
# print(b)
# # extend
# c=["you"]
# b.extend(c)
# print(b)
# # removing items
# #remove
# a=["sun","moon","star","sky","light","dark"]
# a.remove("sky")
# print(a)
# #pop
# b=a.pop(4)
# print(b)
# # del
# del a[2]
# print(a)
# # clear 
# b=a.clear()
# print(a)
# # list methods
# d=["new","old","first","last","first"]
# print(d.count("first"))
# print(d.index("last"))
# d.reverse()
# print(d)
# d.sort()
# print(d)
# cpy=d.copy()
# print(cpy)
# # sort list 
# a=[2,8,3,4,1,4,3,6,4]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# # joining list 
# g=["as","per","none","off"]
# h=["should","i","leave"]
# v=g+h
# print(v)
# # extend
# g.extend(h)
# print(g)

# DAY -4

# PYTHON TUPLE 
# creating a tuple 
# a=(1,2,3,4,"as","we",6,4.5,3)
# print(type(a),a)
# # accessing items 
# a= ('apple', 'banana', 'cherry')
# print(a[1])
# print(a[-1])
# # slicing
# a=(1,1,2,4,6,8,9,0)
# print(a[1:5])
# # updating a tuple 
# # reassigning
# a=(2,3,4,5)
# a=(1,2,4,7,8)
# print(a)
# # convert tuple to list
# b= ('apple', 'banana', 'cherry')
# c=list(b)
# c[0]="fig"
# b=tuple(c)
# print(b)
# # unpacking tuples
# a= ('apple', 'banana', 'cherry')
# (a1,a2,a3)=a
# print(a1)
# print(a2)
# print(a3)
# # using asterisk
# s=(9,8,7,4,3,5)
# (a,*b,c)=s
# print(a)
# print(b)
# print(c)
# # joining tuple
# a=(9,0,8,7)
# n=(7,8,6,5)
# c=a+n
# print(c)
# # methods
# l=(1,4,3,5,6,4,3,8,9,0,2,1,1,3,4,5,2,3,2)
# print(l.count(2))
# print(l.index(6))
# # delete
# a= ('apple', 'banana', 'cherry')
# del a
# print(a)

# DAY-5

# PYTHON SET & DICTIONARY

# SET 
# a={1,2,3,5}
# print(type(a),a)
# b=set([3,2,4])
# print(b)
# a=set()
# print(a)
# # accessing items
# v={10, 20, 30, 40}
# print(10 in v)
# print(9 in a)
# # methods
# # adding items
# g={2,3,4}
# g.add(7)
# print(g)
# o={4,5,6,0}
# o.update([1,2,3,9])
# print(o)
# # remove items
# v={10, 20, 30, 40}
# v.remove(20)
# print(v)
# v.discard(10)
# print(v)
# b={1,2,3,4}
# c=b.pop()
# b.clear()
# print(c)
# print(b)
# # joining
# v={10, 20, 30, 40}
# x={1,2,3,4}
# a=v.union(x)
# v.update(x)
# print(v)
# print(a)
# a={2,1,4,3,5}
# b={4,3,7,89,9}
# c=a&b
# print(c)
# g=a-b
# print(g)
# h=a^b
# print(h)
# s={1,4}
# f={2,3,43,3,4,1,76,7}
# print(s.issubset(f))
# print(f.issuperset(s))
# # frozen set 
# w=frozenset([32,45,43,21,51])
# print(w)

# dictionary
# a = {"name": "Jack", "age": 20, "city": "america"}
# print(type(a),a)
# b=dict(name='jane',age=21,place='washington')
# print(b)
# a={}
# print(a)
# # accessing items
# a = {"name": "Jack", "age": 20, "city": "america"}
# print(a["age"])
# print(a.get("name"))
# print(a.get("job"))
# # changing
# a = {"name": "Jack", "age": 20, "city": "america"}
# a["city"]='france'
# print(a)
# # adding items
# a = {"name": "Jack", "age": 20, "city": "america"}
# a["job"]="engineer"
# print(a)
# # removing items
# a = {"name": "Jack", "age": 20, "city": "america"}
# j=a.pop("age")
# print(j)
# print(a)
# a = {"name": "Jack", "age": 20, "city": "america"}
# b=a.popitem()
# print(b)
# c = {"name": "Jack", "age": 20, "city": "america"}
# del c["city"]
# print(c)
# e= {"name": "Jack", "age": 20, "city": "america"}
# e.clear()
# print(e)
# # nested dict 
# q={"a1":{"name": "kevin", "age": 20, "city": "america"},
# "a2" : {"name": "mike", "age": 26, "city": "france"},
# "a3" : {"name": "silva", "age": 30, "city": "norway"},}
# print(q["a2"]["city"])
# # methods
# a = {"name": "Jack", "age": 20, "city": "america"}
# print(a.keys())
# print(a.values())
# print(a.items())
# a = {"name": "Jack", "age": 20, "city": "america"}
# a.update({"place":"washington","age":22})
# print(a)
# s= {"name","age","city"}
# b=dict.fromkeys(s,"np")
# print(b)
# a = {"name": "Jack", "age": 20, "city": "america"}
# b=a.setdefault("place","wow")
# print(b)