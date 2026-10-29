import numpy as np

rng = np.random.default_rng()

# print(rng.integers(low = 1,high = 7,size=(3, 2)))

# print(np.random.uniform(low = -1, high = 1, size = (3, 2)))

# shuffle

# array = np.array([1, 2, 3, 4, 5])
# rng.shuffle(array)

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])
fruits = rng.choice(fruits, size = (3, 2))
print(fruits)
