sum = lambda x: x + 15
product = lambda x, y: print(str(x)+" x"+str(y)+" is : ",x * y)

number = int(input("Enter a number : "))
result = sum(number)
print("Result after adding 15 to", number, ":", result)

product(5, 6)