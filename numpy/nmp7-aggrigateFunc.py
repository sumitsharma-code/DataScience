import numpy as np

# Aggrigate funcitons = summarize data
#              and typically return
#              single value

array = np.array(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
    ]
)

print(np.sum(array))
print(np.mean(array)) # average
print(np.std(array)) # standard deviation
print(np.var(array)) # variance = (std)^2
print(np.min(array)) # 1
print(np.max(array)) # 10
print(np.argmin(array)) # 0 - index of the min val
print(np.argmax(array)) # 9 - index of the max val

# suming cols
print(np.sum(array, axis=0)) # [ 7  9 11 13 15]
# suming rows
print(np.sum(array, axis=1)) # [15 40]