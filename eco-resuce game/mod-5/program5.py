username=input("enter the username:")
password=input("enter the password:")
attempts=0
while(username!="python"and password!="rules"):
    print("invalid username and password:")
    username=input("enter again:")
    password=input("enter again:")
    attempts+=1
    if(attempts==5):
        print("access denied:")
        break
else:
    print("access granted:")