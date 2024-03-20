import pandas as pd
data = {
    'Column': ['apple', 'banana', 'orange', 'grape', 'watermelon']
}
df = pd.DataFrame(data)
substring = 'an'
indices = df[df['Column'].str.contains(substring)].index
print("Indices of rows containing the substring:", indices)
