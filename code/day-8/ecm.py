
num1=int(input("enter first no"))
num2=int(input("enter second no"))
num3=int(input("enter third no"))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number between",num1,",",num2,"and",num3," largest is",largest)
