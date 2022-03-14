## **Github page actions**
### 5.1
1. One aspect of technology that has had a great impact on society is how it affects learning. It’s made learning more interactive and collaborative, this helps people better engage with the material that they are learning and have trouble with. Another way technology has impacted society is through communication, how we can easily and quickly communicate with one another worldwide. It also allows for the easier access of information worldwide. Some of the negative effects of computers are human's break their social interact with friends and families, cause mental health problems like depression, and poor physical health. Computer addiction is really dangerous to our lives and has consequences that can affect academic performance as well.


2. Dopamine is a real issue especially in teenagers who can't control their screen time. When students feel stressed or want to take a break from their academic work, they turn to video games or social media, both of which are related to dopamine. When teens feel pleasure playing video games or scrolling through social media, they tend to forget about time and this affects their academic performance and sleep as well.

### 5.2
1. Someone can empower themself in a digital world by confidently participating in the digital world. For example, on social media, people can gain countless followers by posting content that appeals to their audience. Considering another example, people who have extraordinary gaming skills can empower themself in the digital gaming world. I think digital empowerment means to maximize personal potential through digital technology.

2. Someone can empower someone else by inspiring them and giving them guidancde. Something I could do at Del Norte HS is giving words of encouragement or even giving constructive feedback to those who are not empowered or not confident, so that they feel moved, encouraged, supported, and grow to become more motivated and confident.

3. Red tape is defined as a lot of official forms and procedures that are involved before something is accomplished. I think it can affect digital empowerment as individuals may feel overwhelmed by the amount of red tape before they even access something that allows them to empower themselves in the digital world. I There are such barriers at Del Norte. For example, students have to get tons of signatures and fill out numerous forms just to take or drop a course of their choice. Red tape is particularly burdensome to smaller businesses. Smaller businesses can drown in a sea of red tape, as there are so many requirements and documents that they have to follow before they start up their business. 

### **Data Structures**
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

## **Create Task**
 ```
def adFunc(a, val):
    for i in range(val -1):
        for j in range(val - i - 1):
            if(a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

def deFunc(a, val):
    for i in range(val -1):
        for j in range(val - i - 1):
            if(a[j] < a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

while True:
    a = []
    val = int(input("Please Enter the Total Elements : "))
    for i in range(val):
        value = int(input("Please enter the %d Element : " %i))
        a.append(value)


    answer = input("Would you like to sort these numbers in ascending (A) or descending (D) order? ")
    if answer == "A":
        adFunc(a, val)
        print("The List in Ascending Order : ", a)

    elif answer == "D":
        deFunc(a, val)
        print("The List in Descending Order : ", a)

    final = input("Run again? (Y/N) ")
    if final == "Y":
        continue
    else:
        print("Bye.")
        break


if __name__ == "__main__":
    adFunc(a, val)
    deFunc(a, val)
 ```
[Runtime](https://www.youtube.com/watch?v=v8RZpsUFwvw&feature=youtu.be)
