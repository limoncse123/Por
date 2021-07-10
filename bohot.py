p= int(input("enter the number: "))
for i in range(0,p):
    for j in range(0,p-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("0",end="")
    print("")