import pandas as pd

df = pd.read_csv("pokemon.csv")
# For JSON
# df = pd.read_json("data.json")

print(df.to_string())