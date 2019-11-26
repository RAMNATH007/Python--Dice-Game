var,lis=input("enter the value:"),[]
for i in var:
    lis.append(i)
print(lis)
###
var,a=input("enter the value"),[]
c=[i for i in var]
a.append(c)
print(a)
###
var=[]
y=[1,56,8,4,5]
var=[i for i in y if(i%2==0)]
print(var)
###
lis=[]
for i in range(100):
    if (i%2==0)and(i%3==0):
        lis.append(i)
        print(lis)
var=[i for i in range(100) if(i%2==0)and(i%3==0)]
print(var)
###
y=[10,20,30]
var=[i if(i%2==0) else "odd" for i in y]
print(var)
val=0
for i in range(1,100):
    if (i%3==0)and(i%5==0):
        val+=i
    print(val)
val=[]
for i in range(6, 0,-1):
    val.append(i ** 2)
print(val)
val=[i **2 for i in range(6, 0, -1)]
print(val)
### set comprehansion
var={10,30,45,45}
even=set()
odd=set()
for i in var:
    if(i%2==0):
        even.add(i)
    else:
        odd.add(i)
print(even)
print(odd)


v={10,20,30,40,5}
s={i for i in v if i%2==0}
print("even numbers are:",s)
####
a=set()
for i in {2,3,4,5}:
    for x in {2,3,4,5}:
        l=(i+x)
        a.add(l)
print(a)
a={i+x for i in{2,3,4,5} for x in {2,3,4,5}}
print(a)
### dictonary comprehension
list1=[1,23,4,5]
b={}
for i in list1:
    if (i%2==0):
     b[i]=i**3
print(b)
b={i:i**3 for i in list1  if (i%2==0)}
print(b)
a=[1,2,3]
b=[3,4,5]
c=[]
c+=[a]+[b]
print(c)
print(c[0][1])

# for k,v in zip(list1,b):
#     c[k]=v
# print(c)
# c={k:v for k,v in zip(list1,b)}
# print(c)



