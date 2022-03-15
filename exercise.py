import numpy as np

my_list = [1,2,3]
arr = np.array(my_list)
print(arr)

my_mat = [[1,2,3], [4,5,6], [7,8,9]]

print(np.array(my_mat))

print(np.arange(0,11,2))

print(np.zeros(3))
print(np.zeros((2,3)))

print(np.ones(1))
print(np.ones((3, 4)))

print(np.linspace(0, 5, 10))
print(np.linspace(0, 5, 100))

print(np.eye(4))

print(np.random.rand(5, 5))

print(np.random.randn(4,4))

print(np.random.randint(1, 100, 10))

arr = np.arange(25)
print(arr)
ranarr = np.random.randint(0, 50, 10)
print(ranarr)
arr.reshape(5, 5)
print(arr)

print(ranarr.max())
print(ranarr.min())
print(ranarr.argmax())
print(ranarr.argmin())
print(ranarr.shape)
arr = arr.reshape(5, 5)
print(arr.shape)
print(arr.dtype)

from numpy.random import randint
print(randint(2,10))