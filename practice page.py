# def myfunc(fname):
#     return fname + " " + "world"
#
# print(myfunc("hello"))
from binascii import a2b_qp

# def myfunc (name = "alexa"):
#     print("hey", name)
#
# myfunc()
# myfunc("google")
#
# def myfunc(name, place):
#     print("hi", name + " " +  "i am from", place)
#
# myfunc("google", "nowhere")

# def myfunc(name, place):
#     print("hi",  name + " " + "I am coming from", place)
#
# myfunc("google", place = "norway")

# def myfunc(fruits):
#     for x in fruits:
#         print(x)
#
# fruits = ["apple", "banana", "cherry"]
# print(myfunc(fruits))

# def myfunc(*names):
#     print("my name is ", names[0])
#
# myfunc("alexa", "google", "siri")

# def myfunc(**names):
#      print("my name is ", names["name2"])
#
# myfunc(name = "google", name2 = "siri" )

# def myfunc(greeting, *name):
#     for name in name:
#         print(greeting, name)
#
# myfunc("hello",  "google", "siri")


# def my_func(name, *args, **kwargs):
#     print(name)
#     print(args)
#     print(kwargs)
#
# my_func("google",  "modem", name1 = 23)

# def square_num(n):
#     return n ** 2
#
# print(square_num(21))
#
#
# def iseven_num(num):
#     if num % 2 == 0:
#         print("True")
#     else:
#         print("False")
#
# iseven_num(21)
# iseven_num(200)


# def greet(name):
#     print("hello", name)
#
# greet("google")
# greet("siri")

# def factorial(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#        return n * factorial(n - 1)

# print(factorial(5))

# def sum(n):
#     if n == 0:
#         return n
#     else:
#         return n + sum(n - 1)
#
# print(sum(15))


# def myfunc(x):
#     if x == 0:
#         yield x
#
# for values in myfunc(0):
#     print(values)
#
# print(list(myfunc(0)))


# def myfunc():
#     x = 500
#     def fun2():
#         x = 210
#         print(x)
#     fun2()
#
# myfunc()
# print(myfunc())


# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner()
#
# @changecase
# def myfunc():
#      return "hello world"
#
# print(myfunc())

# def myfunc(a, b):
#     print(a + b)
#     print(a - b)
#     print(a * b)
#     print(a / b)
#
# a = int(input("number 1: "))
# b = int(input("number 2: "))
# myfunc(a, b)


# a = "a2b3c4d2s"
# result = []
#
# i = 0
#     while i < len(a):
#         letter = a[i]
#         if i + 1 < len(a) and a[i + 1].isdigit():
#             number = int(a[i + 1])
#             result.append(letter * number)
#             i += 2
#         else:
#             result.append(letter)
#             i += 1
#
#
# out = "".join(result)
# print(out)


# def str_num(a):
#     result = []
#     i = 0
#     while i < len(a):
#         letter = a[i]
#         if i+1 < len(a) and a[i+1].isdigit():
#             number = int(a[i+1])
#             result.append(letter * number)
#             i += 2
#         else:
#             result.append(letter)
#             i += 1
#
#     out = "".join(result)
#     return out
#
# print(str_num("a2b3c4d2s"))


# a = [1, 2, 2, 1, 3, 4, 3, 5, 6, 6, 7, 7]
# result = []
# result2 = []
# for num in a:
#     if num not in result:
#         result.append(num)
#     else:
#         if num not in result2:
#             result2.append(num)
# result2 = [ num for num in result if num  in result2 ]
# print(result)
# print(result2)

# def num_dup(a):
#     result = list(set(a))
#     result2 = list(set([x for x in a if a.count(x) > 1]))
#
#     return result, result2
#
# unique, duplicate = num_dup([1, 2, 2, 1, 3, 4, 3, 5, 6, 6, 7, 7])
# print("unique list: ", unique)
# print("duplicates: ", duplicate)

# sen ="i love python"
# print(sen[::-1])

# sen = "i love python"
# reverse = ""
# for x in sen:
#     reverse = x + reverse
#
# print(reverse)

# sen = "i love python"
# reverse =  sen.split()
# print(reverse)
# result = " ".join(reverse[::-1])
# print(result)


























