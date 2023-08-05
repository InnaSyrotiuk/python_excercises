# # TASK 51: Write a function to compute 5/0 and use try/except to catch the exceptions. Use try/except to catch exceptions.

import re


def divide():
    return 5/0


try:
    divide()
except ZeroDivisionError:
    print("Division by zero is undefined")
except:
    print("Any other exception")


# # TASK 52: Define a custom exception class that takes a string message as an attribute.

class CustomException(Exception):

    def __init__(self, message):
        self.message = message


num = int(input())

try:
    if num < 10:
        raise CustomException("Input number is less than 10")
    elif num > 10:
        raise CustomException("Input number is grater than 10")
    elif num == 10:
        raise CustomException("Input number is equal 10")
except CustomException as ce:
    print("The error raised: " + ce.message)


# TASK 53: Assuming that we have some email addresses in the "username@companyname.com" format,
# please write a program to print the user name of a given email address.
# Both user names and company names are composed of letters only.


emails = input()
pattern = "(\w+)@\w+.com"
names = re.findall(pattern, emails)
print(names)


# TASK 54: Assuming that we have some email addresses in the "username@companyname.com" format,
# please write a program to print the company name of a given email address.
# Both user names and company names are composed of letters only.


emails = input()
pattern = "\w+@(\w+).com"
names = re.findall(pattern, emails)
print(names)


# TASK 55: Write a program that accepts a sequence of words separated by whitespace as input
# to print the words composed of digits only.
# Example: If the following words are given as input to the program: 2 cats and 3 dogs.
# Then, the output of the program should be: ['2', '3']


emails = input()
pattern = "\d+"
names = re.findall(pattern, emails)
print(names)


# TASK 56: Print a unicode string "hello world". Use u'strings' format to define unicode string.

unicodeString = u"hello world!"
print(unicodeString)


# TASK 57: Write a program to read an ASCII string and convert it to a unicode string encoded by utf-8.
s = input()
u = s.encode('utf-8')
print(u)


# TASK 58: Write a special comment to indicate a Python source code file is in unicode.

# -*- coding: utf-8 -*-


# TASK 59: Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

number = int(input())

if number > 0:
    sum = 0.0
    for i in range(1, number+1):
        sum += i/(i+1)

if number < 0:
    print("The number must be greater than 0. Please try again")

print(round(sum, 2))


# TASK 60: Write a program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=0 with a given n input by console (n>0).

def f(n):
    if n == 0:
        return 0
    else:
        return f(n-1)+100


n = int(input())
print(f(n))
