num1 = 10
num2 = 20

try:
    if num1 == 0:
        raise ZeroDivisionError("num1 cannot be zero")
    result = num1 / num2
    print(result)

except ValueError as e:
    print("ValueError:", e)
