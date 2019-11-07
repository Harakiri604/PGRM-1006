'''
Task 1 - PRINT EVEN FUNCTION
Define a function with an argument called "limit". 
The function creates a list called "user_array" using "limit" as the stop variable. 
Combine it with conditional if statement to only add even numbers to the list
'''

def printEven(limit):
    user_array = [i for i in range (limit) if i%2==0]
    print(user_array)

'''
Call this function using user input, which we need to declare as an integer
'''

userInput=input("Chose a positive integer: ")
userInput=int(userInput)
printEven(userInput)

'''
Task 2 - RETURN EVEN LIST FUNCTION
Same as task 1 except instead of printing the list, we simply return it
'''

def listEven(limit):
    user_array = [i for i in range (limit) if i%2==0]
    return user_array

userInput2=input("Chose a positive integer: ")
userInput2=int(userInput2)

'''
Task 3 -  ONE LINE CREATE LIST FUNCTION
Define a list called "oneLineList" using list comprehension.
The stop variable in the list comprehension is an integer of a user input
We add 1 since the stop variable is exclusive
'''

oneLineList = [i for i in range((1+int(input("Chose a positive integer: "))))]

'''
Task 4 - LAMBDA CREATE LIST FUNCTION
Same as task 4 except using lambda and testing it by printing it
'''
y=lambda a: [a for a in range((1+int(a)))]
print(y(150))

'''
Task 5 - SLICEME FUNCTION
Create a variable called userString based on user input
Create a string called everyOther which slices out every second letter from userString
Print to see if it works
'''

userString = input("Type in a word to see its every other letter: ")
everyOther = userString[::2]
print(everyOther)

