
import pandas as pd
from pathlib import Path

# Get project root directory
BASE_DIR = Path(__file__).resolve().parents[1]

# CSV file path
file_path = BASE_DIR / "data" / "raw" / "sales.csv"

# Read CSV file
df = pd.read_csv(file_path)

# Display first 5 rows
print("\n--- FIRST 5 ROWS ---")
print(df.head())

# Display total rows and columns
print("\n--- DATA SHAPE ---")
print(df.shape)

# Display column names
print("\n--- COLUMN NAMES ---")
print(df.columns)

# Display data information
print("\n--- DATA INFO ---")
df.info()

print("\nData extracted successfully!")