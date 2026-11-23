from extract import extract_data
from clean import clean_data
from load import load_data

def main():
    print("ETL Pipeline Started")

    df = extract_data()
    df = clean_data(df)
    load_data(df)

    print("ETL Pipeline Completed Successfully!")

if __name__ == "__main__":
    main()