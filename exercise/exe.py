#reverse of a string
# str=input("enter a string to reverse:")
# a=len(str)
# for i in reversed(str):
#     print(i)
#slicing a string
# s=input("enter a string:")
# print(s[2:5])
#finding the maxium length of a string
# s1,s2=input("string 1:"),input("string2:")
# a,b=len(s1),len(s2)
# if (a>b)&(a!=b):
#     print(s1,"is the biggest string and the length is:",a)
# elif(b>a)&(b!=a):
#     print(s2,"is the biggest string and the length is:",b)
# else:
#     print("Both string1 and string are equal in length")
#Boolean expression
# 1
# a=True and not False
# print(a)
# 2
# b= True and not false
# print(b)
# 3
# c= True or True and False
# print(c)
# 4
# d= not True or not False
# print(d)
# e = True and not 0
# print(e)
# f =52.3 < 52
# print(f)
# 7
# g = 1+52<52.3
# print(g)
# 8
# print(4!=4.0)
# Boolean expressions :
#1
# a,b=4,4
# print(a==b)
# 2
# Operations on a list
#multiplying a list
# lis1=[1,2,3,4,5,6,7,8,9]
# count=1
# for i in lis1:
#     a=i*count
#     count=a
#     print(a)
# num=int(input("Enter the number your want to find the divisiblity:"))
# b=[]
# for i in range(1,100):
#     if (i%num==0):
#         print("These are numbers divisiblity:",i)
# a=[5445,5646,8,8,9,5,6,7,5,8,88,888,44,5,5,65,1,4,5]
# # b=[4,5,8,4,2,5,8,5,56,5,8,8,8,4,5,5,]
# print(max(a))
# print(min(a))

# dicts={"India":"IN","united states of america":"USA","china":"chn","srilanka":"sl"}
# print(dicts.values())
# print(dicts.keys())

# import os
# f=open("abc.txt","w")
# f.write("Take it easy")
# f.close()
# f=open("abc.txt","r")
# x=f.read()
# print(x)
# f.close()
# class traingle:
#     def __init__(self,angle1,angle2,angle3):
#         self.angle1=angle1
#         self.angle2=angle2
#         self.angle3=angle3
#         number_of_sides=3
#     def check_angles(self):
#         if self.angle1+self.angle2+self.angle3==180:
#             print(True)
# a=[[1,2],[3,4],[5,6]]
# b=[]
# c=[]
# for i in a:
#     c.append(i[0])
#     b.append(i[1])
# print(b)
# print(c)
# print(a[0][0]
# dict1={"ram":80,"raj":"shop","rock":90,"fly":"high"}
# b=  dict([(value, key)for key,value in dict1.items()])
# print(b)
# Adding a list
# lis1=[1,2,3,"hello"]
# lis2=["good","bad","sing"]
# lis3=["morning","afte"]
# for i in lis2:
#     lis1.append(i)
# print(lis1)
# for j in lis3:
# #     lis1.append(j)
# lis1.extend(lis2)
# lis1.extend(lis3)
# print(lis1)
x1=int(input('enter the factor'))
def add(a,b):
    return a+b
def sub(c,d):
    return c-d
def mul(e,f):
    return e*f
def div(g,h):
    f=float(g)/float(h)
    return float(f)
def ADD(A,B,C):
    return A+B+C
def SUB(D,E,F):
    return D-E-F
def MUL(G,H,I):
    return G*H*I
def DIV(J,K,L):
    F=float(J)/float(K)/float(L)
    return float(F)
if(x1==2):
    p2=int(input('enter the value '))
    q2=int(input('enter the value'))
    n2=int(input('enter 1.add or 2.sub or 3.mul or 4.div'))
    if(n2==1):
         print (add(p2,q2))
    elif(n2==2):
         sub(p2,q2)
    elif(n2==3):
        mul(p2,q2)
    elif(n2==4):
        div(p2,q2)
    else:
         'Please enter the proper operation'
elif(x1==3):
    p3=int(input('enter the value'))
    q3=int(input('enter the value'))
    r3=int(input('enter the value'))
    n3=int(input('enter 1.add or 2.sub or 3.mul or 4.div'))
    if(n3==1):
        print (ADD(p3,q3,r3))
    elif(n3==2):
        print (SUB(p3,q3,r3))
    elif(n3==3):
        print (MUL(p3,q3,r3))
    elif(n3==4):
        print (DIV(p3,q3,r3))
    else:
        print ('Please enter the proper operation')
else:
    print('enter the proper factor')
