### **Data Structures Week 0**
[Runtime](https://replit.com/@GigiGuan/gigiguangithubio#main.py)
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
 
### Data Structures Challenge
[Runtime](https://replit.com/@GigiGuan/gigiguangithubio#tree.py)
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

