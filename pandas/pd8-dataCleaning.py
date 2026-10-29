import pandas as pd

df = pd.read_csv("pokemon.csv")


# 1. Dropping irrelivant columns
# df = df.drop(columns=["Legendary", "Speed"])

# 2. Handle missing data
# df = df.dropna(subset=["Type 2"]) # drop any rows that are missing a value in `Type 2`
# df = df.fillna({"Type 2": "None"}) # filling any not available value

# 3. Fix inconsistent values
# df["Type 1"] = df["Type 1"].replace({
#                             "Grass": "GRASS",
#                             "Water": "WATER"
#                             })

# 4. Standardize Text
# df["Name"] = df["Name"].str.lower()

# 5. Fix Data Type
# df["Legendary"] = df["Legendary"].astype(int)

# 6. Remove Duplicate Values
df = df.drop_duplicates()

print(df.to_string())