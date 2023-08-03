# TASK 41: Write a program that can map() to make a list
# whose elements are squares of elements in [1,2,3,4,5,6,7,8,9,10].

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqrs = map(lambda x: x**2, li)
print(list(sqrs))


# TASK 42: Write a program that can map() and filter() to make a list
# whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, li)
sqrs = map(lambda x: x**2, even_numbers)
print(list(sqrs))


# TASK 43: Write a program that can filter() to make a list whose elements are even numbers between 1 and 20 (both included)).

print(list(filter(lambda x: x % 2 == 0, range(1, 21))))


# Task 44: Write a program that can map() to make a list whose elements are squares of numbers between 1 and 20 (both included).

print(list(map(lambda x: x**2, range(1, 21))))


# TASK 45: Define a class named American that has a static method called printNationality.

class American():

    @staticmethod
    def printNationality():
        print("I'm American")


American.printNationality()


# TASK 46: Define a class named American and its subclass NewYorker.

class American():
    pass


class NewYorker(American):
    pass


american = American()
new_yorker = NewYorker()

print(american)
print(new_yorker)


# TASK 47: Define a class named Circle which can be constructed by a radius.
# The Circle class has a method that can compute the area.


class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.14*(self.radius**2)


circle = Circle(5)
print(circle.area())


# TASK 48: Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method that can compute the area.

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


rectangle = Rectangle(3, 6)
print(rectangle.area())


# TASK 49: Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as an argument.
# Both classes have an area function that can print the area of the shape where the Shape's area is 0 by default.

class Shape():
    def area():
        return 0


class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.lenght = l

    def area(self):
        return self.lenght**2


square = Square(5)
print(square.area())
print(Shape.area())


# TASK 50: Please raise a RuntimeError exception.

raise RuntimeError('something wrong')
