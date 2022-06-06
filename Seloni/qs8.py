print("Enter a string")
str=input()
sum=0
for i in str:
    if(ord(i)>=48 and ord(i)<=57):
        sum=sum+int(i)
print("sum is",sum)  
