# # 1. Create a string "hello" and convert it to uppercase using a string method.
# a="hello"
# print(a.upper())
# #ans;HELLO
# # 2.Given "PYTHON" , convert it to lowercase using a string method
# b="PYTHON"
# print(b.lower())
# #ans;python
# # 3.From "hello world" , replace "world" with "python" using a string method
# c="hello world"
# c=c.replace("world","python")
# print(c)
# # ans;hello python
# # 4.Extract "ell" from "hello" using slicing only.
# d="hello"
# print(d[1:4])
# # ans;ell 
# # 5.Reverse the string "python" using slicing (no loops).
# e="python"
# print(e[::-1])
# # ans;nohtyp
# # 6.Combine "hello" and "world" into one string using string operations.
# a="hello"
# b="world"
# f=a+" "+b
# print(f)
# a=["hello","world"]
# b=" ".join(a)
# # ans;hello world
# # 7.Repeat the string "hi" to get "hihihi" using string operations.
# a="hi"
# g=a*3
# print(g)
# # ans;hihihi
# # 8.Check if "cat" exists in "concatenate" using a string operator.
# a="concatenate"
# print("cat" in a)
# # ans;True
# # 9.Count how many times "a" appears in "banana" using a string method
# b="banana"
# print(b.count("a"))
# # ans;3
# # 10.Remove leading and trailing spaces from " hello " using a string method.
# a=" hello "
# print(a.strip())
# # ans;hello
# # 11.Find the index of "o" in "hello" using a string method.
# c="hello"
# print(c.find("o"))
# # ans;4
# # 12.Split the string "a,b,c,d" into a list using a string method.
# b="a,b,c,d"
# print(b.split(","))
# # ans;['a', 'b', 'c', 'd']
# # 13.Join the list ["a","b","c"] into "abc" using a string method.
# a=["a","b","c"]
# print("".join(a))
# # ans;abc
# # 14.Extract every 2nd character from "abcdef" using slicing → expected "ace" .
# c="abcdef"
# print(c[0:7:2])
# # ans;ace
# # 15.Replace all "a" with "@" in "banana" using a string method.
# a="banana"
# print(a.replace("a","@"))
# # ans;b@n@n@
# # 16.Check if "hello123" is alphanumeric using a string method
# a="hello123"
# print(a.isalnum())
# # ans;True
# # 17.Capitalize the first letter of "python" using a string method.
# a="python"
# print(a.capitalize())
# #ans;Python
# # 18.Convert "hello world" into "Hello World" using a string method.
# a="hello world"
# print(a.title())
# # ans;Hello World
# # 19.Remove all vowels from "python" using string operations (no loops if possible 😈).
# b="python"
# a=b.replace("python","pythn")
# print(a)
# # ans;pythn
# # 20.Check if "madam" is a palindrome using slicing
# a="madam"
# print(a[::-1])
# # ans;madam