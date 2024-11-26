import numpy as np
# import time
# import sys

# s = range(1000)
# print(type(s))
# print(sys.getsizeof(s)*len(s))
# d = np.arange(1000)
# print(type(d))
# print(d.size*d.itemsize)

# arr = np.array([[1,2,3],[1,2,3]])

# print(arr)
# print(type(arr))

# arr = np.array([[1,2,3],[1,2,3]])
# print(arr.flags)

# arr = np.array([[1,3],[3,4],[1,2]],dtype=complex)

# print(arr)

# arr = np.zeros(10,dtype=int)
# arr = np.ones((3,4),dtype=int)
# arr = np.full((3,4),345)
# arr = np.arange(0,21,2)
# arr = np.linspace(1,1000,10,dtype=int)
# arr = np.random.random((3,3))  

# arr = np.random.normal(1,3,(3,2))            
# arr = np.random.normal(1,3,(3,2))            
# arr = np.random.randint(1,10,(3,5))            
# arr = np.eye(10)   
# arr = np.empty(5,dtype=int)         
# print(arr)

# x = [[1,2,3],[7,8,9],[1,3,6]]
# print(type(x))
# a = np.asarray(x)
# print(type(a))
# print(a)

# x = np.array([[10,20],[30,40]])
# print(x)
# m = np.asmatrix(x)
# m[0,0] = 50
# print(m)

# x = b'HELLO PYTHON'
# print(type(x))

# a = np.frombuffer(x,dtype="S1",count=5,offset=5)
# print(a)
# print(type(a))

# f = range(10)
# g = iter(f)
# x = np.fromiter(g,dtype=int)

# print(x)

# x = np.array([1,2,3]) #[1,2,3]
# y = x                 #[1,2,3]  
# z = np.copy(x)        #[1,5,3]

# z[1] = 5

# print(x==y)
# print(y==z)
# print(z==x)

# a = np.arange(10,31,3,int)
# print(a)

# a = np.linspace(1,1,5,endpoint=True)
# print(a)