a=int(input("enter 1st quadrant value"))
b=int(input("enter 2nd quadrant value"))

if(a>0 and b>0):
    print("it is in 1st quadrant")
elif(a<0 and b>0):
    print("it is in 2nd quadrant")
elif(a<0 and b<0):
    print("it is in Third quadrant")
elif(a>0 and b<0):
    print("it is in 4th quadrant")
else:
    print("enter value is invalid")
