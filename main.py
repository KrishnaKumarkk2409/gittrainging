print(" hell")
a= 1
b=2 
c= a*b
print(c)
print("hello world")


sum=a+b
print("The sum of", a, "and", b, "is", sum)



num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


for i in range(1, 6):
    print("Number:", i)


# make a calculator
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y    
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ('1','2','3', '4' ):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid Input")
if __name__ == "__main__":
    calculator()    
    


print("hello world, this is a test from Krishna")
print("This is a test for the GitHub Actions workflow.")
print("This is a test for the GitHub Actions workflow, with a change.")
