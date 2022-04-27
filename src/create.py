#functions allows the numbers to compare with adjacent numbers and exchanges those that are out of order
def asc(n, num):
    for i in range(num - 1):
        for j in range(num - i - 1):
            if(n[j] > n[j + 1]):
              #allows the numbers to compare with adjacent numbers and exchanges those that are out of order
                num2 = n[j]
                n[j] = n[j + 1]
                n[j + 1] = num2
              #larger integers bubbles up to the end of the list

def des(n, num):
    for i in range(num - 1):
        for j in range(num - i - 1):
            if(n[j] < n[j + 1]):
                num2 = n[j]
                n[j] = n[j + 1]
                n[j + 1] = num2
              #smaller integers bubbles up to the end of the list

def sort():
  while True:
        #array represent integers that the user inputted
        n = []
        num = int(input("How many numbers would you like to sort? : "))
        for i in range(1, num+1):
          number = int(input("What is number %s? : " %i))
          n.append(number)
           
        answer = input("Would you like to sort these numbers in ascending (A) or descending (D) order? ")
        #changes input answer to upper case to avoid errors
        answer2 = answer.upper()
        if answer2 == "A":
            #calls adFunc()
            asc(n, num)
            print("Here are the sorted numbers : ", n)
  
        elif answer2 == "D":
            #calls deFunc()
            des(n, num)
            print("Here are the sorted numbers : ", n)
        else:
          print("Invalid input. Please enter 'A' or 'D'")


        final = input("Run again? (Y/N) ")
        final2 = final.upper()
        if final2 == "Y":
            continue
        elif final2 == "N":
            print("Bye.")
            break
        else:
          print("Invalid input. Please enter 'Y' or 'N'")


if __name__ == "__main__":
    sort()
