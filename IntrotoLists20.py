# # 21. intro to Lists
# friend1 = "Mike"
# friend2 = "josh"
# friend3 = "jerry"
# print(f"{friend1},{friend2},{friend3} are my friends.")

# # Loop 迴圈
# friendList = ["Mike", "josh", "jerry"]
# print(f"{friendList[2]},{friendList[1]},{friendList[0]} ate my friends.")
# friendList = []
# print(len(friendList))  # 0

# luckyNumber = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(luckyNumber[0:3])  # [2, 3, 4]
# print(luckyNumber[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2]

# x = [5, 0, 5]
# print(x.count(5))  # 2  x.index  # 0

# x = [5, 0, 5]
# y = [3, 4, 5]
# print(x + y * 3)


# # List 不一樣的地方
# x = [5, 0, 5]
# x[1] = 10
# print(x)

# # 22.List Functions I
# # insert() 放進去
# friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
# friends.insert(2, "Aarron")
# print(friends)

# # remove() 移除
# friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
# friends.remove("Mike")
# print(friends)

# # clear() 清空
# friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
# friends.clear()
# print(friends)

# # sort() 排序
# friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
# friends.sort()
# print(friends)

# # reverse() 反轉
# friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
# friends.reverse()
# print(friends)

# # 反轉的第二種方式
# friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
# friends = friends[::-1]
# print(friends)

# # 23.List Functions II
# # append() 附加
# friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
# friends.append("Aaron")
# friends.append("Milly")
# friends.append("5.5")
# print(friends)

# # pop() 從最後一個拿掉
# friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
# my_lost_friend = friends.pop()
# print(friends)
# print(my_lost_friend)


# # copy()
# x = [1, 2, 3, 4, 5, 6]
# y = x  # y = [1, 2, 3, 4, 5, 6]
# y[0] = 15  # y = [15, 2, 3, 4, 5, 6]

# print(x)  # [1, 2, 3, 4, 5, 6]
# print(y)  # [15, 2, 3, 4, 5, 6]

# print("--------------------")
# a = 10
# b = a   # b = 10
# b = 15   # b = 15
# print(a)  # a =  10
# print(b)    # b = 15


# x = [1, 2, 3, 4, 5, 6]
# y = x.copy()
# y[0] = 15
# print(x)
# print(y)


# # list of lists
# x = [1, 2, [4, 5, 6], 2, 1, [4, 3, [-10, 4]]]
# print(x[5][2][0])


# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(x[len(x) - 1])

# # what data types can be used for keys?

# person = {"name": "Wilson", "age": 25}
# print(person["name"])

# # what data types can be used for values?
# person = {"x": {"age": [10, 20, 30]}}
# print(person["x"]["age"][2])

# x = {}
# x["name"] = "Geace"
# x["age"] = 26
# print(x)

# x = {'name': 'Geace', 'age': 26}
# x["name"] = "Floy"
# print(x)


# # 25.Dicts Functions
# # keys()
# x = {'name': 'Geace', 'age': 26}
# print(x.keys())  # Loop
# # values()
# x = {'name': 'Geace', 'age': 26}
# print(x.values())
# # items()
# x = {'name': 'Geace', 'age': 26}
# print(x.items())   # something Like a List of tupLes


# # object
# x = {'name': 'Geace', 'age': 26}
# print(x["name"])

# # 26.what can be a key?
# # 27.intro to tuples
# mytuple = (10, "100", "Hello")
# print(len(mytuple))

# mytuple = (10, "100", "Hello")
# print(mytuple[0:2])

# mytuple = (10, "100", "Hello")
# print(mytuple.count(10))
# print(mytuple.index("Hello"))


# # 28.tuple Packing and Unpacking
# x = 10, 15  # tuple packing
# print(x)
# print(type(x))

# x = ("Wilson", 25)
# print(x[0])
# name, age = x
# print(name)
# print(age)  # variable names have meanings

# a, b = (15, 100)
# print(a)
# print(b)
# # x,y值交換
# # 1
# x = 25
# y = 35
# x = y
# y = y-10
# print(x, y)
# # 2
# x = 25
# y = 35
# temp = x    # temp = 25
# x = y       # x = 35
# y = temp    # 25

# print(x)
# print(y)
# # 3
# x = 25
# y = 35
# x, y = y, x
# # tuple packing(右邊)
# # tuple unpacking
# print(x)
# print(y)

# # 29.Mutable objects in tuples
# #  if an element in a tuple is mutable, then we can just
# # select the element, nd then change it.
# # if we want to use a tuple as a dictionary key,
# # then all elements in the tuple has to be immutable.
# a = ([1, 2, 3], "wilson")  # dictionary key? Nope!
# a[0][1] = 100
# print(a)  # ([1, 100, 3], 'wilson')

# # dictionary key?
# # 15  yes,Integer
# # 'Bob'  yes,string
# # ('Tom',[14,23,27])  no ,List
# # ['filename', (15, 16)]   no,list is mutable
# # "filename"  yes,string
# # ("filename", 25, "extension")   yes,tuple(string , Integer ,string)

# # 30.intro to sets
# mySet = set({1, 2, 3})
# print(mySet)


# myList = [1, 4, 3, 2, 5, 1, 5]
# mySet = set(myList)
# print(mySet)

# # add() clear() discard()
# s = set()
# s.add(1)
# s.add(2)
# s.discard(2)
# s.clear()
# print(s)

# # 31.Built-in Set Methods
# a = {1, 3, 4, 5}
# b = {3, 4, 7, 8}
# print(a.difference(b))   # A - B
# print(b.difference(a))   # B - A
# print(a.intersection(b))
# print(b.intersection(a))
# print(a.union(b))
# print(b.union(a))
# # 不交集
# print(a.isdisjoint(b))
# # 子集合
# print(a.issubset(b))

# # 32.Booleans in Python
# x = True
# print(x)

# # 33.python Comments and Type-checking

# x = "Floy"
# print(type(x))

# # 34.Addditional Information
# def hello():        # hello is store in RAM
#     print("hello")


# print(hello())

# myList = ["a", "b", "c", "d"]
# myString = "|".join(myList)
# print(myString)

# # 35.Value , Reference ,Sorted
# x = [4, 2, 3, 1]
# y = sorted(x, reverse=True)  # keyword arguments
# print("the list x is", x, ". Also, the list y is", y)

# # tuple
# x = {"name": "wilson", "age": 19}
# y = sorted(x)
# print(x)
# print(y)

# # set unordered collection oh unique objects
# x = [4, 5, 3, 2, 1]
# y = sorted(x)
# print(x)
# print(y)

# # Srting
# x = "How are you doing today"
# y = sorted(x)
# print(x)
# print(y)


# 36.Membership Operator

# a = "ABCD"
# if "A" in a:
#     print("A is in ", a)


# a = "A" "B" "C" "D"
# if "A" in a:
#     print("A is in ", a)

# # 37.Comparison and Assigement Operators
# # return a boolean
# # == Comparison Operators
# a = 10
# b = 20
# print(a == 20)

# a = "today is a good day."
# print(a == a.lower())


# Logical Operators
# a = True
# b = False
# print(a and b)
# print(a or b)

# a = True
# print(not a)

# # Bitwise Operators (Optional)
# a = 60
# b = 13
# print(a & b)

# a = 60
# b = 13
# print(a | b)

# a = 60
# b = 13
# print(a ^ b)

# # 39. Truthy and falsy values
# print([] and [])
# # short circuit

# if []:
#     print("empty list is true in boolean context")
# else:
#     print("empty list is false in boolean context")

# print(bool(""))

# # 40. Short-Circuit Evaluation
# print(10/0)  # 沒意義

# # if 2 or (10 / 0):
# #     print("we got no error")
