import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker("en_IN")

# -----------------------------
# CONFIG
# -----------------------------
NUM_USERS = 5000
NUM_MERCHANTS = 500
NUM_TRANSACTIONS = 50000
NUM_SPLITS = 15000

np.random.seed(42)
random.seed(42)

# -----------------------------
# CITIES
# -----------------------------
cities = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Hyderabad",
    "Pune",
    "Kolkata",
    "Ahmedabad",
    "Jaipur",
    "Kochi"
]

# -----------------------------
# MERCHANT CATEGORIES
# -----------------------------
categories = [
    "Restaurant",
    "Travel",
    "Fuel",
    "Grocery",
    "Entertainment"
]

# -----------------------------
# USERS
# -----------------------------
users = []

for i in range(NUM_USERS):
    users.append([
        f"U{i+1:05}",
        random.randint(18, 55),
        random.choice(cities),
        fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
        random.randint(5, 120)
    ])

users_df = pd.DataFrame(
    users,
    columns=[
        "user_id",
        "age",
        "city",
        "signup_date",
        "monthly_transactions"
    ]
)

# -----------------------------
# MERCHANTS
# -----------------------------
merchants = []

for i in range(NUM_MERCHANTS):
    merchants.append([
        f"M{i+1:04}",
        random.choice(categories),
        random.choice(cities)
    ])

merchants_df = pd.DataFrame(
    merchants,
    columns=[
        "merchant_id",
        "category",
        "city"
    ]
)

# -----------------------------
# TRANSACTIONS
# -----------------------------
transactions = []

for i in range(NUM_TRANSACTIONS):

    merchant = merchants_df.sample(1).iloc[0]

    category = merchant["category"]

    if category == "Restaurant":
        amount = round(np.random.uniform(200, 3000), 2)

    elif category == "Travel":
        amount = round(np.random.uniform(500, 8000), 2)

    elif category == "Fuel":
        amount = round(np.random.uniform(200, 3000), 2)

    elif category == "Grocery":
        amount = round(np.random.uniform(300, 5000), 2)

    else:
        amount = round(np.random.uniform(200, 4000), 2)

    transactions.append([
        f"T{i+1:06}",
        random.choice(users_df["user_id"].tolist()),
        merchant["merchant_id"],
        amount,
        fake.date_between(
            start_date="-12m",
            end_date="today"
        )
    ])

transactions_df = pd.DataFrame(
    transactions,
    columns=[
        "transaction_id",
        "user_id",
        "merchant_id",
        "amount",
        "date"
    ]
)

# -----------------------------
# SPLIT REQUESTS
# -----------------------------
split_requests = []

transaction_ids = transactions_df["transaction_id"].tolist()

for i in range(NUM_SPLITS):

    status = np.random.choice(
        ["Completed", "Pending", "Failed"],
        p=[0.82, 0.13, 0.05]
    )

    split_requests.append([
        f"S{i+1:06}",
        random.choice(transaction_ids),
        random.randint(2, 8),
        np.random.choice(
            ["Equal", "Custom"],
            p=[0.75, 0.25]
        ),
        round(np.random.uniform(1, 120), 1),
        status
    ])

split_df = pd.DataFrame(
    split_requests,
    columns=[
        "split_id",
        "transaction_id",
        "group_size",
        "split_type",
        "settlement_time_minutes",
        "status"
    ]
)

# -----------------------------
# SAVE FILES
# -----------------------------
users_df.to_csv(
    "data/users.csv",
    index=False
)

merchants_df.to_csv(
    "data/merchants.csv",
    index=False
)

transactions_df.to_csv(
    "data/transactions.csv",
    index=False
)

split_df.to_csv(
    "data/split_requests.csv",
    index=False
)

# -----------------------------
# SUMMARY
# -----------------------------
print("\nDATA GENERATED SUCCESSFULLY\n")

print(f"Users: {len(users_df):,}")
print(f"Merchants: {len(merchants_df):,}")
print(f"Transactions: {len(transactions_df):,}")
print(f"Split Requests: {len(split_df):,}")

print("\nFiles saved in /data folder")