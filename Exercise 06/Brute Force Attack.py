'''Exercise 6: Brute Force Attack - 30 Marks

Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.'''

password='12345'  #the given password
while True:       #using while loop
    ans= input("Enter the password: ")  #taking answer from the input
    if ans==password:                   #using if statement
        print("Your answer is correct!")
        break                           #break function is used to break the loop once the answer is correct.
    else:
        print("Your answer is incorrect! Try again!") #output if the input in incorrect
        

    
