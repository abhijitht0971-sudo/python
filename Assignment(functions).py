# 1. Write a function that takes a number as input and returns whether the number is even or odd.
# def even_or_odd(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# number=even_or_odd(9)
# print(number)
# Ans:odd

# 2. Write a function that takes three numbers as input and returns the largest number among them.
# def large(a,b,c):
#     return max(a,b,c)
# print(large(12,56,23))
# Ans:56

# 3.Write a function that takes a list of numbers as input and returns the sum of all elements in the list.
# def list(n):
#     total=0
#     for num in n:
#         total+=num
#     return total
# a=[1,2,3,4,5,6,7,8,9,10]
# print(list(a))
# Ans:55

# 4. Write a function that takes a list of numbers as input and returns a new list containing only even numbers.
# def list_even(n):
#     return [x for x in n if x%2==0]
# a=[1,2,3,4,5,6,86,40,12,13,11]
# print(list_even(a))
# Ans:[2, 4, 6, 86, 40, 12]

# 5.Write a function that takes a string as input and returns the length of the string.
# def string(abc):
#     return len(abc)
# print(string("hellooo"))
# Ans:7

# 6.Write a function that takes a string as input and returns the string in uppercase.
# def string(abc):
#     return abc.upper()
# print(string("helloo"))
# Ans:HELLOO

# 7.Write a function that takes a number as input and returns whether the number is positive, negative, or zero.
# def num(n):
#    if n>0:
#     return("positive")
#    elif n==0:
#     return("zero")
#    else:
#     return("negative")
# print(num(-8))
# Ans:negative

# 8.Write a function that takes a number as input and returns True if the number  is a multiple of
#  both 3 and 5, otherwise returns False .
# def num(n):
#     if n%3==0 and n%5==0:
#         return "True"
#     else:
#         return "false"
# print(num(40))
# Ans:false 

# 9. Write a function that takes a list of numbers as input and returns the maximum value in the list.
# def list (n):
#    if not n:
#       return "none"

#    vmax=n[0]
#    for num in n[1:]:
#       if num>vmax:
#          vmax=num
#    return vmax
   
# print(list([1,23,12,14,5]))
# Ans:23

# 10. Write a function that takes marks as input and returns the grade according to the following rules:
# A for marks >=90
#  B for marks >= 75 
# C for marks >=60 
# Fail for marks below 60
# def mark(m):
#     if m>=90:
#         return "A"
#     elif m>=75:
#         return "B"
#     elif m>=60:
#         return "c"
#     else:
#         return "Fail"
# print(mark(100))
# Ans:A

# 11.Write a function that takes a price as input and returns the discounted price after applying a 10% discount.
# def discount(p):
#     dis=p*0.10
#     return p-dis
# print(discount(100))
# Ans:90

# 12.Write a function that takes a list of numbers as input and returns the count of even and odd numbers.
# def even_odd(n):
#     even=0
#     odd=0
#     for x in n:
#         if x%2==0:
#             even+=1
#         else:
#             odd+=1
#     return even,odd
# a=[1,2,3,4,5,6,7,8,9]
# even,odd=even_odd(a)
# print(f"Even:{even},odd:{odd}")
# Ans:even:4,odd:5

# 13.Write a function that takes a temperature in Celsius as input and returns the temperature in Fahrenheit.
# def temperature(celsius):
#     return (celsius*9/5)+32
# print(temperature(37))
# Ans:98.6