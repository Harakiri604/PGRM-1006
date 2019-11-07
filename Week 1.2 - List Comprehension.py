'''
Create a list using comprehension:
    - State how you want each element to be created
    - Then use for loop to create each as many times as you need
'''

x = [str(i)+"ss" for i in range (50,100,2)]

print(x)

#You can use conditional

y = [str(i)+" is even" for i in range (100) if i % 2 == 0]

print(y)

#Function for use in comprehension

def addFive(xx):
    return xx + 5

z = [addFive(val) for val in range (100)]
print(z)


