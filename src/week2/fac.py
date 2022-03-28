class Factorial:
    def __call__(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * self(n-1)


# def factorial():
#   # this would create an instance of the Factorial class
#   fac = Factorial()
#   print(fac(1))

# make a def factorial () for testing
def factorial():
    num = [1,2,3,4,5,6,7,8]
    for fact in num:
        # mypal = MyPal()
        fac = Factorial()
        print(fact,"! = ", fac(fact))

if __name__ == "__main__":
    factorial()
