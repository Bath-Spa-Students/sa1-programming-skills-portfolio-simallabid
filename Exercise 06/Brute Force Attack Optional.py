        
''' Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.'''


maxi_attempts = 5
correct_pass = '12345'
attempts = 0

while attempts < maxi_attempts:
    password = input("Enter the password: ")
    if password == correct_pass:
        print('Correct Password!')
        break
    else:
        attempts +=1
        remaining_attempts= maxi_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect answer! You have {remaining_attempts} attempts left.")
        else:
            print("You have reached the maximum limit of attempts. The authorities have been informe")