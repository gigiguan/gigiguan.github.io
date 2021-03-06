"""
Introduction to Console Programming
Writing a function to print a menu
"""


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

def swap1(option, option2):
    if option > option2:
        option2, option = option, option2  # swap values
    return option, option2  # return 2 values

def swap1_helper(option, option2):
    print("This is your order: ", option, option2)
    option, option2 = swap1(option, option2)
    print("We recommend you drink them in this order: ", option, option2)
    print()
    # no return value

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
            option2 = int(input('What else would you like to order? (1-7)'))
            if option2 == 1:
                one()
            elif option2 == 2:
                two()
            elif option2 == 3:
                three()
            elif option2 == 4:
                four()
            elif option2 == 5:
                five()
            elif option2 == 6:
                six()

            else:
                print('Invalid option. Please enter a number between 1 and 7.')
            swap1_helper(option, option2)
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    # print_menu1()
    print_menu2()
    swap1_helper()