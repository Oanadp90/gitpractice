def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(2, n + 1): #2nd error: for i in range(), range expected at least 1 argument, got 0
         result = result * i
        return result

num = int(input("Enter a number: "))
factorial_result = factorial(num) #1st error: factorial() missing 1 argument: 'n'
print(f"The factorial of {num} is: {factorial_result}")  