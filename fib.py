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
    while True:
        if n <= count:
            try:
                print(fibonacci1(n),end = " ")
                n+=1
            except ValueError:
                print('Invalid input. Please enter an integer input.')
    print()
    return

def fibonacci1(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

if __name__ == "__main__":
    fibonacci()

