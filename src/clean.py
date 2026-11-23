
import pandas as pd
from pathlib import Path

def clean_data(df):

    BASE_DIR = Path(__file__).resolve().parents[1]

    print("Original rows:", len(df))

    # 1. Fill missing customer names
    df["customer_name"] = df["customer_name"].fillna("Unknown")

    # 2. Remove missing quantity
    df = df.dropna(subset=["quantity"])

    # 3. Remove negative prices
    df = df[df["unit_price"] >= 0]

    # 4. Calculate total sales
    df["total_sales"] = df["quantity"] * df["unit_price"]

    # 5. Save cleaned data
    output_path = BASE_DIR / "data" / "processed" / "cleaned_sales.csv"
    df.to_csv(output_path, index=False)

    # DATA ANALYSIS
    print("\n--- TOTAL REVENUE ---")
    print(df["total_sales"].sum())

    print("\n--- PRODUCT-WISE REVENUE ---")
    print(df.groupby("product")["total_sales"].sum())

    print("\n--- PRODUCT-WISE QUANTITY ---")
    print(df.groupby("product")["quantity"].sum())

    print("\n--- AVERAGE ORDER VALUE ---")
    print(df["total_sales"].mean())

    print("\nCleaning completed successfully!")
    print("Remaining rows:", len(df))

    return df