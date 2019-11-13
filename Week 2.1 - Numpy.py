import numpy as np

#Numpy can create ranges in float steps, e.g. 0.5
x = range(0,101,1)
y = np.arange(-100,100,0.5)
print(y)

#Reshaping the array into a matrix 
print(y.shape)
z = y.reshape((40,10))
print(z)
print(z.shape)

#Creating a matrix of 0s or 1s
zeros = np.zeros((10,20))
print(zeros)
print(zeros.shape)

ones = np.ones((10,20))
print(ones)
print(ones.shape)

#Reshaping said matrix
shapeOnes = (ones.reshape(5,40))
print(shapeOnes.shape)

#Converting a list into a numpy array
myList = [1,2,3,4,5]
print(type(myList))
myNpList = np.array(myList)
print(type(myNpList))

z1 = "Hello World"
NpZ=np.array(z1)

#Creating an evenly spaced array
x1 = np.linspace(0,10,50)
print(x1)

#Doing math functions on arrays
sins=np.sin(x)
cosins=np.cos(sins)
print(cosins)

#Creating conditional statement arrays
boolArray = sins < 0
print(boolArray)

#Creating random arrays and reshaping them
x2 = np.random.random(20)
print(x2)

y2 = x2.reshape((5,4))
print(y2)

#Random integer
x3 = np.random.randint(0,100,20)
print(x3)

y3 = x3.reshape((10,2))
print(y3)

#Transpose it
y3T = y3.T
print(y3T)

#Max or Min
print(y3T.max())
print(y3T.min())

#Sum by row
print(y3T.sum(axis=0))
#Sum by column
print(y3T.sum(axis=1))