import pandas as pd

# STEP 1
# Load the campaign data from the CSV file.
data = pd.read_csv("data/campaign_spend.csv")

# STEP 2
# Print the full dataset so we can inspect what Python loaded.
print(data)

# YOUR FIRST CHALLENGE
# Add a new column called "remaining_budget".
# It should equal monthly_budget minus spend_to_date.
#
# Hint:
# data["remaining_budget"] = ...
#
# Then print the updated dataset.
