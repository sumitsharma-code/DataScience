# if statements - execute some code only if a certain condition is true
#                 basic decision making in programming
#                 (if, elif, else)

age = int(input("Enter your age: "))


if(age >= 18):
    print("You are eligible to vote.")
elif (age < 0):
    print("You are not born yet.")
elif (age == 0):
    print("You are a newborn baby.")
else:
    print("You are not eligible to vote.")
    

has_ticket = True

if has_ticket:
    print("You can enter the stadium.")
else:
    print("You cannot enter the stadium.")