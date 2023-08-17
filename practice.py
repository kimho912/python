'''
print(3*(3+1))
print('ballun')
print("butterfly")
print("?"*8)

#True / False
print(5 > 10)
print(10 > 5)
print(True)
print(not True)
print(not (5 > 10))
'''
#variables
'''
animal = "Cat"
name = "Lucy"
age = 4
hobby = "walking"
is_adult = age >= 3

print("My " + animal + " name is " + name)
hobby = "playing soccer"
# print("She is " + str(age) + " years old, and likes " + hobby)
print("She is" , age , "years old, and likes" , hobby)
print("is " + name + " an adult? " + str(is_adult))

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
'''

#Arithmetic Operators
'''
print(2**3) #2^3
print(5//3) # 1
print(10//3) # 3

number = 2 + 3 * 4
print(number)
number += 2
print(number)
'''
#random
'''
from random import *
print(int(random()*10))

print(randrange(1, 46))
print(randint(1, 45)) #1-45
'''
#문자열
'''
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """나는 소년이고,
파이썬은 쉬워요"""
print(sentence3)
'''

'''slicing'''
# jumin = "990120-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[:6])
# print("뒤 7자리 : " + jumin[7:])
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:])

'''문자열처리함수'''
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Jave"))

# index = python.index("n")
# print(index)
# #next index
# index = python.index("n", index + 1)
# print(index)

# print(python.find("Java"))

# print(python.count("n"))

'''문자열포맷'''
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요" % "파이썬")
# print("Apple 은 %c로 시작해요." % "A")
# # %s
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# print("I'm {age} years old, and like {color} color.".format(age = 20, color = "Red"))
# print("I'm {age} years old, and like {color} color.".format(color = "Red", age = 20))

# age = 20
# color = "red"
# print(f"I am {age} years old, and I like {color} color.")

'''exiting character'''
# # \n : new line
# print("Hi, \nI'm Kim")

# # \" \'
# print("Hi, My name is \"Kim\".")

# # \r : move the cursor to the front
# print("Red Apple\rPine")

# # \b : backspace (delete one character)
# print("Redd\bApple")

# # \t : tap

# quiz
'''url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")] 
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(f"The password of the site, {url}, is {password}.")'''

# list
'''subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# find the index
print(subway.index("조세호"))
# append at the end
subway.append("하하")
print(subway)
# insert in the middle
subway.insert(1, "정형돈")
print(subway)
# delete one person from the end
print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# sort
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

num_list = [5,2,4,3,1]
mix_list = ["Seho", 20, True]
print(mix_list)
# extend list
num_list.extend(mix_list)
print(num_list)'''

#dictionary (gym)
'''cabinet = {3:"hyunho", 100:"Gaeun"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5,"availale"))

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"ABC", "B-100":"DEF"}
print(cabinet.get("A-3"))
print(cabinet.get("B-100"))

# new customer
print(cabinet)
cabinet["A-3"] = "GHI"
cabinet["C-20"] = "JKL"
print(cabinet)

# gone customer
del cabinet["A-3"]
print(cabinet)

# print keys
print(cabinet.keys())

# print values
print(cabinet.values())

# print pairs of keys and values
print(cabinet.items())

# closing the gym
cabinet.clear()
print(cabinet)'''

#tuples
'''menu = ("Donkasu", "Cheesekasu")
print(menu[0])
print(menu[1])

# name = "Hyunho"
# age = 27
# hobby = "workout"
# print(name, age, hobby)

(name, age, hobby) = ("Hyunho", 27, "workout")
print(name, age, hobby)'''

# set
'''# no duplicates, no order
my_set = {1,2,3,3,3}
print(my_set)

java = {"A","B","C"}
python = set(["A","D"])

# intersection (java and python)
print(java & python)
print(java.intersection(python))

# Union ( java or python)
print(java | python)
print(java.union(python))

# difference (java - python)
print(java - python)
print(java.difference(python))

# adding
python.add("B")
print(python)

java.remove("B")
print(java)'''

# changing data structure
# cafe
'''menu = {"coffee", "milk", "juice"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))'''

# quiz
'''from random import *
ids = list(range(1,21))
shuffle(ids)
winners = sample(ids, 4)
chicken = winners[0]
coffee = winners[1:]

print(f" -- Winners -- \nChicken : {chicken} \nCoffee : {coffee} \n -- Congrats --")'''

# if
'''weather = "sunny"
weather = input("How is the weather? ")
if weather == "rain" or weather == "snow":
    print("bring your unbrella")
elif weather == "bad":
    print("bring a mask")
else:
    print("don't need anything")

temp = int(input("What's the temperature? "))
if 30 <= temp:
    print("Too hot. Don't go out")
elif 10 <= temp and temp < 30:
    print("nice weather!")
elif 0 <= temp < 10:
    print("bring a coat")
else:
    print("Too cold, don't go out")'''

# for
'''for waiting_no in range(1, 6):
    print(f"Waiting number : {waiting_no}")

starbucks = ["Iron man", "Thor", "Grute"]
for customer in starbucks:
    print(f"{customer}, your coffee is ready")'''

# While
'''customer = "Thor"
index = 5
while index >= 1:
    print(f"{customer}, your coffee is ready. {index} call(s) left.")
    index -= 1
    if index == 0:
        print("your coffe is disposed")

customer = "Iron-man"
person = "Unknown"

while person != customer:
    print("{0}, your coffee is ready. ".format(customer))
    person = input("What is your name? ")'''

# continue & break
'''absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("{0}, come to the office".format(student))
        break
    print("{0}, read a book.".format(student))
'''
# for 2
'''students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)'''

# quiz
'''from random import *
total = 0
for i in range(1,51):
    time = randrange(5,51) 
    if 5 <= time <= 15:
        print("[O] {0} customer (spent time : {1}mins)".format(i, time))
        total += 1
    else:
        print("[ ] {0} customer (spent time : {1}mins)".format(i, time))

print("Total : {0}".format(total))'''

# function
def open_account():
    print("a new account is activated.")

def deposit(balance, money):
    print("Deposing is completed. balance is now ${0}.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print(f"Complete. Balance is now ${balance - money}.")
        return balance - money
    else:
        print(f"Not complete. Balance is ${balance}.")
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
# print(balance)
commission, balance = withdraw_night(balance, 500)
print(f"commission = ${commission}, balance = ${balance}")
