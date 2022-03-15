import numpy as np

arr = np.arange(0, 11)
sum_of_arrays = arr + arr
sub_of_arrays = arr - arr
mult_of_arrays = arr * arr
power_of_arrays = arr ** 2
print(arr + 100)
print(arr * 100)
print(arr - 100)
print(arr / 100)
print(arr / arr)
print(1 / arr)

#---Universal array functions---
print(np.sqrt(arr))
print(np.exp(arr))
print(np.max(arr))
print(np.sin(arr))
print(np.log(arr))
