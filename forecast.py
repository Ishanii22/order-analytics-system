import pandas as pd
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
import numpy as np

# Connect to the database
DATABASE_URL = "postgresql://postgres:Postgre123@localhost:5432/order_system"
engine = create_engine(DATABASE_URL)

# Load daily sales data
df = pd.read_sql("SELECT * FROM daily_sales ORDER BY sale_date", engine)
df["sale_date"] = pd.to_datetime(df["sale_date"])

# Convert dates into a simple numeric feature (day number since start)
df["day_number"] = (df["sale_date"] - df["sale_date"].min()).dt.days

X = df[["day_number"]]
y = df["total_sales"]

# Train a simple Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict the next 7 days
last_day = df["day_number"].max()
future_days = np.array([[last_day + i] for i in range(1, 8)])
predictions = model.predict(future_days)

print("\n📈 Forecast for the next 7 days:")
for i, pred in enumerate(predictions, start=1):
    future_date = df["sale_date"].max() + pd.Timedelta(days=i)
    print(f"{future_date.date()}: predicted sales = {round(pred, 2)}")