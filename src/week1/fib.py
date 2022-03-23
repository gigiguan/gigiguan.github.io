# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)
# this is test driver or code that plays when executed directly, versus import which will not run these statements
def tester():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input
def fibonacci():
    count = int(input("Enter fibonacci sequence count: "))
    n = 0
    while n <= count:
      print(fibonacci1(n),end = " ")
      n+=1
    print()
    return 
  
def fibonacci1(n):

    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

