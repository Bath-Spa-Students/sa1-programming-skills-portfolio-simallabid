'''Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.'''

days_in_a_month = {
    1: 31,  
    2: 28,   #(non-leap year)
    3: 31, 
    4: 30, 
    5: 31, 
    6: 30,
    7: 31, 
    8: 31, 
    9: 30, 
    10: 31,
    11: 30, 
    12: 31 
}

month = int(input("Enter the month number (1-12): "))        #asks the user for the month number

if 1 <= month <= 12:                                         #using the if else statement to check if the input is valid or not
    if month == 2:                                           #checks for febryary if the user inputs 2 to check if it's a leap year or not
        leap_year = input("Is it a leap year? (yes/no): ")   #takes the input from the user
        if leap_year.lower() == "yes":                       #leap_year.lower() is used to make it case-insensitive
            print("February has 29 days in a leap year.")    #if else statement is used to check if it's a leap year or not
        else:
            print("February has 28 days in a non-leap year.")
    else:
        print(f"The month has {days_in_a_month[month]} days.")   #output for other months
else:
    print("Invalid month number! Enter a number between 1 and 12.")   #outputs if the user doesn't enter the correct answer
