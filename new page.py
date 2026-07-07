# a = "a2b3c4d2s"
# result = []
#
# i = 0
# while i < len(a):
#         letter = a[i]
#         if i + 1 < len(a) and a[i + 1].isdigit():
#             number = int(a[i + 1])
#             result.append(letter * number)
#             i += 2
#         else:
#             result.append(letter)
#             i += 1
#
# out = "".join(result)
# print(out)
from itertools import filterfalse


# a = int(input("number 1 = "))
# b = int(input("number 2 = "))
# print(a * b)

# x = input()
# print("this is " + x + " signing off")

# y = True
# while y == True:
#   x = input("Enter a number:")
#   try:
#     x = float(x);
#     y = False
#   except:
#     print("Wrong input, please try again.")

# x = "python is fun"
# print(x[::-1])

# x = "banana"
# print(x.count("a"))
#
# a = "madam"
# if a == a[::-1]:
#     print("palindrome")
# else:
#     print("false")
#
# b =  "python"
# print(b[2:])

# x = "helloworld"
# print(x[0::2])

# x = "copilotAI"
# print(x[-2:])
#
# x = "hello world"
# print(x.title())

# x = "i love python programming"
# print(x.replace(" ", "_"))
#
# x = "i love python"
# print(x.index("py"))

# x = "python makes coding easier"
# y = x.split()
# print(len(y))
#
# x = "this is a sentence"
# vowel = "aeiou"
# result = [char for char in x if char in vowel]
# print("".join(result))

# x = "programming"
# print("".join(dict.fromkeys(x)))

# x = "ABC"
# print(x.isascii())
# for asc in x:
#     print(ord(asc), end = " ")

# x = "PyThOn"
# print(x.swapcase())
#
# x = "copilot"
# reverse = ""
# for i in x:
#     reverse = i + reverse
#
# print(reverse)

# x = "abcdefghijkl"
# print(x[2::3])
#
# x = "DataScience"
# print(x[:5])
# print(x[-6:])

# x = "12345"
# print(x.isnumeric())
# Convert "python STRING practice" into "Python String Practice".


# x = "python STRING practice"
# print(x.title())

# x = "This is a string, and it is simple"
# print(x.count("is"))

# x = "abracadabra"
# print(x.replace("a", ""))

# x = "success"
# result = {}
# for i in x:
#     result[i] = result.get(i, 0) + 1
#
# print(result)

# x = "helloworld"
# print("-".join(x))


# x = "python is fun"
# reverse = ""
# for char in x:
#     reverse = char + reverse
#
# print(reverse)

# list_1 = [1,3,5,7,5,1,2,3,4,4]
# duplicate = []
# for x in list_1:
#     if list_1.count(x) > 1 and x not in duplicate:
#         duplicate.append(x)
#
# print(duplicate)


# val_1 = "madam"
# val_2 = "sky"
# if val_1[0:] == val_1[::-1]:
#     print("yes it is a palindrome")
# else:
#     print("false")


# val_1 = "madam"
# reverse = ""
# for x in val_1:
#     reverse = x + reverse
#
# if val_1 == reverse:
#     print("palindrome")
# else:
#     print("not a palindrome")


# x = 10
# print("true" if x > 5 else "false")
# print("true" if x != 5 else"false")

# x = "string"
# print("s" in x)

# x = "editorial"
# vowel = "aeiouAEIOU"
# out = {}
# for i in x:
#     if i in vowel:
#         out[i] = out.get(i, 0) + 1
#
# print(out)

# def square_num(n):
#     return n ** 2
#
# print(square_num(12))

# def is_even(num):
#     if num % 2 == 0:
#         print("true")
#     else:
#         print("the given number is odd")
#
# is_even(44)

# def greet(name):
#     print("hello "+name+"!")
#
# greet("michael")

# name1 = input("what is your favourite food: ")
# name2 = input("what is its colour: ")
# x = f"i love {name1} and it is {name2} in colour."
# print(x)

# import re
# x = "3ajs"
# y = re.findall(r'^[a-zA-Z]{3}$', x)
# if y:
#     print("true")
# else:
#     print("no match")

# def str_max(x):
#     import re
#     y = re.findall(r'^[a-zA-Z]{3}$', x)
#     try:
#         if not y:
#             raise Exception("No match found")
#         return "match found"
#     except Exception as e:
#         return str(e)
#
# x = input("enter the string: ")
# print(str_max(x))

# def dict_keys(a):
#     import json
#     y = json.loads(a)
#     swap = {value : key for key, value in y.items()}
#     return swap, swap.keys(), swap.values()
#
# x, y, z = dict_keys('{"name" : "raj", "age" : 22, "city" : "chennai"}')
# print(x)
# print(y)
# print(z)

# import re
# a = input("enter text: ")
# x = re.findall("\d", a)
# y = re.findall("[a-zA-Z]", a)
# z = re.findall("\S", a)
# if x:
#     print("".join(x))
# if z:
#     print("".join(z))
# if y:
#     print("".join(y))




#code to check if a number is prime or not
# def check_prime(n):
#     if n <= 1:
#         return "not prime"
#     for i in range(2, n):
#         if n % i == 0:
#             return "The number is composite"
#         else:
#             return "The number is prime"
#
# n = int(input("Enter the number: "))
# print(check_prime(n))


#code to calculate sum of elements in a list
# def sum_num(numbers):
#     sum = 0
#     for i in numbers:
#         sum += i
#     return sum
#
# print(sum_num([10, 20, 30, 40, 50, 60]))


# #find second largest number
# numbers = [10, 50, 20, 40, 30]
# large = large2 = float('-inf')
# for i in numbers:
#     if i > large:
#         large2 = large
#         large = i
#     elif i > large2 and i != large:
#         large2 = i
# print(large2)


#find largest of three numbers
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# if a>b and a>c:
#     print(a)
# elif b>c and b>a:
#     print(b)
# elif c>a and c>b:
#     print(c)
# else:
#     print("no match")

# price = 45
# x = f"the price is {price} dollars"
# print(x)


# numbers = [10, 50, 20, 40, 30]
# x = numbers[0::2]
# print(x)
# y = numbers[1:4:2]
# print(y)
# print(x + y)



numbers = [10, 50, 20, 40, 30]

# Bubble sort
for _ in range(len(numbers) - 1):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(numbers)  # Fully sorted list

