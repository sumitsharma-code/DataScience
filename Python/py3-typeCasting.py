# typecasting - converting a variable from one type to another
                # str(), int(), float(), bool()


name = "Sumit Sharma" # string
age = 22 # integer
gpa = 7.94 # float
is_student = False # boolean

gpa = int(gpa) # typecasting float to integer
print(f"My gpa is {gpa} and my age is {age}.") # gpa will be 7 now

print(type(gpa)) # type of gpa will be <class 'int'>
print(type(type(gpa))) # type of the type of gpa will be <class 'type'>