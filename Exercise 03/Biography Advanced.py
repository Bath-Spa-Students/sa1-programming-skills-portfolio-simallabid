'''Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?'''


Name = input('Enter name: ')             #takes input from user (name)
Hometown = input('Enter hometown: ')     #takes input from user (hometown)

while True:                             #using while loop to ensure a correct answer
    try: 
        Age = int(input("Enter age: ")) 
        break                           #using break statement to end the while loop once the user has entered a correct answer
    except ValueError:
        print("Please enter a valid integer for age.") 

info ={                                    
    'Name' : Name,
    'Hometown' : Hometown,
    'Age' : Age
}                                     #dictionary that stores the info

print(f"Name: {info['Name']} \nHometown: {info['Hometown']} \nAge {info['Age']}") #prints the information