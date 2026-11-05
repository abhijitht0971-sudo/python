# tuple is immutable collection

# creating
a=(1,2,3,4,"hello")
print(a,type(a))
# accessing tuple item
# index 
a=("orange","grapes","cherry")
print(a[0])
print(a[-1])
# slicing
a=11,12,16,18,22,30
print(a[1:5])
# updating tuple 
# ressigning tuple 
a=(1,2,3,4)
a=(2,4,6,8)
print(a)
# convert tuple into list 
a=("me","you","us","we")
b=list(a)
b[2]="all"
a=tuple(b)
print(a)
# unpacking tuple
a=("me","you","us","we")
(a1,a2,a3,a4)=a
print(a1)
print(a2)
print(a3)
print(a4)
# using asterik
a=(1,2,3,4,5)
(first,second,*third,four)=a
print(first)
print(second)
print(third)
print(four)
# joining tuple 
a=(1,2,3,4)
b=(2,4,6)
c=a+b
print(c)
# tuple methods
a=(1,2,2,2,2,2,2,2,3,4,5,6)
print(a.count(2))
print(a.index(4))
# deleting tuple 
a=("ab","cd","ef")
del a 
print(a)