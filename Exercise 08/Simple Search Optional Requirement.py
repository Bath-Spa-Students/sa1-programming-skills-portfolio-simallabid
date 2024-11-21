''' Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.'''

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]          #list of names

while True:                                                   #using while loop to check if user input is present
    name_search = input("Enter a name: ")                     #initializing a variable to take input from user
    
    if name_search.lower() == "exit":                         #using if statement, using '.lower()' to make it case-insensitive
        print("Thank you for using the search program!")
        break                                                 #using break statement to stop the loop 
   
    if name_search in names:                                  #if statement to check if the user input is present in list 
        print(f"'{name_search}' is in the list.")             #using the f-string for correct and neat output
    else:                                                     
        print(f"'{name_search}' is not in the list.")
        
