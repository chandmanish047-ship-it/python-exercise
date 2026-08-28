year=int(input("enter the year:"))
if(year%100!=0 and year%4==0 or year%400==0):
    print("It's a leap year:")
else:
    print("It's not a leap year:")