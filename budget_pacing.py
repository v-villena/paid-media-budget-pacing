import pandas as pd

# Load campaign data
data = pd.read_csv("data/campaign_spend.csv")

# Calculate remaining budget
data["remaining_budget"] = data["monthly_budget"] - data["spend_to_date"]

# Calculate percentage of budget used
data["budget_used_pct"] = (
    data["spend_to_date"] / data["monthly_budget"] * 100
)

print(data)