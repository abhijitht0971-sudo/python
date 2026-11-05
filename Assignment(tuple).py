# 1.Create a tuple (1,2,3,4) and access the element 3 using indexing.
a=(1,2,3,4)
print(a.index(3))
# ans;2
# 2.Convert the tuple (10,20,30) into a list.
b=(10,20,30)
c=list(b)
print(c)
# ans;[10, 20, 30]
# 3.Convert the list (1,2,3) into a tuple.
a=[1,2,3]
b=tuple(a)
print(b)
# ans;(1, 2, 3)
# 4.From the tuple ("a","b","c","d") , extract ("b","c") using slicing.
c=("a","b","c","d")
print(c[1:3])
# ans;('b', 'c')
# 5. Check if "x" exists inside the tuple ("x","y","z")
d=("x","y","z")
print(d.index("x"))
# ans;0=True
# 6.Given (5,3,9,1) , find the maximum value using a tuple function.
e=(5,3,9,1)
print(e[2])
# ans;9
# 7.Given (1,2,3) , create a new tuple (1,2,3,1,2,3) using tuple operations only.
a=(1,2,3)
b=(1,2,3)
c=a+b
print(c)
# ans;(1, 2, 3, 1, 2, 3)
# 8.Count how many times 2 appears in (1,2,2,3,2) using a tuple method.
a=(1,2,2,3,2)
print(a.count(2))
# ans;3
# 9.Find the index of "cat" in ("dog","cat","mouse") 
a=("dog","cat","mouse")
print(a.index("cat"))
# ans;1
# 10.Reverse (1,2,3,4,5) using slicing.
b=(1,2,3,4,5)
print(b[::-1])
# ans;(5, 4, 3, 2, 1)
# 11.Combine (1,2) and (3,4) into  (1,2,3,4) using tuple operations.
a=(1,2)
b=(3,4)
c=a+b
print(c)
# ans;(1, 2, 3, 4)
# 12.Convert "hello" into a tuple of characters.
a= "hello"
b=(a)
print(b)
# ans;hello
# 13.Convert (1,2,3,4) into the list [1,4] by extracting only first & last elements.
a=(1,2,3,4)
a=(1,4)
b=list(a)
print(b)
# ans;[1, 4]
# 14.Given a tuple (10,20,30,40), replace the value 30 with 99 (hint:convert to list → modify → convert back).
a=(10,20,30,40)
b=list(a)
b[2]=99
a=tuple(b)
print(a)
# ans;(10, 20, 99, 40)
# 15.Using unpacking, extract a=1 , b=2 ,c=3 from (1,2,3) .
a=(1,2,3)
(a,b,c)=a
print(a)
print(b)
print(c)
# ans;a=1,b=2,c=3
# 16.Create a nested tuple: turn (1,2,3) into ((1,2,3)) .
a=(1,2,3)
b=((a),)
print(b)
# ans;((1, 2, 3),)
# 17.Merge ("a","b") with ["c","d"]  to get a single tuple ("a","b","c","d")  (hint: convert list → tuple).
a=("a","b") 
b=["c","d"]
c=tuple(b)
d=a+c
print(d)
# ans;('a', 'b', 'c', 'd')
# 18.Check if tuple (1,2,3) is equal to its reverse.
a=(1,2,3)
b=a[::-1]
c=(a==b)
print(c)
# ans;False
# 19.Convert a tuple of lists ([1,2],[3,4]) into a single flat list [1,2,3,4]
a=([1,2],[3,4])
(c,d)=a
b=c+d
print(b)
# ans;[1, 2, 3, 4]
# 20.Given (1, [2,3], 4) , add 5  inside the inner list so result becomes (1,[2,3,5], 4 ).
a=(1,[2,3],4)
a[1].append(5)
print(a)
# ans;(1, [2, 3, 5], 4)