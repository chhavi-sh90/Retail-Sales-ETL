import pandas as pd
from pathlib import Path

def extract_data():

    # Get project root directory
    BASE_DIR = Path(__file__).resolve().parents[1]

    # CSV file path
    file_path = BASE_DIR / "data" / "raw" / "sales.csv"

    # Read CSV file
    df = pd.read_csv(file_path)

    print("\n--- FIRST 5 ROWS ---")
    print(df.head())

    print("\nData extracted successfully!")

    return df