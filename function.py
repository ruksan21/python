# #function in python 
# #function with no parameters and no return value
# def greet():
#     print("hello world from function.py")

# #function with parameters and no return value
# def sum(num1, num2):
#     add= num1 + num2
#     print("The sum is:", add)
    
    
# a=10
# b=20
# sum(a, b)
    
    
#function with parameters and return value
def fact(num):
    if num ==0:
        return 1
    else:
        result = 1
        #for loop to find factorial
        for i in range(1, num + 1):
            result *= i
    return result
num = int(input("Enter a number to find factorial: "))
result = fact(num)
print("The factorial of", num, "is", result)
#function with no parameters and return value


