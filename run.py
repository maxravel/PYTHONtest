# x = 6
# print(x/2)
# print(type(x))
# print(type(x/2))
#
# y = "hello"
# z = " world"
# print(y+z)
# print(type(y+z))

# p = input()
# p = int(p)
# #p = float(p)
#
# print(p*2)
# print(type(p*2))


# x = "asddfafdafads"
# x = x[1:4]
# print(x)

# x = 67
# if x == 5:
#     print("x jest inne")
# else:
#     print("jakie?")
# print("gotowe")
#
# x = 6 < 7
# print(x)
# print(type(x))
#
# y = 1
# print(bool(y))


# listy
# produkty = ["ser","mleko","parówki"]
# produkty.append("pomidor")
# print(produkty[1:2])
# print(type(produkty))
# # produkty.clear()
# print(produkty)
# x = produkty.count("pomidor")
# print(x)
# wiecej_produktow = ["kawa","sos"]
# produkty.extend(wiecej_produktow)
# produkty.pop(0)
# produkty.remove("sos")
# print(produkty)


# tuple nie można edytować
# przybory = ("dlugopis","linijka","kredka")
# print(przybory)


# słowniki
# person = {"wiek":20,"imię":"ania","nazwisko":"kowalska"}
# print(person)
# print(person["wiek"])
# keys = person.keys()
# print(keys)

# pętla while
# i = 0
# while i <= 10:
#     print(i)
#     i += 1
# print("koniec")

# i=10
# while i>0:
#     print(i)
#     i -= 1
# print("koniec")

# suma = 0
# while True:
#     print("wpisz liczbę")
#     x = input()
#     suma += int(x)
#     print(suma)

# lista = ["a","b","c","d","e","f","g"]
#
# for litera in lista:
#     print(litera)
#     if litera == "e":
#         print("to jest e!")

# for i in range(10,30,2):
#     print(i)

# fruits = ["apple", "pear", "banana", "orange", "apple"]
# first one is enumerating number:
# for i, fruit in enumerate(fruits):
#     print("Sprawdzam {}".format(i))
#     if i == 3:
#         break
#     print(i)
#     print(fruit)
# print("koniec")

# x = "Hello {}"
# y = x.format("world!")
# print(y)

# fruits = ["bee", "pear", "banana", "orange", "strawberry"]
# for fruit in fruits:
#     if fruit == "pear": continue
#     print(fruit)
#     if fruit == "banana": break

# fruits = ["bee", "pear", "banana", "orange", "strawberry"]
# if "apple" in fruits:
#     print("znaleziono jabłko")
# elif "orange" in fruits:
#     print("nie znaleziono jabłka, ale mamy pomarańczę")
# else:
#     print("nic nie znaleziono")


# while True:
#     liczba = int(input())
#     if liczba > 20 and liczba < 80:
#         print("liczba jest większa od 20, ale mniejsza od 80")
#     elif liczba >100 or liczba > 80:
#         print("liczba jest większa od 100 lub od 80")
#     else:
#         print("nic")


# import time
# print("Start")
# time.sleep(2)
# # stop pojawi się po 2 sekundach
# print("Stop")

# timer = time.time()
# time.sleep(2)
# d = time.time() - timer
# print(d)

# timer = time.time()
# timer2 = time.time()
# timer3 = time.time()
# while True:
#     if time.time() - timer > 2:
#         print("minelo 2 sekundy")
#         timer = time.time()
#     if time.time() - timer2 >1:
#         print("minela 1 sekunda")
#         timer2 = time.time()
#     if time.time() - timer3 >5:
#         break

# import datetime
# teraz = datetime.datetime.now()
# print(str(teraz.hour)+" : "+str(teraz.minute))
# print(str(teraz.strftime("%H:%M  %d.%m.%Y")))


# def printme(liczba):
#     print("hello")
#     print(liczba)
#
# printme(5)

# def mnoz(a,b=4):
#     return a*b
#
# wynik = mnoz(2)
#
# print(wynik)


#
# # import file
# import new
# new.test("hello")
# new.test("121")
#
# # import function from file
# from new import test
# test("hello")
# test("121")
#
# # import all from file
# from new import *
# test("another one")
#
# def testOne():
#     print("Test one run.py")
#
# # import function with same name as another name
# from new import testOne as testOneNew
# testOne()
# testOneNew()



# files, tribes
# r - read, r+ - read+write, w - also create, w+, a, a+
# f = open("plik.txt","w")
# f.write("test1")
# f.close()
# \n - write in new line

# f = open("plik.txt","r")
# # print(f.read())
# # print(f.readlines())
# print(f.readline())
# f.close()

# f = open("plik.txt","r")
# for line in f.readlines():
#     print(line)
# f.close()



# # folders
# import os
# lista = os.listdir(".")
# print(lista)
#
# for item in os.listdir("."):
#     # print(item)
#     if os.path.isfile(item):
#         # .format put in curly braces item from ()
#         print("{} is a file".format(item))
#     elif os.path.isdir("."):
#         print("{} is a folder".format(item))
#     else:
#         print("{} is not a folder or file".format(item))

# # creating folder
# import os
# os.mkdir("newFolder")

# # rename folder
# os.rename("newFolder","bestFolder")

# # remove directory - os.rmdir("directory"); remove file - os.remove("file")
# os.rmdir("bestFolder")

# open("test2.txt","w").close()


# # making directories
# import os
# path="pliki/11/data.txt"
# print(os.path.dirname(path))
# print(os.path.basepath(path))
# print(os.path.abspath(path))
# os.makedirs(os.path.dirname(path))
# open(path,"w").close()



#exceptions

# try:
#     file = open("tekst.txt","r+")
#     file.write("tester")
#     file.close()
# # if file can't be created exception works:
# except FileNotFoundError as e:
#     print("wystąpił błąd z plikiem")
#     print(e)
#
# try:
#     file2 = open("plik.txt","r")
#     file2.write("xero")
#     file.close()
# except FileNotFoundError as e:
#     print("wystąpił błąd z plikiem")
#     print(e)
# except:
#     print("some other error")



# # objects
# class Calculator():
#     def __init__(self):
#         print("init")
#         #declaring self parametr
#         self.liczba=10
#     def __del__(self):
#         print("del")
#     def __str__(self):
#         return "hello"
#     def __len__(self):
#         return 6
#     def __bool__(self):
#         return False
#     def dodaj(self, a, b):
#         wynik = a+b
#         print(wynik)
#     def odejmij(self, a, b):
#         wynik = a-b
#         print(wynik)

# my_calculator = Calculator()
#
# my_calculator.dodaj(2,3)

# test = Calculator()
# # this del deletes test variable:
# del test
# print(test)

# test3 = Calculator()
# test3.dodaj(3,3)
# # this prints hello (__str__) when converting to string
# print(test3)

# if test3:
## __bool__ store boolean value of class
#     print("True")
# else:
#     print("Falseeee")

# calc = Calculator()
# calc.liczba = 10
# calc.liczba+=5
# print(calc.liczba)
#
# calc2 = Calculator()
# calc2.liczba+=5
# print(calc2.liczba)

# class Calculator2:
#     def __init__(self):
#         self.ostatni_wynik = 0
#
#     def dodaj(self, a, b):
#         wynik = a+b
#         self.ostatni_wynik = wynik
#         print(wynik)
#     def odejmij(self, a, b):
#         wynik = a - b
#         self.ostatni_wynik = wynik
#         print(wynik)
#
# calc21 = Calculator2()
# calc21.dodaj(3,2)
# calc21.dodaj(10,5)
# calc21.odejmij(17,9)
# print("Ostatni wynik:{}".format(calc21.ostatni_wynik))



# # inheritence
# class Parent():
#     def __init__(self):
#         print("Parent init")
#     def parent(self):
#         print("Parent parent")
#     def poke(self):
#         print("Parent poked")

# parent = Parent()
# parent.parent()
# parent.poke()

# class Child(Parent):
#     def __init__(self):
#         # super is realising parent __init__ function
#         super().__init__()
#         print("Child init")
#     def poke(self):
#         super().poke()
#         print("Child poked")
#
# child = Child()
# child.poke()
# child.parent()

# class Person():
#     def __init__(self, name):
#         self.name = name
#         self.surname = "Kwiatkowski"
#         self.age = 25
#
# class Employee(Person):
#     def __init__(self, position):
#         super().__init__("Tomek")
#         self.position = position
#         self.specialization = "Python"
#
# class Client(Person):
#     def __init__(self, name):
#         super().__init__(name)
#         self.ordered = "website"
#
# worker = Employee("programmer")
# print(worker.name)
# print(worker.position)
# print(worker.specialization)

# worker2 = Employee("designer")
# print(worker2.position)
#
# buyer = Client("Marta")
# print(buyer.name)



# # Exceptions
# class TooColdException(Exception):
#     def __init__(self, temp):
#         super().__init__("Temperature {} is below absolute zero.".format(temp))
#
# def celsius_to_kelvin(temp):
#     if temp < -273:
#         raise TooColdException(temp)
#     return temp+273
#
# # try:
# #     print(celsius_to_kelvin(-300))
# # except TooColdException:
# #     print("Too cold")
#
# print(celsius_to_kelvin(-300))



# ************TRAVERSY MEDIA CRASH COURSE

"""
this is
multiline
comments
"""

# # this prints multiline string
# print("""fsdfsdfsd
# sdsdfdsf
# sdfsdfsfds""")
#
# print("hello"[2:4])
# # this above printing ll
#
# print(2,3,4,"string")
# # printing in new line
# print("line1\nline2\nline3")

# # variables and data types
# greeting = "hello world"
# print(greeting)
# myStr = "hello"
# myInt = 5
# myFloat = 2.3
# print(type(myFloat))

# myList = [1, 2, 3, "abc"]
# myDictionary = {"a":1,"b":2,"c":3}
# print(type(myList), myList)
# print(type(myDictionary), myDictionary)
#
# print(myList[3])
# print(myDictionary["a"])



# # CONDITIONALS
# x = 4;
#
# # basic if
# if x < 6:
#     print("this is true")
#     print("only here it will be works")
#
# # if and else
# if x > 6:
#     print("your number is greater than 6")
# else:
#     print("your number is lower than 6")
#
# # elif
# color = "blue"
# if color == "red":
#     print("color is red")
# elif color == "blue":
#     print("color is blue")
# else:
#     print("color is different")
#
# # nested if
# if color == "blue":
#     if x <10:
#         print("color is blue and x is lower than 10")
#
# # logical operators
# if color == "blue" and x <10:
#     print("true")



# # LOOPs
# # FOR LOOP
# people = ["jonh","barry","bob","alf"]
# for person in people:
#     print("current person: ", person)
#
# for i in range(len(people)):
#     print("current person: ", people[i])
#
# for i in range(1,10):
#     print(i)
#
# # while loop
# count = 0
# while count < 10:
#     print("count: ", count)
#     if count == 5:
#         break
#     count = count + 1



# # functions
#
# # default name is barry, but when you put different function output will be different
# def sayHello(name = "barry"):
#     print("hello", name)
#
# sayHello("alf")
#
# def getSum(num1,num2):
#     total = num1 + num2
#     return total
#
# numSum = getSum(3,4)
# print(numSum)
#
# # scope
# def addOneToNum(num):
#     num = num + 1
#     print("value inside a function", num)
#     return num
#
# num = 5
# addOneToNum(num)
# print("value outside a function", num)
#
# def addOneToList(myList):
#     myList.append(4)
#     print("myList inside function: ", myList)
#
# myList = [1,2,3]
# addOneToList(myList)
# print("myList outside function:", myList)



# # string functions
# myStr = "Hello World!"
#
# # only first letter is capitalize
# print(myStr.capitalize())
#
# # first letter is lower, other are capitalize
# print(myStr.swapcase())
#
# # get length
# print(len(myStr))
#
# # replace
# print(myStr.replace("World","Everyone"))
#
# # count - counting nummber of something
# sub = "l"
# print(myStr.count(sub))
#
# # startswith() - checking if something starts with signs
# print(myStr.startswith("Hello"))
#
# # endswith() - checking if string ends with parameter substring
# print(myStr.endswith("!"))
#
# # split to list
# print(myStr.split())
#
# # find - checking position of substring
# print(myStr.find("lo"))
#
# # index
# print(myStr.index("l"))
#
# # is alphanumeric - checking if string is alphanumeric
# print(myStr.isalpha())



# WORKING ON MODULES
# # you need to have file new.py with function sayHello
# import new
# new.sayHello("mark")

# # you import only one function
# from new import sayGoodbye
# sayGoodbye("andy")



# # OPENING FILES
# openingVariable = open("plik.txt","w")
# # printing name of file
# print("Name: ", openingVariable.name)
# # checking if file is closed
# print("Is Closed: ",openingVariable.closed)
# # checking mode of file
# print("Mode of file: ", openingVariable.mode)
# openingVariable.write("Python is ok")
# openingVariable.write("Javascript is better")
# openingVariable.close()
#
# # opening again and write something replace the previous text
# openingVariable = open("plik.txt","w")
# openingVariable.write("i don't like java")
# openingVariable.close()
#
# # using append mode - letter "a" - append new text,
# openingVariable = open("plik.txt","a")
# openingVariable.write(" python is the best")
# openingVariable.close()
#
# # using "r+" mode you can read variable and print it out
# openingVariable = open("plik.txt", "r+")
# readingVariable = openingVariable.read(10)
# # reading only first 10 characters when you put 10 in read()
# print(readingVariable)



# CLASSES & OBJECTS
class Person:
    __name = ''
    __email = ''

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

andy = Person()
andy.set_name("Andy")
andy.set_email("andy@gmail.com")
print(andy.get_name())

# this don't' work!!!!!!!!!!!!11
mark = Person("Mark", "mark@gmail.com")
print(mark.get_name())


