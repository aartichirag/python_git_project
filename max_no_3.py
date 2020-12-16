print("\t\t maximum no program ")
no1=int(input("enter no1:"))
no2=int(input("enter no2:"))
no3=int(input("Enter no3:"))
print("output :\n")
if no1>0 and no2>0 and no3>0:
    if no1>no2 and no1>no3:
        print(no1," is a maximum no")
    elif no2>no3 :
        print(no2," is a maximum no")
    else :
        print(no3," is a maximum no")
else:
    print("nagetive no are not allowed.")
