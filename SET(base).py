# creating set 
a={1,2,3,4,5}
print(type(a),a)
b=set([4,5,6,7])
print(b)
c=set()
print(type(c),c)
# accessing items
d={1,21,23,43,22,44,4,5,6}
print(2 in d)
print(22 in d)
# adding items
e={1,3,5,7,9}
e.add(2)
print(e)
e.update([2,4,6,8])
print(e)
e={1,3,5,7,9}
e.remove(1)
print(e)
e={1,3,5,7,9}
e.discard(7)
print(e)
e={1,3,5,7,9}
e.pop()
print(e)
e={1,3,5,7,9}
e.clear()
print(e)
# joining set 
a={1,2,3,4}
b={3,4,5,6}
c=a.union(b)
print(c)
a.update(b)
print(a)
a={1,2,3,4}
b={3,4,5,6}
print(a&b)
c=a-b
print(c)
a={1,2,3,4}
b={3,4,5,6}
c=a^b
print(c)
a={1,2,3,4}
b=a.copy()
print(b)
a={3,4}
b={3,4,5,6}
c=a.issubset(b)
print(c)
e=b.issuperset(a)
print(e)
a=frozenset([1,2,3,4])
print(a)