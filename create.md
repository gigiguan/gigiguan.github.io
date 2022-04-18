  <div id="video_wrapper">
    <video autoplay loop>
        <source src="https://drive.google.com/uc?export=view&id=1kAw4XIS3JH_cpTHGMRsV0mwl7dcFz2wq" type="video/mp4">
    </video>
  </div>


## [Create Task Runtime](https://youtu.be/v8RZpsUFwvw)
## [Code](https://github.com/gigiguan/gigiguan.github.io/blob/main/src/create.py)
3a.
i. The overall purpose of the program is to sort user-inputted numbers in ascending order or descending order.

ii. The video shows how users can sort the numbers that they inputted in ascending or descending order based on the user's choice. Also, the program restarts or ends based on the user input.

iii. The user first enters '5' indicating that they would to sort a total of five numbers. Then, the user enters 'an input to determine how many numbers they want to sort. Then, the user enters '3', '6', '7', '2', '5' indicating the specific numbers that they would like to sort. The program then prompts the user to enter 'A' or 'D'. The user enters 'A' indicating that they would like to sort the 5 numbers in ascending order. The output given reads "The List in Ascending Order : 2, 3, 5, 6, 7". The user enters "Y" to replay the program. This time, the user enters 'D' to sort the numbers in descending order. The output given is "The List in Ascending Order : 7, 6, 5, 3, 2". The user enters "N" to end the program. The output given is "Bye."

3b. 
i. 
![image](https://user-images.githubusercontent.com/89219495/155937154-d511d67c-ff72-4f65-b787-6ebdca129bd8.png)

ii. 
![image](https://user-images.githubusercontent.com/89219495/155937108-e6ffaf59-ef5e-4931-89c3-58b5e91c3db0.png)

The data contained in the “array” represent integers that the user inputted. It makes sorting the integers from smallest to biggest or biggest to smallest much easier because it allows the numbers to compare with adjacent numbers and exchanges those that are out of order. With every pass, the largest or smallest integers bubbles up to the end of the list depending on if the array is to be sorted in ascending or descending order. 


3c.
i. 
![image](https://user-images.githubusercontent.com/89219495/155937082-0be23b54-e195-4edf-8b70-79c97371fe35.png)

ii. 
![image](https://user-images.githubusercontent.com/89219495/155937203-197a91fd-a64b-47cb-80f8-0558d5c6973d.png)

iii. The functions allows the numbers to compare with adjacent numbers and exchanges those that are out of order. With every pass, the largest or smallest integers shifts to the end of the list depending on if adFunc() or deFunc() is called.

iv. "val" represents the number of elements the user inputted. There are two for loops. The first for loop (for i in range(val -1)) iterates the list until the list is sorted completely and the second for loop (for j in range(val-i-1)) iterates the list and then swap unsorted adjacent elements. In adFunc, if an element (a[j]) is greater than the element to the right of it (a[j]+1), the two elements will switch positions so that the greater element shifts to the end of the list. This can be seen as a[j] is set equal to temp, a[j+1] replaces a[j], and at last temp replaces the original a[j+1]. deFunc works differently from adFunc in that the smaller element shifts to the end of the list.

3d.
i. 
First call: The user enters "A" after inputting the numbers '3', '6', '7', '2', '5'. Entering "A" calls and executes the adFunc() function.

Second call: The user enters "D" after inputting the numbers '3', '6', '7', '2', '5'. Entering "D" calls and executes the deFunc() function. 

ii. 
The condition tested by the first call is whether the user inputted A or D after being prompted "Would you like to sort these numbers in ascending (A) or descending (D) order? ". If the user's answer is "A", then adFunc() will be called and the list will be sorted accordingly.

The condition tested by the second call is whether the user inputted A or D. If the user's answer is "D", then deFunc() will be called and the list will be sorted accordingly.

iii.
First call: The list of numbers sorted in ascending order is returned - "The List in Ascending Order: 2, 3, 5, 6, 7".

Second call: The list of numbers sorted in descending order is returned - "The List in Descending Order: 7, 6, 5, 4, 2".
