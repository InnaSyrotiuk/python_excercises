# TASK 61: The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0, f(n)=1 if n=1, f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by the console.

import random


def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return f(n-1)+f(n-2)


n = int(input())
print(f(n))


# TASK 62: The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0, f(n)=1 if n=1, f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n by the console for all numbers in the range from 0 to n.

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return f(n-1)+f(n-2)


n = int(input())
results = [str(f(i)) for i in range(0, n+1)]

print(",".join(results))


# TASK 63: Please write a program using a generator to print the even numbers between 0 and n in comma-separated form while n is input by the console.

def evenGenerator(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1


n = int(input())
values = [str(i) for i in evenGenerator(n)]
print(",".join(values))


# TASK 64: Please write a program using a generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma-separated form while n is input by the console.

def numGenerator(n):
    i = 0
    while i <= n:
        if i % 5 == 0 and i % 7 == 0:
            yield i
        i += 1


print(",".join([str(i) for i in numGenerator(int(input()))]))


# TASK 65: Please write assert statements to verify that every number in the list [2,4,6,8] is even.

li = [2, 4, 6, 7, 8]

for i in li:
    assert i % 2 == 0, '{} is not an even number'.format(i)


# TASK 66: Please write a program that accepts basic mathematical expressions from the console and print the evaluation result.

expression = input()
ans = eval(expression)
print(ans)


# TASK 67: Please write a binary search function that searches for an item in a sorted list.
# The function should return the index of elements to be searched in the list.

def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = round((low + high) / 2)

        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


lst = [1, 3, 5, 7, 10, 15]
print(binary_search(lst, 3))


# TASK 68: Please generate a random float where the value is between 10 and 100 using Python module.

print(random.uniform(10, 100))


# TASK 69: Please generate a random float where the value is between 5 and 95 using Python module.

print(random.random()*100-5)


# TASK 70: Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

print(random.choice([i for i in range(11) if i % 2 == 0]))
