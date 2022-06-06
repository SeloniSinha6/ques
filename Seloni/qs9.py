print("enter a string")
str=input()
list=[]
for i in str:
    list.append(i)
list.sort()
str=''.join(list)
print(str)