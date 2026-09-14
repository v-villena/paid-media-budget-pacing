import calendar
from datetime import date

import pandas as pd
import streamlit as st


# Page setup
st.set_page_config(
    page_title="Paid Media Budget Pacing Tool",
    layout="wide",
)


# Get current date and month progress
today = date.today()
day_of_month = today.day
days_in_month = calendar.monthrange(today.year, today.month)[1]
expected_spend_pct = day_of_month / days_in_month * 100
days_remaining = days_in_month - day_of_month + 1


# Determine whether a campaign is pacing correctly
def get_pacing_status(budget_used_pct, expected_spend_pct):
    difference = budget_used_pct - expected_spend_pct

    if difference > 5:
        return "Overpacing"
    elif difference < -5:
        return "Underpacing"
    else:
        return "On Pace"


# Add color to pacing status
def color_pacing_status(value):
    if value == "Overpacing":
        return "background-color: #ffcccc; color: #990000;"
    elif value == "Underpacing":
        return "background-color: #fff2cc; color: #7f6000;"
    elif value == "On Pace":
        return "background-color: #d9ead3; color: #274e13;"
    return ""


# App header
st.title("Paid Media Budget Pacing Tool")

st.write(
    "Upload a campaign spend CSV to analyze pacing, projected spend, "
    "remaining budget, and campaigns that may need attention."
)


# CSV format guide
with st.expander("CSV format guide"):
    st.write(
        "Your CSV should include these columns:"
    )

    st.code(
        "campaign,channel,monthly_budget,spend_to_date"
    )

    st.write(
        "Example:"
    )

    st.code(
        "Meta Prospecting,Meta,5000,2100\n"
        "Google Search - Brand,Google Ads,3000,1980"
    )


# Upload campaign data
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])


if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Check for required columns
    required_columns = {
        "campaign",
        "channel",
        "monthly_budget",
        "spend_to_date",
    }

    missing_columns = required_columns - set(data.columns)

    if missing_columns:
        st.error(
            "Your CSV is missing these required columns: "
            + ", ".join(sorted(missing_columns))
        )
        st.stop()

    # Calculate account-level totals
    total_budget = data["monthly_budget"].sum()
    total_spend = data["spend_to_date"].sum()
    total_remaining = total_budget - total_spend
    account_budget_used_pct = total_spend / total_budget * 100

    # Display account summary
    st.subheader("Account Summary")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Total Budget",
        f"${total_budget:,.0f}"
    )

    col2.metric(
        "Spend to Date",
        f"${total_spend:,.0f}"
    )

    col3.metric(
        "Remaining Budget",
        f"${total_remaining:,.0f}"
    )

    col4.metric(
        "Budget Used",
        f"{account_budget_used_pct:.1f}%"
    )

    col5.metric(
        "Month Progress",
        f"{expected_spend_pct:.1f}%"
    )

    # Calculate remaining budget
    data["remaining_budget"] = (
        data["monthly_budget"] - data["spend_to_date"]
    )

    # Calculate average daily spend so far
    data["average_daily_spend"] = (
        data["spend_to_date"] / day_of_month
    )

    # Project month-end spend at current spending rate
    data["projected_month_end_spend"] = (
        data["average_daily_spend"] * days_in_month
    )

    # Calculate projected variance from budget
    data["projected_variance"] = (
        data["projected_month_end_spend"] - data["monthly_budget"]
    )

    # Calculate required daily spend for rest of month
    data["required_daily_spend"] = (
        data["remaining_budget"] / days_remaining
    )

    # Calculate percentage of budget used
    data["budget_used_pct"] = (
        data["spend_to_date"] / data["monthly_budget"] * 100
    )

    # Determine pacing status
    data["pacing_status"] = data["budget_used_pct"].apply(
        lambda x: get_pacing_status(
            x,
            expected_spend_pct
        )
    )

    # Campaigns requiring attention
    attention_data = data[
        data["pacing_status"] != "On Pace"
    ].copy()

    st.subheader("Campaigns Requiring Attention")

    if attention_data.empty:
        st.success(
            "All campaigns are currently within the pacing tolerance."
        )
    else:
        attention_display = attention_data[
            [
                "campaign",
                "channel",
                "budget_used_pct",
                "projected_variance",
                "required_daily_spend",
                "pacing_status",
            ]
        ].copy()

        attention_display.columns = [
            "Campaign",
            "Channel",
            "Budget Used %",
            "Projected Variance",
            "Required Daily Spend",
            "Pacing Status",
        ]

        styled_attention = (
            attention_display.style
            .format(
                {
                    "Budget Used %": "{:.1f}%",
                    "Projected Variance": "${:,.2f}",
                    "Required Daily Spend": "${:,.2f}",
                }
            )
            .map(
                color_pacing_status,
                subset=["Pacing Status"]
            )
        )

        st.dataframe(
            styled_attention,
            use_container_width=True,
            hide_index=True
        )

    # Main campaign analysis table
    st.subheader("Campaign Budget Analysis")

    display_data = data[
        [
            "campaign",
            "channel",
            "monthly_budget",
            "spend_to_date",
            "remaining_budget",
            "budget_used_pct",
            "required_daily_spend",
            "projected_month_end_spend",
            "projected_variance",
            "pacing_status",
        ]
    ].copy()

    display_data.columns = [
        "Campaign",
        "Channel",
        "Monthly Budget",
        "Spend to Date",
        "Remaining Budget",
        "Budget Used %",
        "Required Daily Spend",
        "Projected Month-End Spend",
        "Projected Variance",
        "Pacing Status",
    ]

    styled_data = (
        display_data.style
        .format(
            {
                "Monthly Budget": "${:,.2f}",
                "Spend to Date": "${:,.2f}",
                "Remaining Budget": "${:,.2f}",
                "Budget Used %": "{:.1f}%",
                "Required Daily Spend": "${:,.2f}",
                "Projected Month-End Spend": "${:,.2f}",
                "Projected Variance": "${:,.2f}",
            }
        )
        .map(
            color_pacing_status,
            subset=["Pacing Status"]
        )
    )

    st.dataframe(
        styled_data,
        use_container_width=True,
        hide_index=True
    )

    # Download analyzed CSV
    st.subheader("Download Results")

    export_data = data.copy()

    csv_output = export_data.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Analyzed CSV",
        data=csv_output,
        file_name="budget_pacing_analysis.csv",
        mime="text/csv",
    )