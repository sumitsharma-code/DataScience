import numpy as np

# ==================================

# Scalar arithmetic

array = np.array([1, 2, 3])

# print(array + 1) # each value added 1
# print(array - 2)
# print(array * 3)
# print(array / 4)
# print(array ** 2)

# ==================================

# Vectorized math functions

array = np.array([1.01, 2.5, 3.99])

# print(np.sqrt(array))
# print(np.round(array))
# print(np.floor(array))
# print(np.ceil(array))
# print(np.pi)


# TASK - convert radii -> Area of circle

radii = np.array([1, 2, 3])

# print(np.pi * (radii**2)) # areas of circles

# ==================================

# Element-wise arithmetic

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# print(array1 + array2) #[5 7 9]
# print(array1 - array2) 
# print(array1 * array2) 
# print(array1 / array2) 
# print(array1 ** array2) 

# ==================================

# Comparison Operators

scores = np.array([91, 55, 100, 73, 82, 64])

# print(scores == 100) # [False False  True False False False]
# print(scores >= 60)

scores[scores < 60] = 0

print(scores)