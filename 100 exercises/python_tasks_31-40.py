# TASK 31: Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys.

def print_dict():
    dict = {i: i**2 for i in range(1, 21)}
    return dict


print(print_dict())


# TASK 32: Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys. The function should just print the keys only.

def dict_keys():
    dict = {i: i**2 for i in range(1, 21)}
    return dict.keys()


print(dict_keys())


# TASK 33: Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included)

def print_lst():
    lst = [i**2 for i in range(1, 21)]
    print(lst)


print_lst()


# TASK 34: Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.

def print_lst_first5():
    lst = [i**2 for i in range(1, 21)]
    print(lst[:5])


print_lst_first5()


# TASK 35: Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the last 5 elements in the list.

def print_lst_last5():
    lst = [i**2 for i in range(1, 21)]
    print(lst[-5:])


print_lst_last5()


# TASK 36: Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print all values except the first 5 elements in the list.

def print_lst_last15():
    lst = []
    for i in range(1, 21):
        lst.append(i**2)
    print(lst[5:])


print_lst_last15()


# TASK 37: Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

def square_of_numbers():
    return tuple(i ** 2 for i in range(1, 21))


print(square_of_numbers())


# TASK 38: With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values on one line and the last
# half values on the other.


def split_tuple():
    tpl = tuple(i for i in range(1, 11))
    tpl1 = tpl[:5]
    tpl2 = tpl[5:]
    print(tpl1)
    print(tpl2)


split_tuple()


# TASK 39: Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

tpl = tuple(i for i in range(1, 11))
even_lst = []
for i in tpl:
    if int(i) % 2 == 0:
        even_lst.append(i)

print(tuple(even_lst))


# Task 40: Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

input_str = str(input().lower())
if input_str == 'yes':
    print('Yes')
else:
    print('No')
