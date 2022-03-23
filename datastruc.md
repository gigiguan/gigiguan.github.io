{% include navigation.html %}

## **Code**
### **Week 2**
Hack 1

![image](https://user-images.githubusercontent.com/89219495/159799434-3a359919-1214-4da0-91a4-9f39963f7c96.png)




### **Week 1**
Check Replit(navbar) for runtime
```
# Hack 1: InfoDB lists

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Gigi",  
               "LastName": "Guan",  
               "DOB": "June 23",  
               "POB": "Shanghai",  
               "Email": "gigikwan180@gmail.com",  
               "Favorite_movies":["Chungking Express", "Before Sunrise", "Euphoria"]  
              })  

InfoDb.append({  
               "FirstName": "Ariel",  
               "LastName": "Jin",  
               "DOB": "April 27",  
               "POB": "Beijing",  
               "Email": "arielj@gmail.com",  
               "Favorite_movies":["Dune", "My Blueberry Nights"]  
              })  

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Favorite movies: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Favorite_movies"]))  # join allows printing a string list with separator
    print()
```

```
# Hack 2: InfoDB loops.
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
      

# for loop iterates on length of InfoDb- Gigi Guan
#change the while loop to move argument n inside the definition - Gigi Guan
def while_loop():
    n = 0
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(): # Pass an argument and sometimes do not pass an argument, so I just remove all the arguments - Gigi Guan
  #Those that already have a function, then I made a new one without it and call if recursively - Gigi Guan
    n = 0
    recursive_loop1(n)
    return

def recursive_loop1(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop1(n + 1)
    return # exit condition


def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion
```

```
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
                print()

            except ValueError:
                print('Invalid input. Please enter an integer input.')
        else:
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

```

### **Week 0**
Check Replit(navbar) for runtime
```
# Menu options in print statement
def print_menu1():
    print('1 -- Kiwi Starfruit Drink' )
    print('2 -- Dragon Drink' )
    print('3 -- Pink Drink' )
    print('4 -- Vanilla Latte' )
    print('5 -- Green Tea Creme Frappuccino' )
    print('6 -- Iced White Chocolate Mocha' )
    print('7 -- Exit' )
    runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'Kiwi Starfruit Drink',
    2: 'Dragon Drink',
    3: 'Pink Drink',
    4: 'Vanilla Latte',
    5: 'Green Tea Creme Frappuccino',
    6: 'Iced White Chocolate Mocha',
    7: 'Exit',
}

# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

# menu option 1
def one():
    print('Enjoy your \' Kiwi Starfruit Drink\'')

# menu option 2
def two():
    print('Enjoy your \'Dragon Drink\'')

# menu option 3
def three():
    print('Enjoy your \'Pink Drink\'')

def four():
    print('Enjoy your \'Vanilla Latte\'')

def five():
    print('Enjoy your \'Green Tea Creme Frappuccino\'')

def six():
    print('Enjoy your \'Iced White Chocolate Mocha\'')


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('What would you like to order today? (enter 1-7) '))
            if option == 1:
                one()
            elif option == 2:
                two()
            elif option == 3:
                three()
            elif option == 4:
                four()
            elif option == 5:
                five()
            elif option == 6:
                six()


            # Exit menu
            elif option == 7:
                print('Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 7.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    # print_menu1()
    print_menu2()
 ```
 
### Week 0 Data Structures Challenge
Check Replit(navbar) for runtime
```
def tree():
    n = int(input("How many rows: "))
    # number of spaces
    k = n - 1
    # outer loop to handle number of rows
    for i in range(0, n):
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
        # decrementing k after each loop
        k = k - 1
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
            # printing stars
            print("* ", end="")
        # ending line after each row
        print(" ")

if __name__ == "__main__":
    tree()
```


