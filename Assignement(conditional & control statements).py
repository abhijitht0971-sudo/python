# 1. Write a program to check whether a number is positive, negative, or zero.
# a=10
# if a>0:
#     print("positive")
# elif a==0:
#     print("zero")
# else:
#     print("negative")
# Ans:a=10 positive
    # a=0 zero 
    # a=-2 negative

# 2.Check if a number is even or odd.
# n=10
# if n%2==0:
#     print("even")
# else:
#     print("odd")
# Ans:even

# 3.Given a number, check if it is greater than 100.
# a=120
# if a>100:
#     print("yes")
# else:
#     print("no")
# Ans:yes

# 4.Check whether a person is eligible to vote (age >= 18).
# age=18
# if age>=18:
#     print("eligible for vote")
# else:
#     print("not eligible for vote")
# Ans:eligible for vote

# 5.Given two numbers, print the greater number.
# a=20
# b=15
# if a>b:
#     print(" greater is:",a)
# elif a<b:
#     print("greater is:",b)
# else:
#     print("both are equal")
# Ans:b is greater than a 

# 6.Given three numbers, print the largest number.
# a=12
# b=8
# c=20
# if a>=b and a>=c:
#     print("largest number is:",a)
# elif b>=a and b>=c:
#     print("largest number is:",b)
# else:
#     print("largest number is:",c)
# Ans:largest number is 20

# 7.Check whether a year is a leap year.
# year=int(input("enter a year:"))
# if year%400==0:
#     print(f"{year} is a leap year.")
# elif year%100==0:
#     print(f"{year} is not a leap year.")
# elif year%4==0:
#     print(f"{year} is leap year.")
# else:
#     print(f"{year} is not a leap year")
# 2004
# Ans:2004 is leap year

# 8.Given a mark, print: "Pass" if marks >= 40 "Fail" otherwise
# mark=int(input("enter mark"))
# if mark>=40:
#     print("pass")
# else:
#     print("fail")

# 9.Given a mark, print grades: A → >= 90 B → >= 75 C → >= 60 Fail → below 60
# grade=int(input("enter mark"))
# if grade>=90:
#     print("A")
# elif grade>=70:
#     print("B")
# elif grade>=60:
#     print("C")
# else:
#     print("fail")

# 10.Check if a character is a vowel or consonant.
# letter=input("enter a character:").lower()
# if len(letter) !=1 or not letter.isalpha():
#     print("please enter a single alphabet")
# elif letter in ["a","e","i","o","u"]:
#     print("vowel")
# else:
#     print("consonant")


# 11.Print numbers from 1 to 10 but stop when number is 6.
# for i in range(1,10):
#     if i==7:
#         break
#     print(i)

#12. Print numbers from 1 to 10 but skip number 5.
# for i in range(1,10):
#     if i==5:
#         continue
#     print(i)

# 13.Use pass inside an if block and explain why it doesnʼt cause an error.
# a=12 
# if a>0:
#     pass
# else:
#     print("negative")
# for i in range(1,11):
#     ...
# print(i)
# Ans:pass literally does nothing and returns none 

# 14.Print all even numbers between 1 and 20
# a=[x for x in range(1,20) if x%2==0]
# print(a)
# Ans:[2, 4, 6, 8, 10, 12, 14, 16, 18]

# 15.Find the sum of numbers from 1 to 10.
# total=0
# for i in range(0,11):
#     if i==0:
#         continue
#     total+=i
# print(total)
# Ans:55

# 16.Check whether a given number is a multiple of both 3 and 5
# number=int(input("number is"))
# if number%3==0 and number%5==0:
#     print(f"{number} is multiple of both 3 and 5.")
# else:
#     print(f"{number} is not a multiple of both 3 and 5.")

# 17.Print "Hello" 5 times using a loop.
# for i in range(5):
#     print("hello")

# 18.Given a list [1,2,3,4,5], print only numbers greater than 3.
# a=[1,2,3,4,5]
# for i in a:
#     if i>3:
#         print(i)

# 19.Advanced Login System
# Write a Python program to simulate a login system with the following rules:
#  The correct username is "admin" and the correct password is "1234" .
#  The user is allowed a maximum of 3 login attempts.
#  The username comparison should be case-insensitive. 
# The password comparison should be case-sensitive.
#  If the user enters correct credentials within the allowed attempts, display Login successful .
#  If all attempts are used without success, display Account locked .
# After each failed attempt, display the number of attempts remaining.

# real_username="admin"
# real_password="1234"
# attemptmax=3
# for i in range(1,attemptmax+1):
#     username=input("enter username")
#     password=input("enter password")
#     if username.lower()==real_username and password==real_password:
#         print("login successfull")
#         break
#     else:
#         attemptmax-=1
#     if attemptmax>0:
#         print("incorrect username or password")
#         print("attempts remaining:",attemptmax)
#     else:
#         print("account locked")

# 20.Enhanced Traffic Light Controller 
# Write a Python program that acts as a traffic light controller with the following conditions:
#  The program should accept either a color or a number as input. 
# Use the mapping:
# 1 or "red"  Stop and wait for 60 seconds 
# 2 or "yellow"  Ready and wait for 5 seconds
# 3 or "green"  Go and drive safely 
# The program should handle inputs in a case-insensitive manner. 
# If the input does not match any valid color or number, display Invalid signal .

# signal=input("enter traffic signal(1/red,2/yellow,3/green):").strip().lower()

# if signal in ("1","red"):
#     print("stop and wait for 60 seconds")
# elif signal in ("2","yellow"):
#     print("ready and wait for 5 seconds")
# elif signal in ("3","green"):
#     print("go and drive safely")
# else:
#     print("invalid signal")

# LIST COMPREHENSION QUESTIONS
# 1.Given a list of numbers, write a program to find the sum of all numbers, 
# the sum of even numbers, and the sum of odd numbers using list comprehension.

# num=[10,15,20,25,30,35]
# total_sum=sum([n for n in num ])
# print("sum of all numbers:",total_sum)
# even_sum=sum([n for n in num if n%2==0]) 
# print("sum of even numbers:",even_sum)
# odd_sum=sum([n for n in num if n%2!=0])
# print("sum of odd numbers:",odd_sum)

# 2.Given a list of numbers, create a new list that contains only numbers 
# greater than 10 and divisible by 3 using list comprehension
# a=[10,15,20,25,30,33,40,42,12]
# b=[x for x in a if x>10 and x%3==0]
# print("new list",b)

# 3.Given a list of numbers, 
# create a new list containing only even numbers greater than 10 using list comprehension.
# b=[10,15,20,25,30,33,40,42,12]
# a=[x for x in b if x%2==0]
# print("even_list",a)

# 4.Given a list of strings,
#  create a new list containing the length of each string using list comprehension.
# words=["you","me","us","our"]
# length=[len(word) for word in words]
# print("length of each string;",length)

# 5.Given a list of numbers, 
# create a new list where: 
# even numbers are replaced with "even"
#  odd numbers are replaced with "odd"
# num=[1,2,3,4,5,6,7,8,9]
# new=["even" if n%2==0 else "odd" for n in num]
# print("new list",new)