import numpy as np

arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])
print(arr_2d)
#------Double bracket notation------
print(arr_2d[0][0])
print(arr_2d[0])
print(arr_2d[1][1])
print(arr_2d[1][2])
#------Comma notation------
print(arr_2d[2,1])
print(arr_2d[1,2])
#------Chunks of the array------
print(arr_2d[:2,1:])
print(arr_2d[1:, ])
#------Conditional selection-------
new_arr = np.arange(1,11)
bool_arr = new_arr > 5
print(new_arr[bool_arr])
print(new_arr[new_arr > 5])
print(new_arr[new_arr < 3])
#-----Exercise------
arr_exe = np.arange(50).reshape(5, 10)
print(arr_exe[1:3, 3:5])
