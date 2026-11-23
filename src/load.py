from sqlalchemy import create_engine

def load_data(df):

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