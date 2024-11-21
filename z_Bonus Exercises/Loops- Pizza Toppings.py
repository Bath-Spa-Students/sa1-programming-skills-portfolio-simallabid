'''Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza.'''

while True:                                                           #using while loop to get answers until the user types quit
    toppings = input('Enter a pizza topping. (type quit to end)')
    
    if toppings.lower() == 'quit':                                    #using if else statement to end the program once the user types quit or to continue it if the user enters a topping
        print('Finished adding your toppings!')
        break                                                         #ends the program
        
    else:
        print(f"We have added {toppings} to your pizza!")