'''# Exercise 10: Is it even? - 35 Marks

Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.'''

def check_even_odd(number):                               #checks if the entered number is even or odd
    if number % 2 == 0:                                   #using the if else statement
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

def main():
    number = int(input("Please enter a number: "))       #takes the input from user
    
    result = check_even_odd(number)                      #result returned by the function
    
    print(result)                                        #prints result         

if __name__ == "__main__":                               #makes sure that the function runs only when the script is executed
    main() 
