# logical operators - evaluate multiple conditions
#                   - return a boolean value
#                   - and = both conditions must be true
#                   - or = at least one condition must be true
#                   - not = negates the condition


# OR
# temperature = 25
# is_raining = False

# if temperature > 35 or temperature < 0 or is_raining:
#     print("The outdoor activities are cancelled.")
# else:
#     print("The outdoor activities are on.")

# --------------------------------------------
# AND
temperature = 25
is_sunny = True

if temperature > 35 and is_sunny:
    print("It is HOT and sunny outside.")
elif temperature <= 0 and is_sunny:
    print("It is COLD and sunny outside.")

# --------------------------------------------
# NOT
