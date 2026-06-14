import pandas as pd

users = pd.read_csv("data/users.csv")
merchants = pd.read_csv("data/merchants.csv")
transactions = pd.read_csv("data/transactions.csv")
splits = pd.read_csv("data/split_requests.csv")

merged = (
    transactions
    .merge(merchants, on="merchant_id")
    .merge(splits, on="transaction_id")
)

print("\nTOP MERCHANT CATEGORIES")

print(
    merged.groupby("category")["amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTOP CITIES")

city_analysis = (
    transactions
    .merge(users, on="user_id")
)

print(
    city_analysis.groupby("city")["amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSETTLEMENT STATUS")

print(
    splits["status"]
    .value_counts()
)