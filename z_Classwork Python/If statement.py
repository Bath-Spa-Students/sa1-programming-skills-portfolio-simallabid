#if statement
a= 4
b= 6

if b>a:
    print("b is greater than a")


#if else statement   
c= 4+2
d= 4+2

if c>d:
    print("c is greater than d")
else:
    print("d is greater than c")
    

#flowchart 1
sales= int(input("Enter the total sales: "))
if sales>50000:
    print("bonus is 500")
#else:
    #print("no bonus")
    


#flowchart 2
temp= int(input("enter the temperature: "))
if temp<40:
    print("A little cold, isn't it?")
else:
    print("Nice weather we're having")


#nested if statement
salary= int(input('What is your salary?'))
if salary>=30000:
    years_on_job = float(input('Enter the year of experience: '))
    if years_on_job>=2:
        print('You qualify for the loan!')
    else:
        print('You must have atleast two years of experience.')
else:
    print('You must earn atleast $30,000 per year to qualify.')

#elif statement
a = 'monday'
b = 'tuesday'
c = 'wednesday'
d = 'thursday'
e = 'friday'
f = 'saturday'
g = 'sunday'

print("""a = monday
b = tuesday
c = wednesday
d = thursday
e = friday
f = saturday
g = sunday""")

day= input("What is the day today? (a , b , c , d , e , f , g )")

if day== 'a' :
    print("Its monday today")
elif day== 'b':
    print("its tuesday today")
elif day== 'c':
    print("its wednesday today")
elif day== 'd':
    print("its thursday today")
elif day== 'e':
    print("its friday today")
elif day== 'f':
    print("its saturday today")    
elif day== 'g':
    print("its sunday today")
else:
    print("please enter a valid anwer.")
    
#flowchart3
score=int(input('enter your score:'))
if score>=90:
    print('your grade is A')
elif score>=80:
    print('your grade is B')
elif score>=70:
    print('your grade is C')
elif score>=60:
    print('your grade is D')
else:
    print('your grade is F')
    