import src.week0.menu
import src.week0.tree
import src.week1.hacks
import src.week1.fib
import src.week2.fac
import src.week2.color
import src.week0.ship
import src.week2.factorialinput
import src.week2.easteregg
from src.week2.prime import Prime

#Vidhi's Additions:
# Colored Numbers
# Ship with Color
# Factorial With input
# EasterEgg Submenu
# Number Table
# Word Expansion
# Number Pattern

main_menu = [
    ["Menu/Swap", src.week0.menu.print_menu2],
    ["Tree", src.week0.tree.tree],
    ["Fibonacci", src.week1.fib.fibonacci],
    ["Color", src.week2.color.numb],
    ["Ship", src.week0.ship.driver],
]

sub_menu = [
    ["Primes", src.week2.prime.primes],
    ["Factorial", src.week2.fac.factorial],
    ["Factorial Input", "src/week2/factorialinput.py"]
]

patterns_sub_menu = [
    ["For Loop", src.week1.hacks.for_loop],
    ["While Loop", src.week1.hacks.while_loop],
    ["Recursive Loop", src.week1.hacks.recursive_loop],
]

easteregg_sub_menu = [
    ["Word Expansion", src.week2.easteregg.word],
    ["Number Table", src.week2.easteregg.rows],
    ["Number Pattern", src.week2.easteregg.pattern]
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"



def patterns_submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, patterns_sub_menu)
    m.menu()


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Loops", patterns_submenu])
    menu_list.append(["Math", submenu])
    menu_list.append(["EasterEgg", easteregg_submenu])
    buildMenu(title, menu_list)

def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
  
def easteregg_submenu():
    title = "EasterEgg Submenu" + banner
    buildMenu(title, easteregg_sub_menu)
  
def patterns_submenu():
  title = "Patterns Submenu" + banner
  buildMenu(title, patterns_sub_menu)
  

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
