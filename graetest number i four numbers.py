num1=int(input("num1 = "))
num2=int(input("num2 = "))
num3=int(input("num3 = "))
num4=int(input("num4 = "))
if(num1>num2 and num1>num3 and num1>num4):
    print("num1 is a greatest number in these four number")
elif(num2>num1 and num2>num3 and num2>num4):
    print("Num2 is a graetest number in the four numbers")  
elif(num3>num1 and num3>num2 and num3>num4):
    print("Num4 is a greatest number in these four numbers")
elif(num3==num1 and num3==num2 and num3==num4 and num4==num1):
    print("Ghaffar is bad boy.")    
else:
    print("num4 is a greatest number in these four numbers ")          
