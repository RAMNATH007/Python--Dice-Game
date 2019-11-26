z=30
# class testname:
#     a=50
#     b=60
#     def sum(self):
#         global z
#         c=self.a+self.b+z
#         print(c)
# c=testname()
# print(z)
# print(c.sum())
# 2
# class student:
#     def __init__(self):
#         self.name="Akash"
#         self.age=23
#         self.marks=80
#
#     def  talk(self):
#         print('hello myself:',self.name)
#         print("my age is",self.age)
#         print("my marks is",self.marks)
# s=student()
# s.talk()
#3
# class student:
#     def __init__(self,name,age,marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#
#
#     def talk(self):
#         print('hello myself:', self.name)
#         print("my age is", self.age)
#         print("my marks is", self.marks)
# s1=student("akash",80,100)
# s1.talk()
# #4
# class test():
#     print("good morning")
# test()
# #5
# class test:
#     def __int__(self):
#         print(10,20)
# t=test()
# t1=test()
#6
# class Employee:
#     def __init__(self,x,y,z):
#         self.ename=x
#         self.eage=y
#         self.eaddress=z
#     def info(self,helo):
#         if helo:
#         print("ename:",self.ename)
#         print("eage:",self.eage)
#         print("eadress:",self.eaddress)
# e1=Employee("Akash",22,"Banglore")
# e2=Employee("Priya",23,"chennai")
# e1.info()
# e2.info()
#7
# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#     def m1(self):
#         self.d=40
#     def m2(self):
#         self.e=50
# t=test()
# print(t.__dict__)
#  8
# class student:
#     def __init__(self,x,y):
#         self.name=x
#         self.id=y
#     def info(self):
#         self.marks=60
# s=student("xyz",11)
# s.info()
# s.y1=21
# print(s.__dict__)
# print(s)
# deleting a variable
# class student:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#     def delete(self):
#             del self.a
#             del self.b
# s=student()
# s.delete()
# print(s.__dict__)

