# while loop = used to repeat a block of code as long as a condition is true
#              - useful when you don't know beforehand how many times you need to repeat something

name = input("What is your name? ")


while(name == ""):
    print("Please enter your name.")
    name = input("What is your name? ")
    
age = int(input("What is your age? "))

while(age < 0):
    print("Please enter a valid age.")
    age = int(input("What is your age? "))

print(f"Hello {name}!")
print(f"You are {age} years old!")