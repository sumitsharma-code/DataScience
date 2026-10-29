import numpy as np
array = np.array([
    [
        ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']
    ],
    [
        ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']
    ],
    [
        ['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '0']
    ]
])

print(array.ndim)

print(array.shape) # (3, 3, 3) (depth, rows, cols)

print(array[1, 1, 2])

word = array[0, 2, 1] + array[0, 1, 1] + array[2, 2, 0]

print(word) # HEY