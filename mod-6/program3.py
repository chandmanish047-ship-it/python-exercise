num=int(input("enter the number:"))
factors=0
for i in range(1,num+1):
        if(num%i==0):
         factors=factors+1
if(factors==2):
    print("it's prime:")
else:
    print("it's composite:")