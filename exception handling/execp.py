# handling type error
# try:
#     a=5
#     b="o"
#     print(a+b)
# except TypeError:
#     print("Enter the value in integer format")
# finally:
#     print("try again")
## handling the index error
# try:
#     l=[1,2,3,4,5]
#     print(l[8])
# except IndexError:
#     print("Enter the value with in the range")
# finally:
#     print("Try again")
# try:
#     print "hello world"
# except SyntaxError:
#     print("Check the syntax")
# try:
#     a=5
#     b=0
#     c=(a/b)
#     print(c)
# except ZeroDivisionError:
#     print("enter the value above 0")
# handling the file error
# try:
#     f=open("../new/","r")
# except  IOError:
#     print("the file doesnt exist")
# else:
#     print("the file exist")
#
#multiple exception
# try:
#  a=5
#  b=0
#  print(a/b)
# except ZeroDivisionError:
#     print("division is not allowed with 0")
# except TypeError:
#     print("the entered data has to be in int")
#handling by using as
# try:
#     x=int(input("Enter the first number:"))
#     y=int(input("Enter the second number:"))
#     print(x/y)
# except(ZeroDivisionError,ValueError)as hh:
#     print("plz provide valid number only and problem is:",hh)
####
try:
    x=int(input("Enter the first number:"))
    y=int(input("Enter the second number:"))
    print(x/y)
except ZeroDivisionError:
    print("can't divide with Zero")
except ValueError:
    print("please provide int value only")



