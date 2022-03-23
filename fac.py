class Fibonacci:
    def __init__(self):
        self.fiboSeq = [0, 1]


    def __call__(self, n):
        if n < len(self.fiboSeq):
            return self.fiboSeq[n]
        else:
            # Compute the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2) # two recursive calls to self (__call__(self, n))
            self.fiboSeq.append(fib_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.fiboSeq[n]


fibo_of = Fibonacci() # object instantiation and run __init__ method
print(fibo_of(5)) # object running __call__ method