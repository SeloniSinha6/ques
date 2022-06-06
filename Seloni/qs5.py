list=[56]
for i in range(1,100):
    list.append(i)


for i in list :
    cou=list.count(i)
    if(cou==2):
        print("duplicate no. is ", i)
        list.remove(i)
