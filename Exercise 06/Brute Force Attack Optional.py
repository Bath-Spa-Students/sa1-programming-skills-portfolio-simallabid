        
''' Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.'''


maxi_attempts = 5      #maximum attempts mentioned
correct_pass = '12345' 
attempts = 0           #attempts start at zero

while attempts < maxi_attempts:               #using while loop to ask the user for input until the answer is correct
    password = input("Enter the password: ")  #takes input from the user
    if password == correct_pass:
        print('Correct Password!')
        break                                 #function stops executing once the answer is correct
    else:
        attempts +=1                          #attempt increases as the user keeps on guessing the wrong password
        remaining_attempts= maxi_attempts - attempts  #the user only has 5 attempts and hence the attempt decreases with the wrong guesses
        if remaining_attempts > 0:
            print(f"Incorrect answer! You have {remaining_attempts} attempts left.")     #it tells the user number of attempts they have left if they enter an incorrect answer
        else:
            print("You have reached the maximum number of attempts. The authorities have been informed")  #message will display if the max number of attempts is reached