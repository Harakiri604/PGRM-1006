# Integer
integer=5

# Float
floater=0.5

# String
stringy="string"

# Boolean
booboolean=True

# List/Array
my_list=["awe", "boo", "booboo"]
my_list2=[1, 2, 3, 4, 5]

# Get date type
print(type(integer))
print(type(floater))
print(type(stringy))
print(type(booboolean))
print(type(my_list))

#try combining them
answer1=integer+floater
print(answer1)

answer2=stringy+"ss"
print(answer2)

#Conditional with 2 numbers
if integer<floater:
    print("We are awesome")
else:
    print("We are not so awesome")

#Loop through a range() object
for i in range(10):
    print(i)
    
#Add a conditional statement inside a loop
for i in range(10):
    if i < 5:
        print(i)
    else:
        print("more than 5")

#While loop with counter
while integer>1:
    print (integer)
    integer -=1

#Print each character in a string  
def printStr(stringy2):
    for char in stringy2:
        print(char)

printStr("Amir")

#Use enumerate using unpacking - *
x = [10, 324, 46, 234, -92]
print(*enumerate(x))

#Use enumerate using "for"
for index, value in enumerate(x):
    print(index)
    print(value)

#Use enumerate to modify list
for index, value in enumerate(my_list):
    my_list[index] += "ss"
    
print(my_list)

#Function example
def averageVal(someList):
    total = 0
    for ele in someList:
        total += ele
    return total/len(someList)

print(averageVal(my_list2))
    

