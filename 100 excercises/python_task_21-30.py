# TASK 21: A robot moves in a plane starting from the original point (0,0). The robot can move UP, DOWN, LEFT, and RIGHT
# with given steps. The numbers after the direction are steps. Please write a program to compute the distance from the current position
# after a sequence of movements and the original point. If the distance is a float, then print the nearest integer.

from math import sqrt

x, y = 0, 0
while True:
    input_data = input().split()
    if not input_data:
        break
    if input_data[0] == "UP":
        x += int(input_data[1])
    if input_data[0] == "DOWN":
        x -= int(input_data[1])
    if input_data[0] == "RIGHT":
        y += int(input_data[1])
    if input_data[0] == "LEFT":
        y -= int(input_data[1])
dist = round(sqrt(x**2 + y**2))
print(dist)


# TASK 22: Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
input_data = input().split()
words = sorted(set(input_data))

for i in words:
    print(f"{i}: {input_data.count(i)}")


# TASK 23: Write a method which can calculate square value of number


def calculate_square(num):
    return num ** 2


print(calculate_square(int(input())))

# TASK 24: Please write a program to print some Python built-in functions documents,
# such as abs(), int(), and str(). And add a document for your own function
print(int.__doc__)
print(abs.__doc__)


def pow(n, p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''
    return n**p


values = input().split(",")
print(pow(int(values[0]), int(values[1])))
print(pow.__doc__)


# TASK 25: Define a class, which have a class parameter and have a same instance parameter.

class Person():
    # Define the class parameter "name"
    name = "Person"

    def __init__(self, name=None):
        # self.name is the instance parameter
        self.name = name


daniel = Person("Daniel")
print(f"{Person.name} name is {daniel.name}")


# TASK 26: Define a function which can compute the sum of two numbers.

def sum(num1, num2):
    return num1+num2


print(sum(1, -12))

# using lambda


def sum(n1, n2): return n1 + n2


print(sum(1, 2))


# TASK 27: Define a function that can convert a integer into a string and print it in console.

def convert_int_to_str(num):
    return str(num)


print(convert_int_to_str(9))
print(type(convert_int_to_str(9)))

# using lambda


def conv(x): return str(x)


n = conv(10)
print(n)
print(type(n))


# TASK 28: Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.

def sum_of_str(num1, num2):
    return int(num1)+int(num2)


print(sum_of_str("-10", "17"))


# TASK 29: Define a function that can accept two strings as input and concatenate them and then print it in console.

def concatenate(str1, str2):
    return str1 + str2


print(concatenate("10", "222"))


# TASK 30: Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.

def str_max_length(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str1) < len(str2):
        print(str2)
    elif len(str1) == len(str2):
        print(str1)
        print(str2)


str_max_length("one", "four")
str_max_length("seven", "ten")
str_max_length("one", "two")
