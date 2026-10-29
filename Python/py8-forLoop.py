# for loop = used to iterate over a sequence (list, tuple, string)
#           - repeats a block of code for each item in a sequence
#           - useful when you know number of iterations in advance

for i in range(10, 44, 10):
    print(i) # prints numbers from 10 to 43 with a step of 10
    
name = "SumitSharma"

for char in name:
    print(char, end="-") # prints each character in the string