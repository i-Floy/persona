# # 40.Control Flow and If Statement
# if True:
#     print("This is so true!!")
# else:
#     print("This is False")

# # <8 => free
# # >= 65 => 300
# # >= 65 => half
# age = 18
# if age < 8:
#     print("Movie is free for you!!")

# elif 8 <= age < 65:
#     print("you need to pay $300!!")
# else:
#     print("you only need to pay $150!!")

# if (5 > 3) and []:
#     print("the condition is true")
# else:
#     print("the condition is false")

# k = True
# if k:
#     print("Variable k is true")
# else:
#     print("Variable k is false")


# # program asks user's name
# # cash
# # Y/N
# # program check if the user has more than or equal to $30
# # 42.breakfast program
# name = input("Enter you name:")  # String
# # print("your name is " + name)
# money = input("Enter you cash amount:")   # String
# hungry = input("Are you hungry? (Y/N)")  # String

# if hungry == "Y":
#     if int(money) >= 30:
#         print(f"{name} hsould go eat breakfast")
#     else:
#         print(f"{name} is hungry but might not have enough money to but breakfast")
# elif hungry == "N":
#     if int(money) >= 30:
#         print(f"{name} has budget but doesn't want to eat breakfast.")
#     else:
#         print(f"{name} has no money but is not hungry.. ")
# else:
#     print("Please male sure that you enter either Y or N.")

# # 43. foe loop
# # for variable in iterable:
# #   do something here
# for letter in "Hello World":
#     if(letter == letter.upper()):
#         print(letter)

# myList = [1, 3, 5, 7, 9]

# for num in myList:
#     print(num ** 2)

# # a list of tuple
# for a, b in [(1, 2), (3, 5), (5, 7)]:
#     print(a + b)

# # dictionart(keys)
# myDictionary = {"nsme": "Wilson", "age": 25}

# for key, value in myDictionary.items():
#     print(f"The key is {key}")
#     print(f"The value is {value}")

# # set
# for i in {1, 3, 5, 7, 9}:
#     print(i)

# # 44.while loop
# x = 0
# while x < 5:
#     print(x)
#     x += 1  # we must write this line of code


# # 45. Nested Loop 巢狀迴圈
# counter = 0
# for i in "1234":
#     for j in "ABCDEFG":
#         print(i, j)
#         counter += 1
#         print(f"counter is new {counter}")
# # 4 X 7 = 28

# # pass
# if True:
#     pass
# else:
#     print("hello")

# def Hello():
#     pass

# # break
# print("before the for loop")
# for i in "123456789":
#     if i == "5":
#         break
#     else:
#         print(i)
# print("After the for loop")
# for i in "123456789":
#     if i == "5":
#         break
#     else:
#         print(i)

# for i in "1234":
#     if i == "5":
#         break
#     for j in "ABCDEFG":
#         if j == "C":
#             break
#         else:
#             print(i, j)


# # Continue 繼續

# for i in "ABCDE":
#     if i == "B":
#         continue
#     print(i)

# for i in "ABCDEF":
#     print("New the current i is " + i)
#     continue
#     print("Here is the line after continue")


# # 47.Range Function
# print(range(100))

# for i in range(10, 20):  # range() function returns an iterable object
#     print(i)

# # 48.lmprovement of range function

# # 49.Enumerate and Zip Function
# counter = 0
# for letter in "How are you today?":
#     if counter < 10:
#         print(letter)
#     counter += 1

# for letter in enumerate("How are you today?"):
#     print(item)

# for counter, char in enumerate("How are you today?"):
#     if counter < 10:
#         print(char)

# x = [1, 2]
# y = ['A', 'B', 'C']
# z = ['a', 'b', 'c', 'c']
# for tuple in zip(x, y, z):
#     print(tuple)

# # 50.List Comprehension
# x = [1, 2, 3, 4]
# # squared_x = [1, 4, 9, 16]
# squared_x = []
# for item in x:
#     squared_x.append(item ** 2)
#     print(squared_x)


# x = [1, 2, 3, 4]

# squared_x = [item ** 2 for item in x if item > 2]
# print(squared_x)


# # Dictionary Comprehensions
# x = [1, 2, 3, 4]

# x_squared_dict = {item ** 2 for item in x if item > 2}
# print(x_squared_dict)

# # Set Comprehensions
# x = [1, 2, 3, 4]

# x_squared_set = {item ** 2 for item in x if item > 2}
# print(x_squared_set)

# # Generator Comprehensions
# x = [1, 2, 3, 4]

# x_squared_generator = {item ** 2 for item in x if item > 2}
# # print(x_squared_generator)
# for i in x_squared_generator:
#     print(i)


# # 53.intro to Functions and Methods
# myList = [1, 2, 3, 4]
# myList.insert(2, 10)
# help(myList.insert)

# def sayHi():
#     print("Hello, how are you?")


# # function execution, invokation
# sayHi()


# def addition(x, y):
#     print(x + y)


# addition(15, 35)

# # 54.parenthesis are local variables
# # x,y are the parmeters
# def addition(x, y):
#     print(x + y)

# # 15,20 are the arguments
# addition(15, 20)

# a = 30
# b = 25


# def addition(x, y):
#     print(x + y)


# addition(a, b)  # arguments can be variables as well

# # global variables , local variables
# a = 5   # global variable


# def f1():
#     x = 2  # f1 function's local variable
#     y = 3  # f1 function's local variable
#     print(x, y, a)


# def f2():
#     x = 10  # f2 function's local variable
#     y = 17  # f2 function's local variable
#     print(x, y, a)


# f1()

# a = 10 無法改變a

# # parameter (inputs) are local variables in the function


# def change(num):
#     # num = a (copy by value) => num = 10
#     num = 25


# change(a)
# print(a)


# a = [1, 2, 3, 4]

# # parameter (inputs) are local variables in the function


# def change(lst):
#     # lst = a (copy by reference) => Lst = a
#     lst[0] = 100


# change(a)
# print(a)


# a = 10

# # can we ever change any copy by value global variables?


# def change(num):
#     global a
#     a = 25


# change(a)
# print(a)

# def myAddition(a, b):
#     """ This function does addtion for inputs a and b"""
#     print(a + b)


# help(myAddition)


# # 55. return keyword
# def myAddition(a, b):
#     return a + b

# resul1 = myAddition(10, 18)
# resul2 = myAddition(26, 19)
# resul3 = myAddition(15, 17)
# print(resul1+resul2+resul3)

# def myAddition(a, b):
#     result = a + b

#     print(result)
#     return result


# myAddition(10, 15)
# # evaluate
# # python sandbox


# def myAddition(a, b):
#     for i in range(a):
#         for j in range(b):
#             if i == 3 and j == 4:
#                 return
#             print(i, j)


# print(myAddition(10, 15))

# # 56.Import Functions
# # 57.Positional and Keyword Arguments

# def exponent(a, b):
#     return a ** b


# # positional arguments
# print(exponent(2, 3))  # 8
# print(exponent(3, 2))  # 9

# def exponent(a, b):
#     return a ** b


# # keyword arguments
# print(exponent(b=2, a=10))


# myList = [4, 6, 3, 2, 1]
# print(sorted(myList, reverse=False))
# # myList is positional argument
# # reverse=False is keyword argument

# # 58.Default Arguments in Python
# # Default Argument
# def sum(n1=10, n2=0):
#     return n1 + n2


# print(sum())

# def sum(n1=0, n2=0):
#     return n1 + n2


# print(sum(n2=100, n1=50))

# # 59.Arbitrary Number of Arguments
# def sum(*args):
#     print(args)
#     print(type(args))


# sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def sum(*args):
#     result = 0
#     for number in range(0, len(args)):
#         print(f"We are now at number {number}.")
#         print(f"also, args[number] is {args[number]}. ")
#         result += args[number]
#         print(f"Now, the result is {result}")
#     return result


# print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def myfunc(**Kwargs):
#     # print(Kwargs)
#     # print(type(Kwargs))
#     print("{} is now {} years old.".format(Kwargs["name"], Kwargs["age"]))


# myfunc(name="Wilson", age=25, address="Hawaii")

# def myfunc(*args, **Kwargs):
#     print("I Would like to eat {} {}".format(args[1], Kwargs["food"]))


# myfunc(14, 17, 23, "Hello", name="wilson", food="eggs")


# def myfunc(*whatever, **Kwargs):
#     print("I Would like to eat {} {}".format(whatever[1], Kwargs["food"]))


# myfunc(14, 17, 23, "Hello", name="wilson", food="eggs")
# 要照順序排
# 1. normal argument (p1, p2)
# 2. default argument
# 3. *args
# 4. **Kwargs

# def func(p1, p2, p3="three", *args, **Kwargs):
#     print("----------------------------------------")
#     print(p1, p2, p3, args, Kwargs)


# func(1, 2, 3, 4, 5, x=1, y=3)
# func(1, 2, 3, 4, x=4)
# func(1, 2, 3, 4)
# func(1, 2, 3)
# func(1, 2)
# # func(1)

# # 60.Higher-Order Function


# def printMant():
#     for i in range(1, 89, 3):
#         print(i)


# printMant()
