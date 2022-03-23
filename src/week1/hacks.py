import time


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