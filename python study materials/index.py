# print("hello world")
# a=50
# b=25
# c="adil"
# add = a+b
# sub = a-b
# mult = a*b
# div = a/b
# print(add)
# print(sub)
# print(mult)
# print(div)
# print(type(a))
# print(type(c))

# from sqlite3 import connect
# from tkinter import W


# x,y,z = "apple","banana","cherry"
# print(x,y,z)




# def myfunction():
#     global x
#     x=56
#     print(x)
    
# myfunction()
# myfunction()

# print(x)

# print(x)

# h = 65
# i = 5.59
# j = 1j

# print(type(h))
# print(type(i))
# print(type(j))



# x=int(3.5)
# print(x)



# a = "adil"
# b = "shabab"
# print(a+'  '+b)

# p="hello world"
# print(p)
# print(p[3])
# print(p[6])
# print(p[8])
# print(p[3:8])
# print(p[-5])
# print(p[-5:-1])
# print(p[-5:8])
# print(p[6:11])


# print("hello\bworl\t d")

# w="hello world"
# for y in w:
#     print(y)

# for x in "orange":
#         print (x)
#         print(len(x))

# print(len(x))
# print(len(w))

# p = "years old"
# age = 17
# name = "adil"
# i = "i"
# text = "my name is {} and {} am {} {}"
# print(text.format(name,i,age,p))
# text = "adil shabab"
# print("id" in text)
# print("il s" in text)
# print("bab" in text)
# print("bab" not in text)





# content = "hello world"
# print(content.upper().replace("HELLO", "hai"))
# print(content[:5].upper())
# print(content[2:].lower())
# print(content[:].upper())
# print(content[-5:-2].lower())
# print(content.replace("ld","md"))

# k = "hello hello"
# print(k.replace("llo he", "llodf he"))


# a = "adil shabab"
# x = a.capitalize()
# print(x)
# print(a.capitalize())




# ==============================================================================================================================================
# methods 

# a = "545451545145"
# b=('','adil','minnu','ammu')
# x="hloo".join(b)
# print(x)
# print(a.casefold())          #1
# print(a.isupper())           #2
# print(a.islower())           #3
# print(a.index("a"))          #4
# print(a.isalnum())           #5
# print(a.isalpha())           #6
# print(a.isnumeric())         #7
# print(a.center(20))          #8
# print(a.find("dg"))          #9
# print(a.isdigit())           #10
# print(a.startswith("a"))     #11
# print(a.isnumeric())         #12
# ==============================================================================================================================================




# print(bool(15>25))                   # to check is it boolean 



# ==============================================================================================================================================
# arithmatic operators

# print(50+56)
# print(70-56)
# print(7*5)
# print(75/5)
# print(5%2)
# print(50%7)
# print(45%20)
# print(2 ** 5)           #same as 2*2*2*2*2          exponention
# print(15//2)            #floor dvision              removes the decimal points
# ==============================================================================================================================================






# ==============================================================================================================================================
# assignment operators

# a=5
# b=2

# a+=b
# print(a)
# a-=b
# print(a)
# a/=b
# print(a)
# a*=b
# print(a)
# a>=b
# print(a)
# a<=b
# print(a)
# a>b
# print(a)
# a<b
# print(a)
# a//=b
# print(a)
# a**=b
# print(a)
# a>=b
# print(a)


# ==============================================================================================================================================






# ==============================================================================================================================================
# comparision operators 

# print(5 == 2)
# print(5 != 2)
# print(5 > 2)
# print(5 < 2)
# print(5 >= 2)
# print(5 <= 2)
# ==============================================================================================================================================



# Array ======================================================================================================================================

# list = ["adil","java", "python", "c++", "sql", "php", "c#" ]
# list3 = ["django", "react js", "node js", "vue js"]
# print(list)
# print(list[2])
# print(list[3])
# print(list[5])
# print(len(list))
# print(len(list[0]))
# print(list[0:4])
# print(list[:5])
# print(list[3:])
# print(list[::-1])
# to change the value of the specific item refers to the index value
# list[2] = "javascript"
# print(list)
# insert the item = to insert a new list item without replacing any of existing values we can use insert method, the insert method an item in the specified index value 
# list.insert(3, "React JS")
# print(list)
# append item = to add an item to the last of list 
# list.append("vue js")
# print(list)
# extend list = to append elements from another list to the current list using extend method
# list.extend(list3)
# print(list)
# remove a specified item = to remove method removes the specified item 
# list.remove("vue js")
# print(list)
# pop method = the pop method removes specified index 
# list.pop(3)
# remove last item if we didn't specify any index 
# list.pop()
# del list[0]
# print(list)
# to delete all items in list use clear method 
# list.clear()
# print(list)
# for x in list:
#     print(x)
# for x in range(len(list)):
#     print(list[x])
# for y in range(16):
#     print(y)
# for m in range(15,26):
#     print(m)
# sort method = list method have a sort method that will be sorted the list alpha numerically 
# list.sort(reverse=True)
# print(list)
# list.sort()
# print(list)
# print(min(list))

# numbers = [1,254,842,42,82,75,2,74]
# print(min(numbers))
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)


# an = ['adil','ammu','123','134','reshu']
# an.sort()
# print(an)
#Array =========================================================================================================================================




# nested list
# list2 = ["apple", [2,3,5,85], 5.821]
# print(list2[1][2])
# print(list2[1][3]) 
# print(list2[-2][-1])


# =====================================================================================================

# l = ["apple", "mango", "orange"]
# l2 = [2,2,5,6,8,6,6,8,56,96,]
# l3 = l+l2
# print(l3)
# print(l2.count(2))
# print(l2.count(6))



# tuple1 = ("apple","apple", 1, "kiwi", 8, "kiwi" "banana", "mango", 1,8)
# tuple3 = (45,56,93,80)
# print(type(tuple1[4]))
# print(tuple1[0:4])
# list4 = (list(tuple1))
# list4[0] = "kiwi"
# print(list4)
# tuple2 = (tuple(list4))
# print(tuple2)
# y=("orange",)
# tuple1+=y
# print(tuple1)
# list5 = (list(tuple1))
# list5.remove("apple")
# print(list5)
# tuple2 = (tuple(list5))
# print(tuple2)
# # del tuple2
# print(tuple2)
# for x in tuple1:
#     print(x)

# tuple4 = tuple1+tuple3
# print(tuple4)

# tuple5 = tuple1*2
# print(tuple5)


# print(tuple1.count("kiwi"))
# print(tuple1.count(1))
# print(tuple1.count(8))
# print(tuple1.count("apple"))

# z=(3,6,8,9,0,3,6)
# s=z.index(4)
# print(s)

# print(tuple1.index("kiwi"))
# tu=(2,4,7,8,9,19)
# s=tu.index(8)
# print(s)




# ============================= set =================================== 
# set1 = {"apple", "banana",2, "kiwi", "apple"} # not allowed duplicate values
# set2 = {2,354,56,45,4,1,54,21,54,0,5,4,"apple"}
# # print(set)
# print(len(set1))
# for x in set1:
#     print(x)
# print("apple" in set1)
# set1.add("orange")
# print(set1)
# set1.update(set2)
# print(set1)
# set1.remove("apple")
# print(set1)
# set1.discard("banana")
# print(set1)
# set1.pop()
# print(set1)
# set1.clear()
# print(set1)
# del set2
# print(set2)
# set3 = set1.union(set2)
# print(set3)
# set1.intersection_update(set2)
# print(set1)
# set1.symmetric_difference_update(set2)
# print(set1)
# ============================= set =================================== 





# ==================================== dictionary =========================
# dictionary1={"name":"adil","age":17}
# print(dictionary1)
# print(dictionary1["name"])
# print(dictionary1["age"])
# print(len(dictionary1))
# x = dictionary1.get("name")
# print(x)
# y = dictionary1.keys()
# print(y)
# z= dictionary1.values()
# print(z)
# u = dictionary1.items()
# print(u)
# if "name" in dictionary1:
#     print("yes ")
# else:
#     print('not in')
# dictionary1["name"]= "shabab"
# print(dictionary1)
# dictionary1.update({"name":"adil"})
# print(dictionary1)
# dictionary1["blood-group"] = "o positive"
# print(dictionary1)
# dictionary1.pop("name")
# print(dictionary1)
# dictionary1.popitem()
# print(dictionary1)
# del dictionary1 ["age"]
# print(dictionary1)
# dictionary1.clear()
# print(dictionary1)
# for x in dictionary1.keys():
#     print(x)
# for x in dictionary1.items():
#     print(x)
# for x in dictionary1.keys():
#     print(x)
# for x in dictionary1.keys():
#     print(x)
# ==================================== dictionary =========================





# ========================= nested dictionary ==========================
# students = {
#     "student1" :{
#         "name": "adil",
#         "age": 17,
#         "place": "padikkal"
#     },
#     "student2" :{
#         "name": "shaba",
#         "age": 27,
#         "place": "calicut"
#     }
# }
# print(students)
# print(students["student2"].get("age"))
# print(students["student2"].get("name"))
# ========================= nested dictionary ==========================




# num = int(input("enter the number"))
# digit = num%10
# print("last number is = ", digit)



# num1 = int(input("enter first number"))
# num2 = int(input("enter second number"))
# sum = num1 + num2
# print("Result is :", sum)

# # loop ================================== loop ==================================== 
# i=0
# while i<8:
#     print(i)
#     i+=1
    
    
# i=0
# while 1<8:
#     print(i)
#     if i==3:
#         break
#     i+=1
    
    
    
# i=0
# while i<8:
#     i+=1
#     if i == 3:
#         continue
#     print(i)
# loop ================================== loop ==================================== 




# for loop  ============================================== for loop
# x = ["apple", "orange", "banana", "mango", "lemon", "cherry"]
# y = "Adil shabab"

# for i in x:
#     print(i)

# for y in x:
#     if y == "mango":
#         break
#     print(y)

# for x in y:
#     if x == "b":
#         break
#     print(x)

# for fruit in x:
#     if fruit == "orange":
#         continue
#     print(fruit)

# for x in y: 
#     print(x)


# for x in range(1,100):
#     print(x)

# for loop  ============================================== for loop



# num = int(input("enter a number"))
# if num>=0:
#     print("entered number is positive number")
# else:
#     print("entered number is negetive")



# for x in range (6):
#     if x == 2:
#         break
#     print(x)
# else:
#     print("finished")
    
    
    
    # ================================== Nested lopp ===================================================
    
# x = ["red","blue","black","orange"]
# y = ["apple", "mango", "banana", "orange"]

# for a in x:
#     for b in y:
#         print(a,b)
        
    # ================================== Nested lopp ===================================================
    
    
    # break and continue is control statement 
    
    
    
    
    
    # ============================= python function ==============================
    # def my_function():
    #     print(range(8))
    
    
    
# ============================================== first question ============================================
# mark = int(input("Enter your mark"))
# if mark <25:
#     print("Failed")
# if mark >25 and mark<45:
#     print("E Grade")
# if mark >45 and mark<50:
#     print("D Grade")
# if mark >50 and mark<60:
#     print("C Grade")
# if mark >60 and mark<80:
#     print("B Grade")
# if mark >80: 
#     print("A Grade")
    
# ====================================== second question ===================================== 
# num1 = int(input("Enter First Number"))
# num2 = int(input("Enter Second Number"))
# if num1>num2:
#     print(num1)
# else:
#     print(num2)
    
# ============================================ third question ========================================

# year = int(input("Enter the year"))
# if year%100==0 and year%400==0:
#     print(year , "is leap year")
# elif year%4 ==0 and year%100!=0:
#     print(year, "is leap year")
# else:
#     print(year, "is not leap year")
    
# ============================================== fourth question ======================================
# number = int(input("Enter 1 to 12"))
# if number == 1:
#     print("january")
# if number == 2:
#     print("february")
# if number == 3:
#     print("march")
# if number == 4:
#     print("april")
# if number == 5:
#     print("may")
# if number == 6:
#     print("june")
# if number == 7:
#     print("july")
# if number == 8:
#     print("august")
# if number == 9:
#     print("september")
# if number == 10:
#     print("october")
# if number == 11:
#     print("november")
# if number == 12:
#     print("december")
# if number >12:
#     print("please enter 1 to 12")



# =============================================== FUNCTION ==============================================================
# def my_function():
#     print("Hello world")

# my_function()




# def function(fname,lname):
#     print("my name is "+ fname +" "+ lname)


# function("Adil","shabab")


# ===================================== arbitary arguments ===========================
# def function(*all):
#     for x in all:
#         print("all elements are", x)

# function("adil","shabab","ajith","salman","aryan")
# ===================================== arbitary arguments ===========================


#we can pass arguments as key value pairs ===================================
# def my_function(child1, child2, child3, child4):
#     print("the small child is ", child2)

# my_function(child1="adil", child2="shabab", child3="ajith", child4="salman")

# passing arguments as key value pairs in arbitary ===============================
# def function(**kid):
#     print("the small child is ", kid["fname"])
    
# function(fname="adil", lname="shabab")

# ========================== default parameters =====================
# def function(country="India"):
#     print("I am coming from ", country)

# function("USA")
# function("mexico")
# function("china")
# function()

# ========================= return ==========================
# def function(x):
#     data = 10+x
#     return data
# print(function(62))
# print(function(20))


# to remove error message if we have a function and nothing to do 
# def my_function():
#     pass

# ====================================================== lambda function ==================
# y = lambda a:a+10
# print(y(5))

# x = lambda a,b,c:a+b-c
# print(x(5,25,10))

# def my_function(n):
#     return lambda a:a*n
# c = my_function(5)
# print(c(11))
# ====================================================== lambda function ==================


# ===================================== python array =========================================
# array=["mango","apple","cherry","apple","banana","apple","kiwi"]
# arrayOfNumber = [1,2,3,4,5,6,7,8,9]
# print(array[4])
# print(len(array))
# for x in array:
#     print(x)
# array.append("tomato")
# print(array)
# array.remove("tomato")
# array.pop(2)
# print(array)
# array.clear()
# print(array)
# array2 = array.copy()
# print(array2)
# print(array2.count("apple"))

# array.extend(array2)
# print(array)

# ========================== extend =================================
# array.extend(arrayOfNumber)
# print(array)
# ========================== extend =================================

# ======================== index ==================================
# print(array.index("apple"))
# ======================== index ==================================

# array.insert(2,"tomato")
# print(array)
# ===================================== python array =========================================

# array.reverse()
# print(array)

# # array.sort()
# # print(array)
# # =============================================== FUNCTION ==============================================================


# # create class

# class mycls:
#     x=5

# p1=(mycls)
# print(p1.x)


# class secondclass:
#     x=15

# p2=(secondclass)
# print(p2.x)


# class person:
#     def __init__(self,name,age) -> None:
#         self.name=name
#         self.age=age
# p3=person("adil",17)
# print(p3.name)


# class student:
#     def __init__(self,name,age,standard):
#         self.name=name
#         self.age=age
#         self.standard=standard
        
#     def myfunction(self):
#         print("hello my name is "+self.name +'\n'+ "iam age is", self.age ,'\n'+ "iam studying ", self.standard)

# p4=student("adil",17,"+2")
# p4.age=56              # to update
# del p4.age             # to delete
# del p4                 # to delete object
# p4.myfunction()


# class phone:
#     def __init__(self,brand,model,ram):
#         self.brand = brand
#         self.model = model
#         self.ram = ram

            
#     def call(self):
#         print("calling.....")
#     def message(self):
#         print("messaging......")
        
# ph=phone("Redmi","mi 8pro", "8")
# ph.call()
# ph.message()





# ==================================== class ================================ 

# class Student:
#     def __init__(self,mark1,mark2,mark3):
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3

#     def function(self):
#         x=self.mark1+self.mark2+self.mark3
#         print(x/3)
#         print(x)
        
# p1 = Student(36,98,52)
# p1.function()


# =================================== single inheritance ================================================

# class Person:
#     def __init__(adil,firstName, lastName) :      # we can also replace self with any keyword
#         adil.firstName = firstName
#         adil.lastName = lastName
    
#     def myfunction(adil) :
#         print(adil.firstName, adil.lastName)
#     def function2(adil):
#         print(5+5564545454)
# class child(Person):
#     def function3(adil):
#         print(adil.firstName)
        
 
# p8 = child("Adil","shabab")
# p8.myfunction()
# p8.function2()
# p8.function3()




# class Teacher:
#     def __init__(self,student1,student2):
#         self.student1= student1
#         self.student2= student2
    
#     def function(self):
#         print("hello world")

#     def myfunction(self): 
#         print("my students are", self.student1, self.student2)

# class Student(Teacher):
#     pass


# p9 = Student("ajith", "amal")
# p9.function()
# p9.myfunction()




# ================================= multiple inheritance ==============================

# class Student1:
#     def __init__(self,firstName,lastName,age,mark,skill):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.age = age
#         self.mark = mark
#         self.skill = skill

#     def function(self) :
#         print("Hai I am ",self.firstName, self.lastName, "and I am ", self.age, " years old")
        
# class Student2:
    
#     def function2(self):
#         print("my mark is ", self.mark, "my skill is ", self.skill)
        
    
# class Child(Student1,Student2):
#     pass


# p10 = Child("Adil","shabab",17,100,'web')
# p10.function()
# p10.function2()


# =============================== multi level inheritance ============================= 

# class GrandFather:
#     def __init__(self,name,initial):
#         self.name = name
#         self.initial = initial
        
#     def function(self):
#         print(self.name,self.initial)

# class Father(GrandFather):
#     def function2 (self):
#         print("My grandfather name is "+ self.name)

# class Child (Father):
#     pass


# p11 = Child("Adil", "MH")
# p11.function()
# p11.function2()




# ================================ Hierarchical inheritance ==================

# class Animal:
#     def __init__(self,leg):
#         self.leg = leg
        
# class Dog(Animal):
#     def function(self):
#         print("dog has ", self.leg, "legs")
        
# class Cat(Animal):
#     def myfunction(self):
#         print("cat has ", self.leg, "legs")
        
# class Hen(Animal):
#     def function2(self):
#         print("hen has ", self.leg, "legs")
        
        
# p1 = Dog(4)
# p2 = Cat(4)
# p3 = Hen(2)

# p1.function()
# p2.myfunction()
# p3.function2()



# ==================================== Encapsulation =========================== 



# ============================= public member ===================================== 
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
        
#     def show(self):
#         print("name =", self.name, "salary = ", self.salary)
        
# em = Employee("Adil",1500000000000000)
# em.show()


# ================================ Private member ================================== 
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.__salary = salary
        
    

        
# em = Employee("Adil",1500000000000000)
# print("salary = ", em.__salary)


# =================== accessing private member ==========================
        
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.__salary = salary
        
#     def show(self):
#         print("name =", self.name, "salary = ", self.__salary)
        
# em = Employee("Adil",1500000000000000)
# em.show()


# =========================== protected class ================================ 

# class Company:
#     def __init__(self,project):
#         self._project = project
        
# class Employee(Company):
#     def show(self):
#         print(self._project)

# p1 = Employee("Demo Project")
# p1.show()


# ========================= polymorphism =============================== 

# def add(x,y,z=0):
#     return x +y +z
# print(add(5,10))
# print(add(25,50,20))


# class India: 
#     def capital(self,capital):
#         self.capital = capital
#         print(capital)

#     def language(self,language):
#         self.language = language
#         print(language)

# p10 = India()
# p10.capital('Delhi')
# p10.language('English')


# ===================== module ============================== 
# import module
# module.myfunction('adil')
        
# import secondmodule as module2
# module2.function1(17)


# ==================  building function (module) =========== 

# import platform
# print(platform.system())
# print(dir(platform))


# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.now().year)              # year 
# print(datetime.datetime.now().strftime('%a'))    # short form week-day
# print(datetime.datetime.now().strftime('%A'))    # full form week-day
# print(datetime.datetime.now().strftime('%w'))    # week-day of the number
# print(datetime.datetime.now().strftime('%d'))    # day of the month
# print(datetime.datetime.now().strftime('%b'))    # short form name of month
# print(datetime.datetime.now().strftime('%B'))    # full form name of month
# print(datetime.datetime.now().strftime('%m'))    # month as number
# print(datetime.datetime.now().strftime('%y'))    # short form year
# print(datetime.datetime.now().strftime('%Y'))    # full form year
# print(datetime.datetime.now().strftime('%H'))    # to get hour
# print(datetime.datetime.now().strftime('%p'))    # to get AM or PM
# print(datetime.datetime.now().strftime('%S'))    # to get second
# print(datetime.datetime.now().strftime('%M'))    # to get minute
# print(datetime.datetime.now().strftime('%c'))    # to get local time
# print(datetime.datetime.now().strftime('%C'))    # to get century

# ================ min and max ======================
# print(min(15,58,56,45,85,100))
# print(max(15,58,56,45,85,100))

# =========== abs ================== 
# print(abs(-25))    # return positive value and only pass one argument


# ====================== power =====================
# print(pow(2,3))

# import math function module 
# import math
# print(math.sqrt(64))  # to get square root
# print(math.ceil(1.4)) # to round (to upward)
# print(math.floor(1.56)) # to avoid decimal
# print(math.pi)




# ========================== file handling ==========================

# demo_text = open('demo.txt')
# print(demo_text.read())

# # external file 
# text = open("../note.txt", 'a')
# print(text.read())

# # write
# print(text.readline(10))
# text.write(" \n this line is added by file handling")
# text.close()
# text = open('../note.txt')
# print(text.read())


# # create a new file 
# my_text = open('mytext.py','x')
# my_text = open('mytext.py','w')
# my_text.write("# this line is added from index.py")
# print(my_text.read())



# # delete 
# import os
# os.remove('mytext.py')




# *************************************************************************************************

# import random

# x = int(input('Enter Two Number'))
# y = int(input())

# x=1
# y=11
# result = random.randint(x,y)
# print(result)

# **********************************************************

# h = 'Head'
# t = 'Tail'

# coin_side = random.choice([h,t])
# print(coin_side)


# ***************************** shuffle ****************************************

# x = list(range(1,16))
# random.shuffle(x)
# print(f'shuffled list is:  {x}')

# ****************************************************************
