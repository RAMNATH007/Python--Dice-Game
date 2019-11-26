# #multiple variables to multiple values
# a,b,c=10,20,"rock"
# print(a,b,c)
# #multiple variable to single value
# a=b=c="jack"
# print(a,b,c)

# set1={4,5,8,7,96,4,8,8,4,8,75,6,5,8}
# print(set1)
# tuple1=(4,5,8,78,9,45,6,5,8,4,5)
# print(tuple1)
# a="5"
# b="10"
# c=a+b
# print(c)
# Three sides of the triangle is a, b and c:
##### Traingle Program
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))
#
# # calculate the semi-perimeter
# s = (a + b + c) / 2
#
# # calculate the area
# area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# print('The area of the triangle is %0.2f' % area)
# import random
# calculating the miles from kilo meters
# class Swapping:
#     def __init__(self,miles):
#         self.miles=miles
#     def cal(self):
#         # print("ID: %d \nName: %s" % (self.id, self.name))
#         kilometers=self.miles*1.6
#         print(kilometers)
# s=Swapping(100)
# s2=Swapping(110)
# s.cal()
# s2.cal()
# display a calendar
# import calendar
# cal=calendar.prcal(2057)
# print(cal)
#program to display negative or postive or zero program
# N = int(input("Enter any number: "))
# while (N):
#     Num=int(input("Enter the number: "))
#     if (Num%2==0 and Num!=0):
#         print("%d is a postive Number:"%(Num))
#     elif (Num%2!=0):
#         print("%d is a Negative Number:"%(Num))
#     else:
#
# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print( i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")
#
# else:
#     print(num, "is not a prime number")
# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))
#
# for num in range(lower, upper + 1):
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         print(digit)
#         temp //= 10
#         if num == sum:
#             print(num)
num = int(input("Enter a number: "))
sum = 0
temp = num
#
while temp > 0:
    digit = temp % 10
    sum +=digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
# num=int(input("Enter a number:"))
# # c=0
# # for i in num:
# num //=10
# print(num)
# print(sum)
