#conditional operator
num1 =int(input("Enter first number: "))
num2 =int(input("Enter second number: "))
num3 =int(input("Enter third number: "))
# Using conditional operator to find the largest number

if (num1 > num2 ):
    if (num1 > num3):
         print(num1, "is the greatest number")
elif (num2 > num1 and num2 > num3):
    print(num2, "is the greatest number")
else:
    print(num3, "is the greatest number",num1)


# #for odd or even
# if num1==0:
#     print(num1,  "is Zero")
# elif num1 % 2 == 0:
#     print(num1, "is even")
# else:
#     print(num1, "is odd")
    