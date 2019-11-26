#creating a dict
# dict1={"flow":"rose","num":45}
# print(dict1)

#accessing a dict
# print(dict1["flow"])

# #deleting a dict
# del(dict1)
# print(dict1)

#length of dict
# print(len(dict1))

#to display the values in a dict
# print(dict1.values())

#to display the keys in a dict
# print(dict1.keys())

#to display the item in a dict
# print(dict1.items())

#update the dict
# dict2={"hello world":"python","num2":458}
# dict1.update(dict2)
# print(dict1)

#clear  ## this methods is used to clear the values in a dict
# dict2.clear()
# print(dict2)

#copy()  copying a dict
# dict3=dict1.copy()
# print(dict3)

dict1={"red":"color","flowers":"rose",92:"number"}
a={'red':'color'}
if(dict1['red']):
    del(dict1)
else:
    print("not applicable")
print(dict1)


