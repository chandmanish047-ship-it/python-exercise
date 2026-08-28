name=input("enter the name:")
print(f"hello,{name}!")

'''radius=int(input("enter the radius of the circle:"))
area=3.14*radius**2
print("the area of circle is=",float(area))'''

'''length=int(input("enter the length:"))
breadth=int(input("enter the breadth:"))
perimeter=2*(length+breadth)
area=(length*breadth)
print("perimeter of the rectangle=",perimeter)
print("area of the rectangle=",area)'''

'''num1=int(input("enter the number-1:"))
num2=int(input("enter the number-2:"))
num3=int(input("enter the number-3:"))
sum=(num1+num2+num3)
product=(num1*num2*num3)
avg=sum/3
print("sum=",sum)
print("product=",product)
print("avg=",avg)'''

'''talents=int(input("enter the mass in talents:"))
pounds=int(input("enter the mass in pounds:"))
lots=float(input("enter the mass in lots:"))
gram=(talents*20*32*13.3)+(pounds*32*13.3)+(lots*13.3)
kilogram=gram/1000
print("weight is kilogram",kilogram)'''
def sum(n):
    if(n==1):
        return 1
    else:
        return sum(n-1)+n
print(sum(100))