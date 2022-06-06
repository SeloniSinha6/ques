list=[12,23,33,55,4,12,56,23,44,23]

fre=0
max=0
maxfreq=0
for i in list:
    fre=list.count(i)
    if(fre>max):
       max=fre
       maxfre=i
print("the value with max frequency is ",maxfre) 
print("with frequency",max)  