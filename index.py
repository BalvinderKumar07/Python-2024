# 2/09/2024
# print("hello Word") 

#03/09/2024
# print("hello World") 

# print( 10 if 20)


# x = 20
# X = 30

# student_name = 'rahul' "57658765" '865765865'

# _a = 34
# a_ = 45
# _name_ = 65

# print(student_name)
# print(X)

# ytujhhhhhhhhhhhhhhhhhg

# uiddddddddddddddddd

# dufdsuhf
# sdfsuddddddddddddddddd

# =====================04/09/2024==============

# fname = "rahul"
# lname = "kumar"
# address = """123, main road
# near bus stand
# kolkata
# """

# x = 54675 
# z = 10 #int
# a = 10.6 #float

# # h = 6787643873632876e #long

# g = 2.14j  #complex

# y = None #10mb

# print(fname + lname )
# print(address)

# print(type(fname))
# 

# =====================05/09/2024==============

# x = 30 
# y = 31

# print(x - y)
# print(x != y)

# a = 10
# a = a + 1 

# y = 3 + 6 % 7 * (7 + 10) # 17
# y = y -  3 # 
# print( a + y) # 11 + 6 = 14

# =====================07/09/2024==============


# x  = 30
# y = 20

# print((x>20) & (x>21)) and
# print((x>35) | (x>50)) or
# print(not(x>35)) not

# =====================09/09/2024==============


# x = 10 # 1 0 1 0
# y = 12 # 1 1 0 0
#        1 1 1 0
        #

# print(x & y)
# print(x | y)
# print(x ^ y)


# print(~10)  # 1 0 1 0 = 0 1 0 1


# =====================12/09/2024==============


# print("hello") #010101110010101 1 = on 0 = off
#                    0      0     0   0   1
# x = 13 #128  64   32 16  8   4  2  1
# y = 23               #        10111 = 01101 =    0101  11111

# print( x & y ) 
# print( x | y ) 
# print( x ^ y ) 
# print(not(x)) 

# Name1 = ["a","b","c","d"]
# Name2 = ["a","b","e","d"]
# Name3 = Name1

# print("c" in Name)
# print("c" not in Name)

# print(Name1 is Name3)
# print(Name3 is Name2)

# ==================IS NOT 

# print(Name3 is not Name1)
# print(Name3 is not Name2)


# =====================13/09/2024==============

# x = 136
# y = 89 

# a = 186
# b = 365
# c = 203

#and or xor not

# =====================14/09/2024==============

# print("hello")

# user = 91

# if((91<= user) & (100>=user)):
#         print("A+")
# elif((81<= user) & (90>=user)):
#         print("B")
# elif((71<= user) & (80>=user)):
#         print("C")
# elif((55<= user) & (70>=user)):
#         print("D")
# elif((33<= user) & (54>=user)):
#         print("E")
# else:
#     print("Fail")   

# if(user >= 33):
#     print("Pass")
# else:
#     print("Fail")    


# =====================16/09/2024==============

# a = int(input("Enter A Number: "))

# if(a%2==0):
#     print("Even")
# else:
#     print("Odd")   


# =====================17/09/2024==============


# h = float(input("Enter A Number : ")) # 6.8 6767.9

# if(h%2==0):
#     print("Even")
# else:
#     print("Odd")

# print(h)

# x = 0
# while x < 10: 
#     print(x)
#     x = x + 1
# print(x)

# =====================18/09/2024==============

# table = int(input("Enter a Number : "))

# x = 1
# while x <= 10: 
#     print(x * table)
#     x = x + 1


# =====================20/09/2024==============

# i = 1
# x = 1
# num = int(input("Enter A number : ")) 

# while i <= num:
#     x = x * i # 1x1 = 1x2 = 2x3 = 6x4 = 24x5 = 120
#     i = i + 1 # 1,2,3,4,5
#     print(x) 
# 
# =====================21/09/2024==============   

# print("Practice Session For The all Programs Chapter No. 4")

# =====================23/09/2024==============

# year = int(input("Enter your year : "))

# if((year%400==0) and (year%100==0)):
#     print(year, "Is Leap year")
# elif(year%4==0):
#    print(year, "Is Leap year") 
# else:
#     print(year, "Is Not Leap year") 


# num = int(input("Enter a Number : ")) # 10

# x = 1
# while x <= 10: #3 <= 10
#     j = 1
#     while( j <= num): # 2 <= 5
#         print(j * x, end=" " ) # 2 X 1 = 2
#         j = j + 1 # 2
#     print()     
#     x = x + 1 

# =====================24/09/2024==============

# x = 11

# while x<=10:
#     print(x)
#     x = x + 1
# else:
#     print("loop is end") 

# name = "PYTHON" # p y t

# for x in name:
#     print(x)

# mylist = ("rahul","aman","pardeep","sonu")

# for f in mylist:
#     print(f)

# for x in range(-100,2,5):
#     print(x)


num = int(input("Enter A Number : ")) # 5
j = 1
while j <= num: # 2 <= 5
    for i in range(1,11): # 2
        print(i * j , end=" ") # 2 x 1 = 2 2 x 2 = 4 3 x 1 = 3 10
    print()
    j = j + 1
