# # print("enter a value")
# # a=int(input())
# # print(" enter b value")
# # b=int(input())
# # print("enter c value")
# # c=int(input())
# # if(a>b)and
#
#
#
# ##FACTORIAL PROGRAM
# n=int(input("Enter:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
#


#
# ##to find the length of a string
# # var1=(input("enter a string:"))
# # num=0
# # for s in var1:
# #     num=num+1
# # print("the length of a string is:",num)
# ## count in a string
# list1=["hi","hello","hi","hello","bye"]
# def add(a,b,c):
#     print(a+b)
#     print(b+a)
#     print(c+a)
#     return (a,b,c)
# add(10,20,33)
# #square of a num
# def sq():
#     for i in range(1,11):
#         val=i**2
#         print(val)
# sq()
##postional arguments
# def cal(x,y):
#     c=10
#     d=45
#     mudiv=c%d
#     sum=x+y
#     return(mudiv,sum)
# print(cal(5,5))
# def emp(a,b):
#     empname=a
#     empid=b
#     print("employee name is:",empname)
#     print("employee id is:",empid)
#     return(emp)
# emp(10,20)
##program to convert clesius to franheit
# t=float(input())
# if t<1000:
#     fren=(1.8*t)+32
#     print(int(fren))
## printing the output values for three times
# a=int(input())
# var=str(input())
# counter=0
# for i in var:
#     counter=i*3
#     print(counter, end='')
## ####
# N=int(input())
# Array=list(map(int, input(),sep=','[:N]))
# print(Array)

# array=list(map(int,input().split()))
# list=["mango","banana","mango","good","bad","good","bad","good","bad"]
# for i in list:
#     print(i)

#
# inp,res=input().split(),0
# for i in inp: res+=int(i)
# max = int(max(inp))
# print(int(res%max))

# ###checking a string whether oval are present or not
# vowel={"a","e","i","o","u"}
# str=set(input("enter a string:\n"))
# will=vowel&str
# for i in will:
#COUNT OF EVEN OR ODD
c=0
c1=0
inp=int(input("enter the number"))
for i in range(0,inp):
    if i%2==0:
        c+=1
        print ("the even numbers are:",i)
    else:
        c1+=1
        print ("the odd numbers are:",i)

print("no of even number present in the range","0",inp,":",c)
print("no of odd number present in the range","0",inp,":",c1)







