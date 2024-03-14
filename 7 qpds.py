import pandas as pd

# Sample sales data (replace this with your actual sales data)
sales_data = {
    'Item': ['A', 'B', 'A', 'C', 'B', 'C'],
    'Units_Sold': [10, 20, 15, 30, 25, 20]
}

# Create DataFrame from sales data
df = pd.DataFrame(sales_data)

# Create pivot table to find item-wise unit sold
pivot_table = pd.pivot_table(df, values='Units_Sold', index='Item', aggfunc='sum')

# Display the pivot table
print("Pivot Table - Item wise unit sold:")
print(pivot_table)
