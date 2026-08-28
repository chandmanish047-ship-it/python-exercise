
gender=input("enter the gender:")
heamoglobin=int(input("enter the heamoglobin:"))
if(gender=="Male"):
    if(heamoglobin<134):
        print("low heamoglobin in male:")
    elif(heamoglobin>167):
        print("high heamoglobin in male:")
    else:
        print("normal heamoglobin in male:")
if(gender=="Female"):
    if(heamoglobin<117):
        print("Low heamoglobin in female:")
    elif(heamoglobin>167):
        print("High heamoglobin in female:")
    else:
        print("Normal heamoglobin in female:")