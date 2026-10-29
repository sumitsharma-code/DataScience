import pandas as pd

# Series = A pandas 1-D labled Array
#          Like a single col in sheet

# data = [100, 102, 104]

# series = pd.Series(data, index=["a", "b","c"])

# series.loc["b"] = 13

# series.iloc[0] = 1

# data = [100, 102, 104, 200, 202]

# series = pd.Series(data, index=["a", "b","c","d","e"])


# print(series[series > 200])


calories = {
    "Day 1": 1750,
    "Day 2": 2100,
    "Day 3": 1700
}

series = pd.Series(calories)

print(series[series >= 2000])

