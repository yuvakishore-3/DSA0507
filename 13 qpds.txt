import pandas as pd
data = {
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, None, 5],
    'C': [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)
missing_values = df.isna()
print(missing_values)
