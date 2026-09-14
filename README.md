# Paid Media Budget Pacing Tool

A Python project for analyzing paid media budget pacing across campaigns and channels.

## Business problem

Paid media managers need to know whether campaigns are spending too quickly, too slowly, or on pace to hit monthly budgets. Checking this manually across multiple platforms is repetitive and can lead to missed pacing issues.

## Project goal

Build a Python workflow that can:

- Read campaign budget and spend data
- Calculate remaining budget by campaign
- Calculate the percentage of monthly budget used
- Create a foundation for more advanced budget pacing analysis

## Current version

Version 0.1 starts with loading campaign data and calculating remaining budget.

## Tools

- Python
- pandas

## Dataset

The included dataset is fictional and created for learning and portfolio purposes.

## Example output

The script calculates:

- Remaining budget by campaign
- Percentage of monthly budget already used

Example:

| Campaign | Monthly Budget | Spend to Date | Remaining Budget | Budget Used % |
|---|---:|---:|---:|---:|
| Meta Prospecting | 5000 | 2100 | 2900 | 42.00 |
| Meta Retargeting | 2500 | 1450 | 1050 | 58.00 |
| Google Search - Brand | 3000 | 1980 | 1020 | 66.00 |
| Google Search - Nonbrand | 8000 | 5100 | 2900 | 63.75 |
| TikTok Creative Testing | 2500 | 700 | 1800 | 28.00 |

## How to run

Install dependencies:

```bash
pip install -r requirements.txt
