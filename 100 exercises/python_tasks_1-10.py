# TASK 1: Write a program that will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

from math import sqrt
list = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        list.append(str(i))
print(','.join(list))

print(*(i for i in range(2000, 3201) if i % 7 == 0 and i %
      5 != 0), sep=',')  # Using generators and list comprehension


# TASK 2:Write a program that can compute the factorial of given numbers. The results should be printed in
# a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be:40320
num = int(input())  # using For Loop
fact = 1
for i in range(1, num+1):
    fact = fact*i
print(fact)

number = int(input())  # using While Loop
factorial = 1
i = 1
while i <= number:
    factorial = factorial*i
    i = i+1
print(factorial)

n = int(input())  # using Lambda Function
def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)


print(shortFact(n))

# TASK 3: With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program: 8. Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n = int(input())       # using For Loop
d = {}
for i in range(1, n+1):
    d[i] = i * i
print(d)

n = int(input())       # using dictionary comprehension
d = {i: i*i for i in range(1, n+1)}
print(d)

# TASK 4:Write a program that accepts a sequence of comma-separated numbers from the console and generates a list and a tuple
# that contains every number
list_with_numbers = input(
    "Enter a series of numbers separated by a comma : ").split(",")
tuple_with_numbers = tuple(list_with_numbers)
print(list_with_numbers)
print(tuple_with_numbers)

# TASK 5: Define a class that has at least two methods:
# getString: to get a string from the console input
# printString: to print the string in upper case.
# Also please include a simple test function to test the class methods.


class InputOutStr():
    def __init__(self):
        self.txt = ""

    def get_string(self):
        self.txt = input()

    def print_string(self):
        print(self.txt.upper())


txt = InputOutStr()
txt.get_string()
txt.print_string()

# TASK 6: Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
values = input("Please write numbers to be calculated separated by commas : ")
lst_num = values.split(",")
C, H = 50, 30
results = []
for i in lst_num:
    square_root = ((2*C*int(i))/H)**(1/2)
    results.append(str(round(square_root)))

print(f"Your result(s): {', '.join(results)}")

# using math functions
C, H = 50, 30


def calc(D):
    return sqrt((2*C*D)/H)


D = (input("Please write numbers to be calculated separated by commas : ")).split(",")
print(", ".join([str(round(calc(int(i)))) for i in D]))

# TASK 7: Write a program that takes 2 digits, X, Y as input, and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.

x, y = map(int, input().split(','))
lst = []

for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(i*j)
    lst.append(tmp)

print(lst)


x, y = map(int, input().split(','))
lst = [[i*j for j in range(y)] for i in range(x)]
print(lst)


# TASK 8: Write a program that accepts a comma-separated sequence of words as input
# and prints the words in a comma-separated sequence after sorting them alphabetically.
print(", ".join(sorted(input().split(","))))

items = input().split(",")
items.sort()
print(", ".join(items))

# TASK 9:Write a program that accepts a sequence of lines as input
# and prints the lines after making all characters in the sentence capitalized.
lines = []
while True:
    input_lines = input()
    if input_lines:
        lines.append(input_lines.upper())
    else:
        break

for line in lines:
    print(line)

# TASK 10: Write a program that accepts a sequence of whitespace-separated words as input and prints them
# after removing all duplicate words and sorting them alphabetically.
# input string splits -> converting into set() to store unique

input_data = input().split()
output_data = []
for words in input_data:
    if words not in output_data:
        output_data.append(words)

print(" ".join(sorted(output_data)))
