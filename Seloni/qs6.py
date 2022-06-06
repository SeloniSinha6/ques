print("Enter the lower limit ")
lowerlim=int(input())
print("Enter the upper limit")
upperlim=int(input())
f=0
list=[]
for i in range(lowerlim,upperlim+1):
    for j in range(2,i):
        if (i%j==0):
         f=1
    if(f==0):
        list.append(i)
    f=0
print("The prime numbers in the range are ",list)