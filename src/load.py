
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

# Project directory
BASE_DIR = Path(__file__).resolve().parents[1]

# Read cleaned CSV
file_path = BASE_DIR / "data" / "processed" / "cleaned_sales.csv"
df = pd.read_csv(file_path)

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:5432@localhost:5432/retail_db"
)

# Load data into PostgreSQL
df.to_sql(
    "sales",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully into PostgreSQL!")
