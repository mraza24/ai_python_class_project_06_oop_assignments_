# 1. Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Ali", 88)
s1.display()

# 2. Using cls
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects: {cls.count}")

c1 = Counter()
c2 = Counter()
Counter.show_count()

# 3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car is starting")

car1 = Car("Toyota")
print(car1.brand)
car1.start()

# 4. Class Variables and Class Methods
class Bank:
    bank_name = "National Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show(self):
        print(f"Bank: {Bank.bank_name}")

b1 = Bank()
b2 = Bank()
b1.show()
Bank.change_bank_name("State Bank")
b2.show()

# 5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 5))

# 6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger created")

    def __del__(self):
        print("Logger destroyed")

log = Logger()
del log

# 7. Access Modifiers
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public
        self._salary = salary  # Protected
        self.__ssn = ssn  # Private

emp = Employee("John", 50000, "123-45-6789")
print(emp.name)
print(emp._salary)
try:
    print(emp.__ssn)
except AttributeError:
    print("Private attribute not accessible")

# 8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

t = Teacher("Sara", "Math")
t.show()

# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(5, 4)
print(r.area())

# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking")

d = Dog("Buddy", "Labrador")
d.bark()

# 11. Class Methods
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)

# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(0))

# 13. Composition
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

e = Engine()
c = Car(e)
c.start_car()

# 14. Aggregation
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

e = Employee("Alex")
d = Department(e)
print(d.employee.name)

# 15. MRO and Diamond Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()

# 16. Function Decorators
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()

# 17. Class Decorators
def add_greeting(cls):
    class NewClass(cls):
        def greet(self):
            return "Hello from Decorator!"
    return NewClass

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ali")
print(p.greet())

# 18. Property Decorators
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

p = Product(100)
print(p.price)
p.price = 200
print(p.price)
del p.price

# 19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

m = Multiplier(3)
print(callable(m))
print(m(10))

# 20. Creating a Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    print("Age is valid")

try:
    check_age(15)
except InvalidAgeError as e:
    print(e)

# 21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        val = self.start
        self.start -= 1
        return val

for num in Countdown(5):
    print(num)

