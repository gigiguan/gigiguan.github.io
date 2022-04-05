def word():
  word = "CSPIsCool"
  x = ""
  for i in word:
    x += i
    print(x)

def rows():
  rows = 10
  for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i * j, end=' ')
    print()

def pattern():
  rows = 6
  for i in range(0, rows):
    for j in range(rows - 1, i, -1):
        print(j, '', end='')
    for l in range(i):
        print('    ', end='')
    for k in range(i + 1, rows):
        print(k, '', end='')
    print('\n')
