# #  1.Create a list [1,2,3] and add 4 to the end using a list method.
# a=[1,2,3]
# a.append(4)
# print(a)
# # ans;[1, 2, 3, 4]
# # 2.Given [10,20,30] , remove 20 using a list method
# b=[10,20,30]
# b.remove(20)
# print(b)
# # ans;[10,30]
# # 3.From [5,3,9,1] , sort the list in ascending order using a list method
# c=[5,3,9,1]
# c.sort()
# print(c)
# # ans;[1, 3, 5, 9]
# # 4.From [1,2,3,4,5] , extract [2,3,4] using slicing only
# d=[1,2,3,4,5] 
# print(a[1:4])
# # ans;[2,3,4]
# # 5.Reverse the list [1,2,3,4] using slicing (no loops).
# e=[1,2,3,4]
# print(a[::-1])
# # ans;[4, 3, 2, 1]
# # 6.Combine [1,2] and [3,4] into one list using list operations
# a=[1,2]
# b=[3,4]
# f=a+b
# print(f)
# # ans;[1, 2, 3, 4]
# # 7.Convert [7,8] into [7,8,7,8] using list operations.
# a=[7,8]
# print(a*2)
# # ans;[7, 8, 7, 8]
# # 8.Check if 3 exists in [1,2,3,4] using a list operator
# a= [1,2,3,4]
# print(3 in a)
# # ans;True
# # 9. Count how many times 2 appears in [1,2,2,3,2] using a list method
# a=[1,2,2,3,2]
# print(a.count(2))
# # ans;3
# # 10.Remove the last element from ["a","b","c","d"] using a list method.
# a=["a","b","c","d"]
# a.remove("d")
# print(a)
# # ans;['a', 'b', 'c']
# # 11.Insert "x" at index 1 in ["a","b","c"] using a list method
# a=["a","b","c"]
# a.insert(1,'x')
# print(a)
# # ans;['a', 'x', 'b', 'c']
# # 12.Replace the element at index 2 in with 99 using indexing
# a= [10,20,30,40]
# a[2]=99
# print(a)
# # ans;[10, 20, 99, 40]
# # 13.Convert range(5) into a list using list functions.
# a=list(range(5))
# print(a)
# # ans;[0, 1, 2, 3, 4]
# # 14.Using slicing, extract every 2nd element from [1,2,3,4,5,6] → expected [2,4,6]
# a=[1,2,3,4,5,6]
# print(a[1:6:2])
# # ans;[2, 4, 6]
# # 15.Remove all elements from [1,2,3] using one list method.
# a=[1,2,3]
# print(a.clear())
# # ans;None
# # 16.Copy a list [4,5,6] using only list tools (no modules).
# a=[4,5,6]
# print(a.copy())
# # ans;[4, 5, 6]
# # 17.Convert [1,2,3] into a nested list [[1,2,3]] using list operations
# a=[1,2,3]
# b=[a]
# print(b)
# # ans;[[1, 2, 3]]
# # 18.Extend [1,2] with [3,4,5] using a list method.
# a=[1,2]
# b=[3,4,5]
# a.extend(b)
# print(a)
# # ans;[1, 2, 3, 4, 5]
# # 19.Using list repetition, create a list ["hello","hello","hello"] 
# a=["hello"]
# print(a*3)
# # ans;['hello', 'hello', 'hello']
# # 20.Remove the element at index 2 from [10,20,30,40] using a list method.
# a=[10,20,30,40]
# a.remove(a[2])
# print(a)
# # ans;[10, 20, 40]