# Python function to find a range of primes
def findprimes(min, max):
    for Number in range(min, max + 1):
        count = 0
        for i in range(2, (Number // 2 + 1)):
            if (Number % i == 0):
                count = count + 1
                break
        if (count == 0 and Number != 1):
            print(" %d" % Number, end='  ')
print()


def primes():
    minimum = 1
    print("Imperative- The Minimum Value for Primes Test is 1.")
    maximum = 20
    print("Imperative- The Maximum Value for Primes Test is 20.")
    print("Imperative- The Prime Numbers between ", minimum, "and ", maximum, "is: ")
    findprimes(minimum, maximum)
    print()


# Define a class for Checking prime number
class Prime:
    # Constructor
    def __init__(self,number) :
        self.num = number
    # define a method for checking number is prime or not
    def isPrime(self) :
        for i in range(2, int(num ** (1/2)) + 1) :
            # if any number is divisible by i
            # then number is not prime
            # so return False
            if num % i == 0 :
                return False
        # if number is prime then return True
        return True

# Main code
if __name__ == "__main__" :
    #Imperative
    primes()
    # #OOP: input number
    # num = 29
    # # make an object of Check class
    # print("OOP- Checking if ", num, " is a prime number...")
    # check_prime = Prime(num)
    # # method calling
    # print(check_prime.isPrime())
    # num = 51
    # print("OOP- Checking if ", num, " is a prime number...")
    # check_prime = Prime(num)
    # print(check_prime.isPrime())
