print("Enter your credit card no.")
num=input()
num=num.replace(" ","")
l=len(num)
str=num[-4:l]
for i in range(0,(l-4)):
   str="*"+str
print(str)