# ======================= question 1 ====================================
# touple1=(2,3,4,5,(6,34,2),-2,-1)

# x= touple1[4]
# print(x[1])


# print(touple1[1:6])

# print(touple1[-2])


# =========================================== question 2 =================================================

# touple2 = (-2,2,43)
# touple3 = (8,-2,9.5,10)

# touple4 = touple2 + touple3
# print(touple4)


# ====================================== question 3 ===============================

# set1 = {"blue", "green", "red", "black",}

# for x in set1:
#     print(x) 
    
  
# print("white" in set1) 
 
# if "white" in set1:
#     print("true")
# else:
#     print("false")
    

# set1.add("yellow")
# print(set1)

# set1.clear()


# ================================== question 4 ========================= 

# dictionary1 = {
#     "Appu" : 25,
#     "Adil" : 17,
#     "Amal" : 20,
#     "Sabique" : 21
# }


# dictionary1["Aby"] = 22
# print(dictionary1)

# dictionary1.pop("Appu")
# print(dictionary1)

# print(dictionary1.get("Adil"))





# ============================== EVEN OR ODD ===================================================
# x = int(input("enter a number"))
# if x%2==0:
#     print("even")
# else:
#     print("odd")
    
    
    
    
    
# y = int(input("enter a number"))
# if y%3==0:
#     print("hello")
# elif y%2==0:
#     print("hai")
# else:
#     print("not")
    
    
    
    
# QUESTIONS 

# =============== fifth question ======================= 


# a = 50
# b = 80

# c=a 
# a=b
# b=c

# print(a)
# print(b)


# ========================== sixth question ==================
# num1 = int(input("Enter a number"))

# if num1 %2:
#     print("Entered number is even")
# else: 
#     print("Entered number is Odd")


# ================================= seventh question ======================

# principle = int(input('Enter your Principle'))
# time = int(input("Enter the time"))
# rate = int(input("Enter your rate of interest"))

# print("Simple Interest " + principle*time*rate/100)


# ========================= eighth question =========================



# array = [12,3,4,50]
# sum = 0
# for x in range(0,len(array)):
#     sum = sum + array[x]

# print(sum)


# =================== ninth question =======================

# list1 = [1,2,3,4,5,6,7,8,9,10]
# list1.reverse()
# print(list1)

# print(list1[::-1])    # another way 



# =================== tenth question =========================

# list2=[5,8,6,8,53,43,23,465]
# m= len(list2)
# print(list2[m-1])


# print(max(list2))
    

# ================ eleventh question =====================

# input1 = input("Enter your Input")

# def function1(value):
#     return value[::-1]

# if input1 == function1(input1):
#     print("Entered word is palinderom")
# else:
#     print("Entered word is not palinderom")
    
    
# another way 

# input2 = input1[::-1]

# if input1 == input2:
#     print("Entered word is palinderom")
# else:
#     print("Entered Word is not palinderom")



# ================== random number =========================
# import random
# print(random.randrange(1,50))


# ======================== format method in string ========================
# name = "Adil"
# place = "Padikkal"
# age = 17

# txt = 'my name is {} and i am from {} and i am {} years old'
# print(txt.format(name,place,age))
# name = "Adil"

                # ---------------------- #
# name = "Adil"
# place = "Padikkal"
# age = 17

# txt = 'my name is {2} and i am from {0} and i am {1} years old'
# print(txt.format(place,age,name))




# ====================== escape characters ==================
# /n    new line
# /'    single quote
# /b    backspace
# /t    tab
# //    to use backslash


# print("Adil \nshabab")
# print("Adil is a \"good\" boy")
# print("Adil \tShabab")
# print("Adil \bshabab")
# print("Adil \\ Shabab")


# ===================== string methods =========================
# capitalize()
# casefold()
# center()
# count()
# find()
# format()
# index()
# upper()
# lower()
# replace()


# =================== pattern printing ==================== 

# def pattern1(number):
#     for x in range(0,number):
#         for y in range(0, x+1):
#             print('* '*y)
            
            
# def pattern2(number):
#     for x in range(0, number):
#         for y in range(0, x+1)
# pattern1(10)
            




# =================== twelth question ============================
# import math
# def area_square(radius):
#     area = 3.14*radius*radius
#     result = float("{:.2f}".format(area))
#     print(f"area of the square is {result}" )
    
# r = int(input("Enter the radius of the circle:  "))
# area_square(r)
# =================== thirteenth question ============================

# def find_positive(x,y):
#     for x in range(x,y):
#         if x > 0:
#             print(x)
# start = int(input("Enter the first range: "))
# end = int(input("Enter teh second range: "))
# find_positive(start, end)

# =================== forteenth question ============================

# name = "Adil Shabab"
# if 'dil' in name:
    # print("yes")

# =================== fifteenth question ============================

# def find_even(x,y):
#     for x in range(x,y):
#         if x%2==0:
#             print(x)
# start = int(input("Enter the first range: "))
# end = int(input("Enter teh second range: "))
# find_even(start, end)


# =================== sixteenth question ============================


# tuple1 = ("Apple", "Mango", "Cherry", "Banana")
# tuple2 = ("tomato", "chilly", "lemon")
# tuple3 = tuple1+tuple2
# print(tuple3)


# =================== seventeenth question ============================

text = input("Enter some text: ")

def change_text(text):
    if text == text.lower():
        result = text.upper()
        print(result)
    else:
        result = text.lower()
        print(result)

change_text(text)




