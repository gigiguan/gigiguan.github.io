class Factorial:
  def __init__(self):
    self.fact = [1]
  def __call__(self,n):
    if n < len(self.fact):
      return 1
    else:
      fact_number = n * self(n-1)
      self.fact.append(fact_number)
    return self.fact[n]

factorial_of_n = Factorial()
n = int(input("n = "))
print(factorial_of_n(n))
