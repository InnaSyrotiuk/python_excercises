# TASK 11: Write a program that accepts a sequence of comma-separated 4-digit binary numbers as its input and then check whether they are
# divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma-separated sequence.
import re
input_data = input().split(',')
output_data = []
for number in input_data:
    if int(number, 2) % 5 == 0:
        output_data.append(number)
print(", ".join(output_data))

# # lambda is an operator that helps to write function of one line
data = list(filter(lambda i: int(i, 2) % 5 == 0, input().split(',')))
print(",".join(data))


# # TASK 12: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of
# # the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

print(','.join([str(num) for num in range(1000, 3001)
      if all(map(lambda num: int(num) % 2 == 0, str(num)))]))

lst = [str(i) for i in range(1000, 3001)]
# using lambda to define function inside filter function
lst = list(filter(lambda i: all(int(j) % 2 == 0 for j in i), lst))
print(",".join(lst))

# TASK 13: Write a program that accepts a sentence and calculates the number of letters and digits.
input_data = input()
number, letter = 0, 0
for i in input_data:
    if i.isalpha():
        letter += 1
    elif i.isnumeric():
        number += 1
print(f"LETTERS: {letter} \nNUMBERS: {number}")

# TASK 14: Write a program that accepts a sentence and calculates the number of upper case letters and lower case letters.
input_data = input()
upper_case_letters, lower_case_letters = 0, 0
for i in input_data:
    if i.isupper():
        upper_case_letters += 1
    elif i.islower():
        lower_case_letters += 1
    else:
        pass
print(
    f"The number of upper case letters is {upper_case_letters}, \nlower case - {lower_case_letters}")

# TASK 15: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
num = input()
sum = int(num)+int(2*num)+int(3*num)+int(4*num)
print(sum)

num2 = input()
sum2 = 0
temp = str()
for i in range(4):
    temp += num2
    sum2 += int(temp)
print(sum2)

# TASK 16:Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.

num = input().split(',')
output_data = []
for i in num:
    if int(i) % 2 != 0:
        result = int(i)*int(i)
        output_data.append(str(result))

print(", ".join(output_data))

lst = [str(int(i)**2) for i in input().split(',') if int(i) % 2]
print(",".join(lst))

# TASK 17: Write a program that computes the net amount of a bank account based on a transaction log from console input.
# The transaction log format is shown as follows: D 100, W 200. D means deposit while W means withdrawal.
amount = 0
while True:
    input_data = input().split()
    if not input_data:
        break
    cm, num = map(str, input_data)
    if cm == "D":
        amount = +int(num)
    if cm == "W":
        amount = -int(num)
print(amount)

# TASK 18: A website requires the users to input username and password to register.Write a program to check the validity
# of password input by users. Following are the criteria for checking the password: At least 1 letter between [A-Z],
# At least 1 letter between [a-z], At least 1 number between [0-9], At least 1 character from [$#@],
# Minimum length of transaction password: 6, Maximum length of transaction password: 12


def check_creteria(x):
    cnt = 0
    if (len(x) >= 6) and (len(x) <= 12):
        cnt += 1
    if (i.islower() for i in x):
        cnt += 1
    if (i.issuper() for i in x):
        cnt += 1
    if (i.isnumeric() for i in x):
        cnt += 1
    for i in x:
        if (i == '@' or i == '#' or i == '$'):
            cnt += 1
    return cnt == 5


passwords = input("Input passwords: ").split(",")
results = []
for i in passwords:
    if check_creteria(i):
        results.append(i)
print(','.join(results))

# using regex

passwords = input("Input passwords: ").split(",")
pass_criteria = re.compile(
    "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,12}$")
correct_passwords = []
for i in passwords:
    if pass_criteria.fullmatch(i):
        correct_passwords.append(i)

print(",".join(correct_passwords))

# TASK 19: You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string,
# age and score are numbers. The tuples are input by console. The sort criteria is: name > age > score.
lst = []
while True:
    input_data = input()
    if not input_data:
        break

    lst.append(tuple(input_data.split(",")))

lst.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))
print(lst)

# TASK 20: Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.


class MyGen():
    def div_by_seven(self, n):
        for i in range(0, n+1):
            if i % 7 == 0:
                yield i


for i in MyGen().div_by_seven(int(input("Enter number: "))):
    print(i)
