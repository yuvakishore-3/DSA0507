import pandas as pd
import numpy as np
data = {
    'A': [1, 2, None, 4, 5],
    'B': [None, None, None, None, None],
    'C': [1, 2, 3, None, 5]
}
df = pd.DataFrame(data)
df_with_nan = df.dropna(thresh=2)
print(df_with_nan)
