# class Car:
#     def __init__(self, brand, year):
#         self.comp = brand
#         self.year = year

#     def detail(self):
#         print(self.comp, self.year)

# c1 = Car("Mustang", 2010)
# c1.detail()


# class Laptop:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#
#     def __str__(self):
#         return f"{self.brand}, {self.price}"
#
# l1 = Laptop("Acer", 39999)
# print(l1)


# class Counter:
#     def __init__(self, value):
#         self.value = 0

#     def increment(self):
#         self.value += 1
#         return self.value

# c1 = Counter(1)
# print(c1.increment())
# print(c1.increment())


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         print(int(3.14 * self.radius * self.radius))

# c1 = Circle(20)
# c1.area()


# class Employee:
#     company_name = "abc pvt ltd"

#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print("name: ", self.name, "company: ", Employee.company_name)

# e1 = Employee("john")
# e1.display()
# Employee.company_name = "tcs india"
# e1.display()

# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def draw(self):
#         print("the shape is ", self.name)

# class Rectangle(Shape):
#     def draw(self):
#         print("the shape is ", self.name)

# class Triangle(Shape):
#     def draw(self):
#         print("the shape is ", self.name)

# s1 = Shape("well defined")
# s1.draw()
# r1 = Rectangle("rectangular")
# r1.draw()
# t1 = Triangle("three sided")
# t1.draw()

# class shape:
#     def write(self):
#         print("the shape is well defined")

# class rectangle(shape):
#     def write(self):
#         print("the rectangle is a shape")

# class circle(shape):
#     def write(self):
#         print("the circle has a radius and diameter")

# def display_shape(shape):
#     shape.write()

# rect = rectangle()

# display_shape(rect)
# display_shape(circle())


# class BankBalance:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self):
#         if self.__balance > 100:
#             print("amount credited to your account")
#         else:
#             print("insufficient balance")

#     def withdraw(self):
#         print("current balance: ", self.__balance)

# b1 = BankBalance(5000)
# b1.deposit()
# b1.withdraw()


# class Person:
#     def __init__(self, name):
#         self.name = name
#
# class Company:
#     def __init__(self, comp):
#         self.comp = comp
#
# class Employee(Person, Company):
#     def __init__(self, name, comp, posting):
#         Person.__init__(self, name)
#         Company.__init__(self, comp)
#         self.post = posting
#
#     def emp(self):
#         # print("name:", self.name, "company:", self.comp, "posting:", self.post)
#         for key, value in e1.__dict__.items():
#             print(key, ":", value)
#
#
# e1 = Employee("george", "bbc india", "trainee")
# e1.emp()


# class Student:
#     def __init__(self, name):
#         self.name = name

# class Athlete:
#     def __init__(self, sport):
#         self.sport = sport

# class StudentAthlete(Student, Athlete):
#     def __init__(self, name, sport):
#         Student.__init__(self, name)
#         Athlete.__init__(self, sport)

#     def show(self):
#         print("Name: ", self.name, "\nsport: ", self.sport)

# s1 = StudentAthlete("john", "shortput")
# s2 = StudentAthlete("bolt", "athletics")
# s1.show()
# s2.show()

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def get_name(self):
#         return self.__name

#     def get_age(self):
#         return self.__age

#     def set_name(self, name):
#         self.__name = name
#         print(self.__name)

#     def set_age(self, new):
#         if new > 10:
#             self.__age = new
#             print(self.__age)
#         else:
#             print("not accepted")

# p1 = Person("Geeks", 10)
# print(p1.get_name())
# print(p1.get_age())
# p2 = Person("john", 16)
# p2.set_name("albert")
# p2.set_age(29)


# from abc import ABC, abstractmethod
# class Shape(ABC):
#     def __init__(self, color):
#         self.color = color

#     @abstractmethod
#     def get_color(self):
#         pass

#     @abstractmethod
#     def get_area(self):
#         pass

# class Square(Shape):
#     def __init__(self, color, side):
#         super().__init__(color)
#         self.side = side

#     def get_color(self):
#         return self.color

#     def get_area(self):
#         return self.side * self.side

# s1 = Square("maroon", 12)
# print(s1.get_color())
# print(s1.get_area())


# class Student:
#     def __init__(self, sid, deptid):
#         self.name = sid
#         self.dept = deptid

#     def get_info(self):
#         print("Student ID: ", self.name, "Dep: ", self.dept)

# class Faculty:
#     def __init__(self, eid, depid, facultyname):
#         self.employ = eid
#         self.dep = depid
#         self.facultyname = facultyname

#     def get_info(self):
#         print("Employee ID: ", self.employ, "Dep ID: ", self.dep, "faculty:", self.facultyname)

# class PhDStudent(Student, Faculty):
#     def __init__(self, sid, eid, depid, deptid, facultyname):
#         Student.__init__(self, sid, deptid)
#         Faculty.__init__(self, eid, depid, facultyname)

#     def get_info(self):
#         print("student: ", self.name, "department: ", self.dep, "employee: ", self.employ, "faculty: ", self.facultyname)

# p1 = PhDStudent("justin", 555, "viscom", 120, "jus")
# p1.get_info()
# s1 = Student("hitler", "history")
# s1.get_info()


# class Addition:

#     @staticmethod
#     def add(n1, n2):
#         return int(n1 + n2)

# a1 = Addition(21, 32)
# a1.add()


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.marks = []
#         self.total = 0
#
#     def stu_name(self):
#          print(f"Name: {self.name}")
#
#     def filter_num(self, n):
#             if isinstance(n, int):
#                 bool_val=True
#                 return n,bool_val
#             if isinstance(n, str) and n.isdigit():
#                 bool_val=True
#                 return int(n),bool_val
#             else:
#                 bool_val = False
#                 return str(n), bool_val
#
#     def sum_num(self, *marks):
#             for i in marks:
#                 try:
#                     value,bool_val = self.filter_num(i)
#                     if bool_val:
#                         self.marks.append(value)
#                         self.total += value
#                     else:
#                         return f"Invalid input: {value}"
#                 except ValueError as e:
#                     return str(e)
#             return self.total
#
#     def get_percent(self):
#         if len(self.marks) == 0:
#             return "no marks available"
#         percent = (self.total / (len(self.marks) * 100)) * 100
#         return percent
#
#     def status(self):
#         if len(self.marks) == 0:
#             return "no status found"
#         percent = (self.total / (len(self.marks) * 100)) * 100
#         return "Pass" if percent >= 40 else "Fail"
#
#
# student = Student("John")
# student.stu_name()
# stu_filter_num = student.sum_num(84, "hi", 98, 84, 89)
# if stu_filter_num is None:
#     print(student.get_percent())
#     print(student.status())
# else:
#     print(stu_filter_num)


# class Calculator:
#     def add(self, a, b):
#         return a + b
#
#     def sub(self, a, b):
#         return a - b
#
#     def multiply(self, a, b):
#         return a * b
#
#     def divide(self, a, b):
#         if b == 0:
#             raise ZeroDivisionError("zero is not a divisor")
#         return a / b
#
#     def num_check(self, prompt):
#         while True:
#             try:
#                 num = input(prompt)
#                 return float(num)
#             except ValueError:
#                 print("Error: Input must be a number")
#
# my_cal = Calculator()
#
# while True:
#     print("1.Add: ")
#     print("2.Subtract: ")
#     print("3.Multiply: ")
#     print("4.Divide: ")
#     print("5. Exit")
#
#     try:
#         ch = input("Enter the sign: ")
#
#         if ch not in ("1", "2", "3", "4", "5"):
#             raise ValueError("invalid sign")
#         if ch == "5":
#             break
#
#         a = my_cal.num_check("Number 1: ")
#         b = my_cal.num_check("Number 2: ")
#
#         if ch == "1":
#             print("Sum: ", my_cal.add(a, b))
#         elif ch == "2":
#             print("Difference: ", my_cal.sub(a, b))
#         elif ch == "3":
#             print("Product: ", my_cal.multiply(a, b))
#         elif ch == "4":
#             try:
#                 print("Quotient: ", my_cal.divide(a, b))
#             except ZeroDivisionError as e:
#                 print("Invalid entry: ", e)
#
#     except ValueError as e:
#         print("ERROR: ", e)


#Calculate student marks and percentage
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        total = 0
        for i in self.marks:
            total += i
        return total

    def percent(self):
        if len(self.marks) == 0:
            return None
        return (self.total() / (len(self.marks) * 100)) * 100

    def show_dict(self):
        return {
            "Name" : self.name,
            "Total" : self.total(),
            "Percent": f"{self.percent():.0f}%"
        }

class StudentMarks:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def show_result(self):
        with open(self.filename, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                data = line.strip().split()
                name = data[1].strip()
                marks = list(map(int, data[2:]))
                student = Student(name, marks)
                self.students.append(student)

    def get_results(self):
        array = []
        for i in self.students:
            array.append(i.show_dict())
        return array

s1 = StudentMarks("StudentMarks.txt")
s1.show_result()
s2 = s1.get_results()
print(s2)


