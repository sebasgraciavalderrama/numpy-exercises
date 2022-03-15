import numpy as np

arr = np.arange(0, 11)

print(arr[8])
print(arr[1:5])
print(arr[0:5])
print(arr[:6])
print(arr[5:])
arr[0:5] = 100
print(arr)
arr = np.arange(0, 11)
slice_of_arr = arr[0:6]
print(slice_of_arr)
print(slice_of_arr[:])
slice_of_arr[:] = 99
print(slice_of_arr)
print(arr)
arr_copy = arr.copy()
print(arr_copy)
arr_copy[:] = 100
print(arr_copy)
print(arr)