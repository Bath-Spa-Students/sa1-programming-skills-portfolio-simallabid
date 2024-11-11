''' Exercise 3: Biography - 25 Marks

In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.'''

info={
    'Name' : 'Simal',
      'Hometown' : 'Sharjah',
      'Age' : 18
      }                           #a dictionary that contains all the information
print (f"Name: {info['Name']} \nHometown: {info['Hometown']} \nAge: {info['Age']}")  #the f-string is used to allow the values to me embedded within the string.