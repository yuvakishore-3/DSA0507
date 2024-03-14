import pandas as pd
sales_data = {
    'Item': ['A', 'B', 'A', 'C', 'B', 'C'],
    'Units_Sold': [10, 20, 15, 30, 25, 20]
}
df = pd.DataFrame(sales_data)
pivot_table = pd.pivot_table(df, values='Units_Sold', index='Item', aggfunc='sum')
print("Pivot Table - Item wise unit sold:")
print(pivot_table)
