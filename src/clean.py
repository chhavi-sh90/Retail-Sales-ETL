
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

# Read raw data
file_path = BASE_DIR / "data" / "raw" / "sales.csv"
df = pd.read_csv(file_path)

print("Original rows:", len(df))

# 1. Fill missing customer names
df["customer_name"] = df["customer_name"].fillna("Unknown")

# 2. Remove rows with missing quantity
df = df.dropna(subset=["quantity"])

# 3. Remove negative prices
df = df[df["unit_price"] >= 0]

# 4. Save cleaned data
output_path = BASE_DIR / "data" / "processed" / "cleaned_sales.csv"

# Calculate total sales
df["total_sales"] = df["quantity"] * df["unit_price"]

print("\n--- TOTAL SALES ---")
print(df[["order_id", "product", "total_sales"]])


# --------------------------------
# DATA ANALYSIS
# --------------------------------

# 1. Total Revenue
total_revenue = df["total_sales"].sum()

print("\n--- TOTAL REVENUE ---")
print(total_revenue)


# 2. Product-wise Revenue
product_sales = df.groupby("product")["total_sales"].sum()

print("\n--- PRODUCT-WISE REVENUE ---")
print(product_sales)


# 3. Total Quantity Sold
product_quantity = df.groupby("product")["quantity"].sum()

print("\n--- PRODUCT-WISE QUANTITY ---")
print(product_quantity)


# 4. Average Order Value
average_order = df["total_sales"].mean()

print("\n--- AVERAGE ORDER VALUE ---")
print(average_order)


# Save processed data
df.to_csv(output_path, index=False)

print("\nAnalysis completed successfully!")


df.to_csv(output_path, index=False)

df.to_csv(output_path, index=False)

print("\n--- CLEANED DATA ---")
print(df)

print("\nRemaining rows:", len(df))
print("Cleaning completed successfully!")
