import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alphabet_stock_prices.csv')
df['Date'] = pd.to_datetime(df['Date'])
start_date = '2022-01-01'  
end_date = '2022-12-31'    
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
plt.figure(figsize=(10, 6))
plt.plot(filtered_df['Date'], filtered_df['Close'], marker='o', linestyle='-')
plt.title('Historical Stock Prices of Alphabet Inc. (Google)')
plt.xlabel('Date')
plt.ylabel('Closing Price ($)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
