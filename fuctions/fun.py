# def test(*a):
#     for i in a:
#       print(i)
# test(10,50,60,89)
# def sum(*a):
#  temp=0
#  for x in a:
#     temp=temp+x
#     print(temp)
# sum(10,10)
# sum(14,45)
# def sum(*a):
#  temp=1
#  for x in a:
#     temp=temp*x
#     print(temp)
# sum(int(input()))
# #
# def test(*a,**b):
# #     print(a,b)
# # test (10,b=20)
#
# a=1
# if a==1:
#     name()
# def name():
#     print("the name is mango")
list1 = ["sid","sid","Good","Bad","Good","Bad","google","Bad","Good","Good","sid","sid","crab","google"]
dict1 = {}
i = 0
while list1:
    val = list1[0]
    count = list1.count(val)
    temp = {count:val}
    dict1.update(temp)
    while val in list1: list1.remove(val)
    i+=1
print(dict1)
n=input("enter a string:")
counter=0
while n !=None:
    counter=n[0]
    print(counter)











