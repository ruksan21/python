#initialization, condition, increment/decrement

#while loop
# i=1
# while i < 10:
#     print(i)
#     i += 1 # increment by 1 (i=i+1) yasari ni garnu sakinxa
    
# #for loop
# for i in range( 10): # range(start, stop, step)
#     print("hello world")
    
# num = int(input("Enter a number: "))
# sum=0
# for i in range(num):
#     num2 = int (input("Enter a number: "))
#     sum = sum + num2
# print("The sum of the numbers is:", sum) #condition aanusar bhitra rw bihera rakhnu milxa
 
# for j in range(5):
#     for k in range(j):
#         print(j, end="")
#     print()  # New line after each inner loop iteration
# # Nested loops example
for i in range(1, 4):  # Outer loop
  for j in range(1, 4):  # Inner loop
    print(i * j, end='')
print()
    