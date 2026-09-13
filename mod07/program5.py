def list_number(number):
    even=[]
    for i in number:
        if i%2==0:
            even.append(i)
    return even
number1=[1,2,3,4,5,6,7,8,9,10]
new_list=list_number(number1)
print("original list is:",number1)
print("even number list is:",new_list)