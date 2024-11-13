'''Multiple Questions:
Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question'''

score=0                                         #initializing score variable
ans1=input("What is the capital of Russia?")    #takes input from user
if ans1.lower()=='moscow':                      #ans1.lower() ignores the case sensitivity
    print("Correct!")                           #if statement to check if he answer is correct
    score+=1                                    #increment in score if the answer is correct
else:
    print("Incorrect answer!")
    print("your score is", score)               #shows the total score once you answer the question incorrectly
    
ans2=input("What is the capital of Germany?")   #asking for the capital of germany
if ans2.lower()=='berlin':
    print("Correct!")
    score+=1
else:
    print("Incorrect answer!")
    print("your score is", score)
    
ans3=input("What is the capital of United Kingdom?")  #asking for the capital of united kingdom
if ans3.lower()=='london':
    print("Correct!")
    score+=1
else:
    print("Incorrect answer!")
    print("your score is", score)
    
ans4=input("What is the capital of Italy?")          #asking for the capital of italy
if ans4.lower()=='rome':
    print("Correct!")
    score+=1
else:
    print("Incorrect answer!")
    print("your score is", score)
    
ans5=input("What is the capital of Spain?")          #asking for the capital of spain
if ans5.lower()=='madrid':
    print("Correct!")
    score+=1
else:
    print("Incorrect answer!")
    print("your score is", score)

ans6=input("What is the capital of Poland?")         #asking for the capital of poland
if ans6.lower()=='warsaw':
    print("Correct!")
    score+=1
else:
    print("Incorrect answer!")
    print("your score is", score)
    
ans7=input("What is the capital of Ukraine?")        #asking for the capital of ukraine
if ans7.lower()=='kyiv':
    print("Correct!")
    score+=1
else:
    print("Incorrect answer!")
    print("your score is", score)
    
ans8=input("What is the capital of Netherlands?")    #asking for the capital of netherlands
if ans8.lower()=='amsterdam':
    print("Correct!")
    score+=1
else:
    print("Incorrect answer!")
    print("your score is", score)
    
ans9=input("What is the capital of Romania?")        #asking for the capital of romania
if ans9.lower()=='bucharest':
    print("Correct!")
    score+=1
else:
    print("Incorrect answer!")
    print("your score is", score)
    
ans10=input("What is the capital of Switzerland?")   #asking for the capital of switzerland
if ans10.lower()=='bern':
    print("Correct!")
    score+=1
    print("your score is", score)                    #displays the total score if you answer all the questions correctly
else:
    print("Incorrect answer!")
    print("your score is", score)