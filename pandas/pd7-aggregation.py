import pandas as pd

df = pd.read_csv("pokemon.csv")


# Whole column
# print(df.mean(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.count())

# Single column
# print(df["Attack"].mean())
# print(df["Attack"].min())
# print(df["Attack"].max())
# print(df["Attack"].sum())
# print(df["Attack"].count())


# Grouping
group = df.groupby("Type 1")

# print(group["Defense"].mean())
# print(group["Defense"].sum())
# print(group["Defense"].min())
# print(group["Defense"].max())
# print(group["Defense"].count())

# print(group)