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

# x = np.array([1,2,3,4,5,6,7,8,9])
# x = np.array([[1,2,3],[4,5,6],[7,8,9]])
# x = np.array([10,32,37,23,19,12,6])

# g = x <= 18 # 1 < 2 = T, 2 < 2 = F , 3 < 2 = F

# print(g)

# print(x[x >= 18])

# print(x[0,0],x[1,2],x[2,0])

# print(x[1:,1:])

# print(x[2])

# print(x[3:6:2]) # strat

# C1 = np.array([10,32,37,23,19,12,16,12,16,12])

# newarr = np.array_split(C1,4)

# print(newarr)

# C2 = np.array([10,32,37,23,19,12,16])
# C3 = np.array([10,32,37,23,19,12,16])

# arr = np.concatenate((C1,C2,C3))

# print(arr)

# x1 = np.array([1,2,3])
# x2 = np.array([1,2,3])

# print(x1 + x2)
# print(x1 * x2)
# print(x1 / x2)
# print(x1 - x2)