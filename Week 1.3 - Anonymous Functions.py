# Lambda function syntax - lambda x,y,z: x+y+z
#Sum function
x = lambda a,b:a+b
print(x(2,3))
print(x(3,5))

#Power function
y = lambda a:a**2
print(y(2))

#List comprehension
z = lambda a:a**2
a = [z(y) for y in range (20)]
print(a)