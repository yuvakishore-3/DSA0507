import pandas as pd
import numpy as np
data = {
    'A': [1, np.nan, 3, np.nan, 5],
    'B': [np.nan, 'hello', np.nan, 'world', np.nan],
    'C': [np.nan, np.nan, np.nan, np.nan, np.nan]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df_filled = df.fillna('N/A')
print("\nDataFrame after replacing missing values:")
print(df_filled)
