a=int(input("enter first digit"))
b=int(input("enter second digit"))
print("1 for addition")
print("2 for Multiplication")
print("3 for substraction")
print("4 for Modulus")
print("5 for Exponent")
print("6 for  division")
c=int(input("option="))
if c==1:
    print(a+b)
elif c==2:
    print(a*b)
elif  c==3:
    print(a-b)
elif  c==4:
       print(a%b)
elif c==5:
    print(a**b)
elif c==6:
    print(a/b)

else:
    print("sorry wrong Choice")
      
