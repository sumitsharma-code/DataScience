import pandas as pd

# DataFrames = A tabular data structure
#              with rows And columns. (2D)
#              Similar to an Excel spreadsheet

data = {
    "Name": ["Spongebob", "Patric", "Squidward"],
    "Age" : [30, 35, 50]
}

df = pd.DataFrame(data, index = ["employee 1", "employee 2", "employee 3"])

# print(df)

# print(df.loc["employee 1"])
# print(df.iloc[0])


# add a new Column
df["Job"] = ["Cook", "N/A", "Cashier"]

print(df)


# # add a new Row
# new_row = pd.DataFrame([{
#     "Name": "Sandy",
#     "Age" : 28,
#     "Job" : "Engineer"
# }], index = ["employee 4"])

# df = pd.concat([df, new_row])

# print(df)
