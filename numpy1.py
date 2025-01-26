import numpy as np
print(np.__version__)
a = np.array([1,2,3,4,5])
print(a)
print(len(a))
print(type(a))
print(type(type(a)))
print(a.dtype)
print(a.ndim)               #represents no of array dimensions or rank of array
print(a.shape)              #is a tuple represents size of array in each dimensions
print(a[1])
a[2]=31

print(a[1:4])
a[3:5] = 8, 6



#/////////////////////  VECTOR:

u = [1, 0]
v = [0, 1]
z = []
for n, m in zip(u, v):
    z.append(n + m)
print(z)

u1 = np.array([1, 0])           # only one line is required for vector addition
v1 = np.array([0, 1])
z1 = []

z1 = u1 + v1
z1 = np.add(u1, v1)
print(z1)


u1 = np.array([1, 2])           # only one line is required for vector addition
v1 = np.array([3, 1])
z1 = []
z2 = []
z3 = []
z4 = []

z1 = u1 + v1
z2 = u1 - v1
z3 = u1 * v1                    # HADAMARD PRODUCT
z4 = np.dot(u1,v1)              # DOT PRODUCT

print(z1, "\n\n", z2, "\n\n", z3, "\n\n", z4, "\n\n", 2*u1)

#///////    UNIVERSAL FUNCTIONS:
print(a.max())
print(a.min())
print(a.mean())

print(np.pi)
a=np.pi
print(np.sin(a))
print(np.sin(np.pi/2))
print(np.sin(0))

print(np.linspace(-2, 2, num=6))            #// generates num line/ equal spaces, starts with -2 & ends with 2


#/////
a = np.array([100, 200, 300, 400, 500, 600, 700])
i = [0, 2, 4, 5]
print(a[i])
print(a.std())



#/////////////////  2D ARRAY
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = np.array(l)
a

a.ndim
a.size
a.shape

a[0, 2]
a[0][2]
a[1, 1:3]
a[1][1:3]
a[0:2, 2]

b = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
a+b
b1 = np.array([[1, 2, 1], [1, 2, 1], [1, 2, 1]])
a*b1                #multiply by another matrix (HARAMARD PRODUCT)
a*5                 #multiply by scalar value 2

np.dot(a, b1)

b2 = np.array([[2, 3, 4], [4, 3, 2]])
a2 = np.array([[ 3, 4], [4, 3], [2, 4]])
a2 * b2
np.dot(a2, b2)

np.sin(b1)

#///    TRANSPOSE OF MATRIX/ ARRAY

a2.T
a.T

X=np.array([[1,0],[0,1]])
Y=np.array([[2,2],[2,2]])
Z=np.dot(X,Y)
Z


