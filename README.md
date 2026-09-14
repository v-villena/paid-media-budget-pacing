# Paid Media Budget Pacing Tool

A web-based budget pacing dashboard built for paid media managers to quickly identify campaigns that are overpacing, underpacing, or on track against monthly budgets.

🔗 **Live App:** https://paid-media-budget-pacing.streamlit.app/

## Business Problem

Paid media managers often manage budgets across multiple campaigns and advertising platforms. Manually comparing spend against monthly budgets can be repetitive and makes it easy to miss campaigns that are spending too quickly or too slowly.

This tool turns campaign-level budget and spend data into an actionable pacing view, helping marketers identify where budget adjustments may be needed.

## Features

The dashboard automatically:

- Calculates remaining budget by campaign
- Calculates percentage of monthly budget used
- Compares budget usage against current month progress
- Identifies campaigns as Overpacing, Underpacing, or On Pace
- Calculates average daily spend
- Calculates the daily spend required to use the remaining budget
- Projects month-end spend based on current spend rate
- Calculates projected budget variance
- Highlights campaigns requiring attention
- Provides account-level budget and spend summaries
- Allows users to download the analyzed data as a CSV

## How It Works

Users upload a CSV containing campaign-level budget and spend data.

Required columns:

```text
campaign,channel,monthly_budget,spend_to_date
```

Example:

```text
Meta Prospecting,Meta,5000,2100
Google Search - Brand,Google Ads,3000,1980
```

The tool automatically determines the current day and number of days in the month, then compares campaign budget usage with month progress.

A 5 percentage point tolerance is used to classify pacing:

- **Overpacing:** Budget usage is more than 5 percentage points ahead of month progress
- **Underpacing:** Budget usage is more than 5 percentage points behind month progress
- **On Pace:** Budget usage is within 5 percentage points of month progress

## Key Calculations

**Remaining Budget**

```text
Monthly Budget - Spend to Date
```

**Budget Used %**

```text
Spend to Date / Monthly Budget × 100
```

**Average Daily Spend**

```text
Spend to Date / Current Day of Month
```

**Projected Month-End Spend**

```text
Average Daily Spend × Days in Month
```

**Projected Variance**

```text
Projected Month-End Spend - Monthly Budget
```

**Required Daily Spend**

```text
Remaining Budget / Days Remaining
```

## Tools & Technologies

- Python
- pandas
- Streamlit
- Git & GitHub
- Streamlit Community Cloud

## Dataset

The included sample dataset is fictional and was created for development, testing, and portfolio demonstration purposes.

The tool can also analyze other campaign datasets that follow the required CSV structure.

## Run Locally

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

Then launch the Streamlit app:

```bash
streamlit run app.py
```

## What I Learned

This project was built as a practical introduction to using Python for marketing analytics and automation.

Through the project, I worked with:

- pandas DataFrames and calculated fields
- Functions and conditional logic
- Date-based pacing calculations
- CSV ingestion and validation
- Data formatting and conditional highlighting
- Streamlit interface development
- Git branches, commits, pull requests, merges, and conflict resolution
- GitHub Codespaces
- Deploying a Python application as a public web app

## Future Improvements

Potential future enhancements include:

- Platform and channel filters
- Adjustable pacing tolerance
- Custom campaign date ranges
- Historical pacing trends
- Budget reallocation recommendations
- Direct integrations with advertising platform APIs
