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

#On line 11 we have the 1st error: factorial() missing 1 argument: 'n'.
#As we would need to calculate the factorial of the number that user will enter, we need to give our factorial() function the argument: num

#Now we have a 2nd error: for i in range(), expected at least 1 argumernt, got 0.
#For the range() function to correctly run we need to give it at least one argument. So we can say range(2) for now, on line 6.
#At this point when entering : 2 or any other number the output is: The factorial of 10 is None
#That is because the for loop is not correctly added in our condition statements and there is no calculation to be made
#Also, on line 7 we have not assigned result * 1 to a variable, which is why line 8 return, won't be able to return our result
#In order to return our result, we need to correct line 8 and add result for the return

#Now we still don't have the correct output, because we also need to correct the next condition statements in order to make the calculation right
#and also return the result of the loop by assigning result * 1 to the variable "result"
#Therefore, because result*1 is not assigned to the variable result, the result can not be returned which is why we keep getting 
#incorrect output : The factorial of 2 (or any other number) is 1 this time.
#We will now assign the the result * 1 to variable "result" on line 7

#At this point, The output for this is: The factorial of 2(or any other number) is 0, which is still not correct.
#That is because for i loop starts i with 0, which means i=0 and that is starting with 0 because we have only used 2 as an argument
#for range() function, so it would only generate numbers 0 and 1.
#On the first iteration i=0, the multiplication result= result * 0 will result in result= 0 because anything multiplied by 0 is 0 #
#and on the 2nd iteration i=1 will result in result= result * 0 
#will also be 0 because any number multiplied by 0 is still 0 as we have the result=0 from the previous iteration.
#1st iteration result= 1 * 0(this is n), result= 0; 2nd iteration result= 0 * 1 (this is n)

#Now we will also add another argument so that we can have a start and stop for our range function and to allow it to calculate from 2 to n, 
#as n + 1 is exclusive and not included.
#The n + 1,2nd argument in range() function : +1 generates numbers up but not including the stopping number (n + 1).
#To include "n", we need to use n+1 as the end point. For example if n=5, range(2,6) generates [2,3,4,5] because 6 is exclusive;
#Which means that it calculates the numbers starting from 2, all the way up to n.
#range() function controls how many times the loop will run and what values it will take during each iteration by generating a series of numbers 
#it starts from 2 and ends at n (the number user enters), which also means it will go up to n because the stop value in range() is 
#exclusive meaning it doesn't include n + 1.
#The for loop will go through each number from n to 2 and multiply the current result with next number in the sequence for i, each time.
#Also the result is being updated each step which contributes to the factorial being built up.

#Please see below a 2nd way to resolve this.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2,n + 1):
#             result = result * i
#     return result
# num = int(input("Enter a number: "))
# factorial_result = factorial(num) 
# print(f"The factorial of {num} is: {factorial_result}")         

#3rd Way to resolve it.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*(factorial(n-1))
    
# num = int(input("Enter a number: "))

# print(f"The factorial of {num} is : {factorial(num)}")


