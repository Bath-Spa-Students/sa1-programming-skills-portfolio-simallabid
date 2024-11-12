'''# Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.'''

a = input("What is the capital of France? ")    #takes the input from the user
if a.lower()=='paris':                          #accepts answers regardless of the capotalization
    print('Correct Answer!')
    
else:                                           
    print("Incorrect Answer!")                  #output if the answer is incorrect.
    