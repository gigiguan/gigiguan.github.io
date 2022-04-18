def adFunc(n, num):
    for i in range(num - 1):
        for j in range(num - i - 1):
            if(n[j] > n[j + 1]):
                num2 = n[j]
                n[j] = n[j + 1]
                n[j + 1] = num2

def deFunc(n, num):
    for i in range(num - 1):
        for j in range(num - i - 1):
            if(n[j] < n[j + 1]):
                num2 = n[j]
                n[j] = n[j + 1]
                n[j + 1] = num2

def sort():
    while True:
        n = []
        num = int(input("How many numbers would you like to sort? : "))
        for i in range(num):
            number = int(input("What is the %d number? : " %i))
            n.append(number)


        answer = input("Would you like to sort these numbers in ascending (A) or descending (D) order? ")
        if answer == "A":
            adFunc(n, num)
            print("The List in Ascending Order : ", n)

        elif answer == "D":
            deFunc(n, num)
            print("The List in Descending Order : ", n)

        final = input("Run again? (Y/N) ")
        if final == "Y":
            continue
        else:
            print("Bye.")
            break


if __name__ == "__main__":
    sort()