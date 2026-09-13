def price(diameter_cm,euro_price):
    radius=(diameter_cm/2)/100
    area=3.14*radius*radius
    price_per_sqm=euro_price/area
    return price_per_sqm
diameter1=float(input("enter the diameter of pizza-1 in cm:"))
euro1=float(input("enter the price of pizza-1 in euro:"))
diameter2=float(input("enter the diameter of pizza-2 in cm:"))
euro2=float(input("enter the price of pizza-2 in euro:"))
price1=price(diameter1,euro1)
price2=price(diameter2,euro2)
if price1<price2:
    print("pizza-1 is better:")
elif price2<price1:
    print("pizza-2 is better:")
else:
    print("both are same:")