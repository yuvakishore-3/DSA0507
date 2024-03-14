import pandas as pd
import numpy as np
np.random.seed(0)  # for reproducibility
data = np.random.randn(10, 4)  # 10 rows, 4 columns of random values
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
df.iloc[2, 0] = np.nan  # Setting a value in row 2, column 0 to NaN
df.iloc[5, 2] = np.nan  # Setting a value in row 5, column 2 to NaN
def highlight_nan(val):
    """
    Takes a scalar and returns a string with
    the CSS property `'color: red'` for NaN values.
    """
    if pd.isna(val):
        return 'color: red'
    else:
        return ''
styled_df = df.style.applymap(highlight_nan)
styled_df
