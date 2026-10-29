import numpy as np

array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# array[row_start:row_ending:step, col_start:col_ending:step]

print(array[2:, 2:])