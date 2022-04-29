---
title: Proctored MCQ 1,2,3 Corrections
---
  <div id="video_wrapper">
    <video autoplay loop>
        <source src="https://drive.google.com/uc?export=view&id=1kAw4XIS3JH_cpTHGMRsV0mwl7dcFz2wq" type="video/mp4">
    </video>
  </div>
  
### **Quiz 3: Score 41/50**
**Q7 Result of iteration statements**
![image](https://user-images.githubusercontent.com/89219495/165630253-946768b3-7b2a-4e96-a813-f982c26a7361.png)

Which of the following best describes the value returned by the procedure?

A: The procedure returns the sum of the integers from 1 to n.
* Explanation: The procedure initially sets result to 1 and j to 2. In the REPEAT UNTIL loop, result is first assigned the sum of result and j, or 1 + 2. The value of j is then increased to 3. In each subsequent iteration of the loop, result is increased by each successive value of j (3, 4, 5, etc.) until j exceeds n. Therefore, the procedure returns the sum of the integers from 1 to n.
* Reflection: The answer is not "the procedure returns the value of 2 * n" because the procedure does not return the value of 2 * n. For a procedure to return 2 * n, it could initialize result to 0 and then repeatedly add 2 to result a total of n times.

**Q9 Apartment rental Web site flowchart**

A flowchart is a way to visually represent an algorithm. The flowchart below is used by an apartment rental Web site to set the variable include to true for apartments that meet certain criteria.

![image](https://user-images.githubusercontent.com/89219495/165849224-b2ab8a6b-ecac-4415-b361-78a40c9e12dd.png)
![image](https://user-images.githubusercontent.com/89219495/165849386-c62097f0-5c57-4050-b255-5016e116e96d.png)

Which of the following statements is equivalent to the algorithm in the flowchart?

A: include <- (floor > 10) OR (bedrooms = 3)
* Explanation: The flowchart sets include to true whenever floor is greater than 1 0 or bedrooms equal 3, and sets include to false otherwise. Therefore, the algorithm is equivalent to include <- (floor > 10) OR (bedrooms = 3).
* Reflection: The answer is not include <- (floor > 10) AND (bedrooms = 3) because this expression would be used for a flowchart to set include to true whenever floor is greater than 1 0 and bedrooms equal 3. This does not correctly set include to true in cases where only one of the two conditions is true.

**Q17 Test cases for procedure Smallest**

The procedure Smallest is intended to return the least value in the list numbers. The procedure does not work as intended.

![image](https://user-images.githubusercontent.com/89219495/165849897-b5c83989-a783-4f2c-81af-f1d4742e8085.png)

For which of the following values of the List will Smallest(the List) NOT return the intended value? Select two answers.

A: theList <- [30, 40, 20, 10] and theList <- [40, 30, 20, 10]
* Explanation: The procedure returns the first number it encounters that is less than the first number in the list. For the list [30, 40, 20, 10], the procedure returns 20, which is not the least value in the list. Also, the procedure returns the first number it encounters that is less than the first number in the list. For the list [40, 30, 20, 10], the procedure returns 30, which is not the least value in the list.
* Reflection: I did not see the part of the question that says "Select two answers". I only chose one answer. I need to remember to read every question thoroughly.


**Q21 Use of weak passwords**

Which of the following best explains how devices and information can be susceptible to unauthorized access if weak passwords are used?

A: Unauthorized individuals can use data mining and other techniques to guess a user’s password.

* Explanation: A strong password is something that is easy for a user to remember but would be difficult for someone else to guess based on knowledge of that user. Weak passwords can often be guessed based on publicly available information about a user. Other weak passwords (such as "password" or "1234") can often be guessed because they are commonly used.
* Reflection: THe answer is not that unauthorized individuals can exploit vulnerabilities in encryption algorithms to determine a user’s password from their encryption key because the exploitation of encryption algorithms is not related to password strength.

**Q35 Consequences of downloading licensed music seller**

A user reads reviews of a popular artist’s new album and then downloads the album from the Web site of a licensed online music seller. Which of the following is LEAST likely to be a consequence of this action?

A: The user will be in violation of the Digital Millennium Copyright Act (DMCA).
* Explanation: If the album was purchased and downloaded through a licensed music store, the user will not be in violation of the DMCA.
* Reflection: The choice "Album reviews from other people who live nearby will be displayed to the user." is incorrect because geolocation data can be accessed by the Web site, which can use this information to provide album reviews from nearby users.


**Q41 Encrypting and decrypting using public key cryptography**

In public key cryptography, the sender uses the recipient’s public key to encrypt a message. Which of the following is needed to decrypt the message?

A: The recipient’s private key
* Explanation: In public cryptography, a message is encrypted with a recipient’s public key and decrypted with the recipient’s private key.
* Reflection: The sender’s public key cannot be used to decrypt the message.

**Q42 Number of bits needed for item inventory**

A store uses binary numbers to assign a unique binary sequence to each item in its inventory. What is the minimum number of bits required for each binary sequence if the store has between 75 and 100 items in its inventory?

A: 7
* Explanation: Using 6 bits will only allow for up to 64 sequences because 2^6=64. Using 7 bits will allow for up to 128 sequences because 2^7=128. Therefore, a minimum of 7 bits are needed.
* Reflection: Using 6 bits will only allow for up to 64 sequences because 2^6=64 but 100 items are needed.

**Q44 Abstraction with procedures Square and Cube**

A programmer notices the following two procedures in a library. The procedures do similar, but not identical, things.

![image](https://user-images.githubusercontent.com/89219495/165868217-bcc33146-b694-4d67-972f-5509f5d6e238.png)

Which of the following procedures is a generalization of the procedures described above?

A: Procedure Power(n, m), which returns the value n^m
* Explanation: The procedures square and cube are each used to determine a power of n. A generalization of this procedure
is Power(n, m), which calculates n raised to the m power.
* Reflection: Polynomial(n) calculates the sum of the square and cube procedures, but does not generalize their functionality to calcualte the power of n.


**Q46 Examples of symmetric encryption**

Which of the following is an example of symmetric encryption?

A: Finn and Gwen develop a system that maps each letter of the alphabet to a unique symbol using a secret key. Finn uses the key to write a message to Gwen where each letter is replaced with the corresponding symbol. Gwen uses the key to map each symbol back to the original letter.
* Explanation: This is an example of symmetric encryption because the secret key is used for both encryption and decryption of messages.
* Reflection: "Evy buys a locked box that operates using two different codes. When the first code is entered, a slot opens that allows a message to be put in the box. When the second code is entered, the door to the box opens. Evy gives the first code to her friends so they can leave messages for her and keeps the second code to herself so that she is the only one who can retrieve the messages." is incorrect because this is an example of an asymmetric system because different codes are used to send and receive messages.

**Other topics to review/Additional notes:**
* An undecidable problem is one for which no algorithm can be constructed that is always capable of providing a correct yes-or-no answer. Some instances of an undecidable problem may have an algorithmic solution, but there is no algorithmic solution that could solve all instances of the problem.
* Devices on the Internet communicate using standard protocols, which do not depend on the manufacturer.
* Creative Commons licensing allows copyright owners to specify the ways in which their works can be used or distributed. This allows individuals to access or modify these works without the risk of violating copyright laws.
* Binary 1011 is equivalent to ![image](https://user-images.githubusercontent.com/89219495/165863392-3562f69d-0351-4930-b125-88d18b2c1c16.png), or decimal 11, and binary 1101 is equivalent to ![image](https://user-images.githubusercontent.com/89219495/165863415-4c27ffa3-8fdd-4443-bc78-798767b418ac.png), or decimal 13. The order of the numbers (written in their equivalent decimal format) is 5, 11, 12, 13.
* The Internet is the global system of interconnected computer networks that uses protocols to connect devices worldwide. The World Wide Web is an information system (of pages, programs, and files) that is accessible over the Internet.
* With a 4-bit integer representation, 2^4 values can be represented, which allows for the values between 0 to 15, inclusive
* Linear efficiency: reasonable amount of run time; Factorial efficiency (n!): unreasonable amount of run time, so a heuristic approach can be used to find an approximate solution.
* A no-rights-reserved Creative Commons license is used when the creator of a published work wants the work to be made freely available to everyone.

### **Quiz 1: Score 42/50**
Q8: Which of the following is most likely to be a benefit of storing the information from each calling session in a database?
![image](https://user-images.githubusercontent.com/89219495/164559019-53d7bbd0-6cdb-4b99-8b74-5ed0649d4ad8.png)
A: The company can analyze the calling session data and thereby make better business decisions.
* Storing information about each call will increase the amount of data storage needed, which is likely to increase the need for data compression.
* By storing information about each call, the company can use machine learning and data mining and thereby make business decisions based on their customers’ needs.

**Q13**
![image](https://user-images.githubusercontent.com/89219495/164559060-71b12b63-df4b-462b-bd01-4480d1b7f383.png)
A: Do the movement patterns of the animal vary according to the weather?

**Q14**: An online store uses 6-bit binary sequences to identify each unique item for sale. The store plans to increase the number of items it sells and is considering using 7-bit binary sequences. Which of the following best describes the result of using 7-bit sequences instead of 6-bit sequences?
A: 2 times as many items can be uniquely identified.
* Using 6-bit binary sequences allows for 26 or 64 different items to be identified. Using 7-bit binary sequences allows for 27 or 128 different items to be identified. Thus there are two times as many items that can be uniquely identified.

**Q20 Collections of books to be combined**
![image](https://user-images.githubusercontent.com/89219495/164559090-e997cf9e-cc83-4158-ac94-5f2eb4fa1dac.png)

A: 

newList ← Combine (list1, list2)

newList ← Sort (newList)

newList ← RemoveDuplicates (newList)

* When list1 and list2 are combined, the newList may have duplicates and will likely not be sorted. Performing the Sort and then the RemoveDuplicates procedures will result in a list that is sorted, has no duplicates, and contains the names of all the books found in either list1 or list2.

**Q23**: Which of the following has the greatest potential for compromising a user’s personal privacy?
A: A group of cookies stored by the user’s Web browser
* The aggregation of information in browser cookies can be used by websites that the user visits to track the user and collect information about the user.

**Q28**: Which of the following is a true statement about data compression?
A: There are trade-offs involved in choosing a compression technique for storing and transmitting data.

**Q32**: Error in countNumOccurences procedure
![image](https://user-images.githubusercontent.com/89219495/164559158-5fda3646-bff0-46c2-a9a9-f0e54b672dcb.png)
A: Moving the statement in line 5 so that it appears between lines 2 and 3


**Q37**: initial values that yield incorrect value of max
![image](https://user-images.githubusercontent.com/89219495/164559182-da716150-b7aa-4438-9b53-b5c3847400ac.png)
A: x = 3, y = 2, z = 1

**Q39**: minimize execution time using parallel computing
![image](https://user-images.githubusercontent.com/89219495/164559205-57d82b7f-1e93-4141-9434-dd8d38ef5f09.png)

A: Take the two shortest execution times and add them - 30+50=80 seconds

### **Quiz 2: Score 46/50**

**Q7 Advantage of lossless over lossy compression**
* Which of the following is an advantage of a lossless compression algorithm over a lossy compression algorithm?
* A lossless compression algorithm can guarantee reconstruction of original data, while a lossy compression algorithm cannot.
* Lossless compression algorithms are guaranteed to be able to reconstruct the original data, while lossy compression algorithms are not.

**Q8 Advantages of open source software**
* Which of the following is NOT an advantage of using open-source software?
* The original developer of open-source software provides free or low-cost support for users installing and running the software.
* Open-source software has source code that is released under a license that allows users the rights to use and distribute it. However, there is no guarantee that the original developer of open-source software will provide support for its users.

**Q45 Combine data sources**
![image](https://user-images.githubusercontent.com/89219495/164558745-d387d002-8fed-42f7-b080-1bc4e967f794.png)
* Spreadsheets I and II
* The desired information can be determined by using the student IDs in spreadsheet II to identify the students who play a sport. Once the students who play a sport are identified, the grade point averages of students who play sports in spreadsheet I can be compared to the grade point averages of all other students in spreadsheet I.

**Q49 Compression**
![image](https://user-images.githubusercontent.com/89219495/164558806-8723999b-cc35-4499-9e51-2792961f7601.png)
Byte pair encoding is an example of a lossless transformation because an encoded string can be restored to its original version.
