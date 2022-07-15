# 11.operations for Numbers in Python
print(10 + 10)
print(20 - 10)
print(20 * 10)
print(20 / 10)

# 餘數
print(20 % 10)  # 0
print(20 % 3)  # 2

# 次方
print(2 ** 3)  # 8
print(5 ** 3)  # 75

# absolute value絕對值
print(abs(-5))  # 5
print(abs(5))  # 5

# power 次方
print(pow(2, 10))  # 1024

# max最大數
print(max(10, 20, 3, 5))

# 最小數
print(min(10, 20, 3, 5))

# 四捨五入(雙數捨去，單數進位)
print(round(2.5))  # 3
print(round(3.5))  # 4
print(round(4.5))  # 4
print(round(5.5))  # 6
print(round(6.5))  # 6

# X.5, the values will be rounded up if the roundup value is an even numler
# otherwise, it will be rounded down.

# *. str(), int() and float() are for typecasting(類型轉換).
# 整數、小數
print(int(3.0))  # 3
print(float(3))  # 3.0
# 字串
print(str(3.0) + str(3.0))  # 3.03.0


# 12.Functions for Numbers
# import math
# Math Module

print(math.e)
print(math.pi)
# 無條件捨去
print(math.floor(4.9999))
# 無條件進位
print(math.ceil(4.00000001))
# 開根號  sqrt() = square root
print(math.sqrt(36))

# 13.Variable and Assignment
x = 5
x = x + 1
print(x)
programming
X = 5
X += 1
print(X)

# 14.Strings(字串) lndexing and Slicing(任意取值)
print("hello World"[6])  # -6

# revese
myString = "hello World"
print(myString[0])  # h
print(myString[-1])  # d

# [開始：結束：間距]
x = "abcdefg"
print(x[2:7])  # strint slicing
print(x[1:5:3])  # be
print(x[::-1])  # 倒反
print(x[::2])  # 雙數

# 15.String Quitations and Line
# I said "good morning"
print('I said \n "good morning"')

# 16.String Concatenation
myString1 = "Hello,"
myString2 = "my name is Floy"
print(myString1 + myString2)

myString1 = "Hello,"
myString2 = "my name is Floy"
result = myString1 + myString2
print(result)


myString1 = "Hello"
myNumber1 = 1
print(myString1 + str(myNumber1))

myString1 = "Hello"
myNumber1 = "1"
print(myString1 + myNumber1)

# 17.String Method l
# len()
print(len("Hello"))  # 5
print(int("200"))  # 整數200
name = "Floy"
# object-oriented programming
print(name.upper())  # 變大寫
print(name.lower())  # 變小寫
name = "Floy"
name.upper()
print(name)  # Floy

name = "Floy"
name2 = name.upper()
print(name2)  # FLOY

name = "Floy"
name = name.upper()
print(name)  # FLOY

# 檢查大小寫
name = "Floy"
print(name.isupper())  # False
print(name.islower())  # False
print(name.upper().isupper())  # True # method chaining

name = "Floy"
print(name.index("oy"))  # 2  子substring

# 18.Format,fstrint and replace
name = "Josh Jordan"
print(name.replace("J", "K"))

# 空格
sentence = "Today is a good day."
print(sentence.split(" "))  # 遇到空格就分開
print(list(sentence))  # typecasting

# string,number,boolean,dict,set,tuple,list

# firmat(), fstring
print("I have a strint {}".format(["asdkf", "0 0"]))  # 資料串接起來
print("{3},{0},{1}".format(20, "here is another strint", 3.14, 35))  # 選擇位置串接資料

# fstring - python 3.6
myName = "Floy"
age = 27
print(f"Hello, my name is{myName}, i'am {age} years old.")

# 19.find,count,startswith,endswith
string = "Good Day is a good day."
print(string.count("day"))  # 1
print(string.lower().count("day"))  # 2

name = "Floy"
print(name.startswith("F"))  # True
print(name.endswith("y"))  # True

# 20.Other rules of Strings
# Strings 組合
name = "Sam Donaldson"  # Pam Donaldsom
name = 'P' + name[1:]
print(name)


print("Floy" * 10)
