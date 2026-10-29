import pandas as pd

df = pd.read_csv("pokemon.csv")

data = df[df["Legendary"] == True]
water_poke = df[
    (df["Type 1"] == "Water") |
    (df["Type 2"] == "Water")
]
print(water_poke)