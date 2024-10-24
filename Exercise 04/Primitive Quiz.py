#Exercise 4: Primitive Quiz - 30 Marks

'''In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.'''

a = input('What is the capital of France? ') #using input to take answer from the user and store it in the variable 'a'
if a == 'Paris':                             #using control structure (if-else)
    print('The answer is correct')           #will be printed if the user answers the question correctly
else:
    print('The answer is wrong')             #will be printed if the user gives an incorrect answer