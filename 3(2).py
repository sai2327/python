import numpy as np

arr = np.array([10, 25, 30, 15, 5, 60, 45])

num = 20
less_than_num = arr[arr < num]
greater_than_num = arr[arr > num]
print(type(less_than_num))
print("Numbers less than", num, ":", less_than_num)
print("Numbers greater than", num, ":", greater_than_num)

print("Index of max:", np.argmax(arr))
print("Index of min:", np.argmin(arr))

print("Max value:", np.max(arr))
print("Min value:", np.min(arr))
print("Repr:", np.array_repr(arr))
print("Count of 25:", np.count_nonzero(arr == 25))
print("Unique values:", np.unique(arr))
