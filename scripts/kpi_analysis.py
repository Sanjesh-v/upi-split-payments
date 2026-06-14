import pandas as pd

# Load data
users = pd.read_csv("data/users.csv")
merchants = pd.read_csv("data/merchants.csv")
transactions = pd.read_csv("data/transactions.csv")
splits = pd.read_csv("data/split_requests.csv")

# -----------------------
# KPI 1: Total Split Volume
# -----------------------

merged = splits.merge(
    transactions,
    on="transaction_id",
    how="left"
)

total_split_volume = merged["amount"].sum()

# -----------------------
# KPI 2: Success Rate
# -----------------------

success_rate = (
    len(merged[merged["status"] == "Completed"])
    / len(merged)
) * 100

# -----------------------
# KPI 3: Avg Settlement Time
# -----------------------

avg_settlement_time = merged[
    "settlement_time_minutes"
].mean()

# -----------------------
# KPI 4: Revenue Estimate
# -----------------------

merchant_fee = 0.002

estimated_revenue = (
    total_split_volume * merchant_fee
)

# -----------------------
# KPI 5: Average Group Size
# -----------------------

avg_group_size = merged[
    "group_size"
].mean()

# -----------------------
# KPI 6: Split Type Distribution
# -----------------------

split_distribution = (
    merged["split_type"]
    .value_counts(normalize=True)
    * 100
)

# -----------------------
# PRINT RESULTS
# -----------------------

print("\nUPI SPLIT PAYMENTS KPI REPORT")
print("=" * 40)

print(
    f"\nTotal Split Volume: ₹{total_split_volume:,.2f}"
)

print(
    f"Settlement Success Rate: {success_rate:.2f}%"
)

print(
    f"Average Settlement Time: {avg_settlement_time:.2f} mins"
)

print(
    f"Estimated Revenue: ₹{estimated_revenue:,.2f}"
)

print(
    f"Average Group Size: {avg_group_size:.2f}"
)

print("\nSplit Type Distribution")

for idx, val in split_distribution.items():
    print(f"{idx}: {val:.2f}%")