# #compile()
import re
# x = re.compile('python')
# print(type(x))

#findier()
# import re
# x=re.finditer('[abc]',"a58ub")
# for match in x:
#     print(match.start())
# import re
# x=re.finditer('[^abc]',"a58ub")
# for match in x:
#     print(match.start())
# import re
# x=re.finditer('[a-z]',"a58ub")
# for match in x:
#     print(match.start())
# import re
# x=re.finditer('[A-Z]',"a58ub")
# for match in x:
#     print(match.start())
# import re
# x=re.finditer('[A-Z-a-z]',"a58ub")
# for match in x:
#     print(match.start())
# import re
# x=re.finditer('[0-9]',"a58ub")
# for match in x:
#     print(match.start())
# import re
# x=re.finditer('[A-Z-a-z-0-9]',"a58ub")
# for match in x:
#     print(match.start())
# import re
# x=re.finditer('[^A-Z-a-z-0-9]',"a5@8ub")
# for match in x:
#     print(match.start())
### special charcters
#s for finding space
# matches=re.finditer("\s",'abc ABC @ 4588 A k 0')
# for i in matches:
#     print(i.start())
#S  expect the space
# matches=re.finditer("\S",'abc ABC @ 4588 A k 0')
# for i in matches:
#     print(i.start())
#d for finding the digits
# matches=re.finditer("\d",'abc ABC @ 4588 A k 0')
# for i in matches:
#     print(i.start(),"....",i.group())
#D
# matches=re.finditer("\D",'abc ABC @ 4588 A k 0')
# for i in matches:
#     print(i.start(),"=",i.group)
#w
# matches=re.finditer("\w",'abc ABC @ 4588 A k 0')
# for i in matches:
#     print(i.start(),"=",i.group())
#W
# matches=re.finditer("\W",'abc ABC @ 4588 A k 0')
# for i in matches:
#     print(i.start(),"=",i.group())
# (.) for all charcters
# matches=re.finditer(".",'abc ABC @ 4588 A k 0')
# for i in matches:
#     print(i.start(),"=",i.group())
#### quantifiers
#a
# matches=re.finditer("a",'abc ABC @ 4588 A k 0')
# for i in matches:
#     print(i.start(),"=",i.group())
#a+
# matches=re.finditer("a+",'abc ABC @ 4588 A k 0')
# for i in matches:
#     print(i.start(),"=",i.group())
#a*
# matches=re.finditer("[a*]",'aabc ABC @ 4588 A k 0')
# for i in matches:
#     print(i.start(),"=",i.group())
#a?
matches=re.finditer("[a?]",'abc ABC @ 4588 A k 0')
for i in matches:
    print(i.start(),"=",i.group())







