import pandas as pd

df = pd.read_csv("pokemon.csv", index_col="Name")

# SELECTION BY COLUMN
# print(df["Name"].to_string())
# print(df[["Speed", "Name"]])


# SELECTION BY ROW
# print(df.loc["Pikachu"])
# print(df.loc["Charizard", ["Speed", "HP"]])


# Exercise
pokemon = input("Enter a pokemon name: ")

data = df.loc[pokemon]

print(data)