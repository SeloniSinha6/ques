print("Enter the length of the list")
l=int(input())
list=[]
for i in range(0,l):
    print("enter the value")
    a =int(input())
    list.append(a)

print("enter the order")
order=input()
if(order=="asc"):
    list.sort()
    print("the new list",list)
if(order=="desc"):
    list.sort()
    list.reverse()
    print("the new list",list)
if(order=="none"):
     print("the list",list)