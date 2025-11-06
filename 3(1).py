import numpy as np

# 3.1
help(np.add)

arr = np.array([1, 2, 3, 4, 5])
print(np.all(arr))

x = np.array([1.0000001, 2, 2, 5])
y = np.array([1.0000002, 2, 2, 5])

print(np.greater(x, y))
print(np.greater_equal(x, y))
print(np.less(x, y))
print(np.less_equal(x, y))
print(np.equal(x, y))
print(np.allclose(x, y))
