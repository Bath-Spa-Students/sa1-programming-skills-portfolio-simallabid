# Exercise 5: Days of the Month - 30 Marks

'''Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.'''

days_in_a_month = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 31,
    5 : 30,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31 
    }        #dictionary with month numbers and number of days in those months

try:                                                           #using try execpt that handles potential errors
    month_num = int(input('Enter the month number (1-12): '))  #takes input from the user
    
    if 1 <= month_num <= 12:                                   #using the if statement
        print(f'The number of days in month {month_num} are {days_in_a_month[month_num]} ')
    else:
        print('Please enter a number from 1-12.')
except:
    print('Invalid answer! Enter a valid number.')