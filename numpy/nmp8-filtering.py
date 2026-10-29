import numpy as np

# filtering = selecting elements from array
#               that match a given condition

ages = np.array(
    [
        [21, 17, 19, 20, 16, 30, 18, 65],
        [39, 22, 15, 99, 18, 19, 20, 21]
    ]
)

teens = ages[ages < 18]

# adults = ages[(ages >= 18) & (ages <= 65)]

dependent = ages[(ages < 18) | (ages >= 65)]

evens = ages[ages % 2 == 0]

odds = ages[ages % 2 == 1]

# Where function

matured = np.where(
    ages >= 18,
    ages,
    0
)

# where is slower and only be used when
# we want to preserve the shape

print(matured)