season=("spring","summer","autumun","winter")
month=int(input("enter the month number:"))
if month in[1,2,3]:
    print("the season is:",season[0])
elif month in[4,5,6]:
    print("the season is:",season[1])
elif month in[7,8,9]:
    print("the season is:",season[2])
elif month in[10,11,12]:
    print("the season is:",season[3])
else:
    print("invalid month number:")