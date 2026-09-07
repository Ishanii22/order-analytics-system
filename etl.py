import pandas as pd
from sqlalchemy import create_engine

# Load the raw CSV
df = pd.read_csv("retail_sales_dataset.csv")

print("Raw data shape:", df.shape)
print(df.head())

# Clean column names (lowercase, no spaces)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Aggregate: daily total sales
daily_sales = df.groupby("date")["total_amount"].sum().reset_index()
daily_sales.columns = ["sale_date", "total_sales"]

print("\nDaily sales aggregated:")
print(daily_sales.head())

# Save aggregated data into PostgreSQL
DATABASE_URL = "postgresql://postgres:Postgre123@localhost:5432/order_system"
engine = create_engine(DATABASE_URL)

daily_sales.to_sql("daily_sales", engine, if_exists="replace", index=False)

print("\n✅ Daily sales data loaded into 'daily_sales' table successfully!")