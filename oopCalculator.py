class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1 
        self.num2 = num2
        
def add(self):
    sum=sum.num1 + sum.num2
    print("The sum is: ", sum)
    
def subtract(self):
    sub=self.num1 - self.num2
    print("the difference of", self.num1, "and", self.num2, "is: ", sub)
    
def multiply(self):
    mul=self.num1 * self.num2
    print("The product of", self.num1, "and", self.num2, "is: ", mul)

def div(self):
    if self.num2 == 0:
        print("Division by zero is not allowed.")
    else:
        div=self.num1 / self.num2
        print("The division of", self.num1, "and", self.num2, "is: ", div)

# Create an instance of the calculator class
calc = calculator(10, 5)
# Call the methods
calc.add = add.__get__(calc)