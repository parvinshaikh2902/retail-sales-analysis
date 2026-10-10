# Retail Sales Analysis (Internship Mini Project)

A data analytics project on a retail sales dataset (3,000 raw orders, January 2024 to December 2025). The project covers the full workflow: data understanding, cleaning, transformation, sales EDA and customer analysis.

## Business Questions

1. What is happening with the company's sales?
2. Who are the company's most valuable customers?

## Project Files

| File | What it does |
|---|---|
| `Retail_Business_Analysis_Messy_3000.csv` | Raw dataset (messy, 3,000 rows) |
| `MiniProject.py` | Data understanding (shape, data types, missing values, duplicates) |
| `Data_Cleaning.py` | Cleans the raw data and saves `cleaned_retail_sales.csv` |
| `cleaned_retail_sales.csv` | Cleaned dataset (2,966 rows) |
| `Data_transformation.py` | Adds new analysis columns and saves `transformed_retail_sales.csv` |
| `transformed_retail_sales.csv` | Final dataset used for analysis (2,965 rows, 29 columns) |
| `Sales_EDA.ipynb` | Sales EDA and customer analysis notebook |

## How to Run

1. Install the libraries:
   ```
   pip install pandas numpy matplotlib jupyter
   ```
2. Keep all files in the same folder and run in this order:
   ```
   python Data_Cleaning.py
   python Data_transformation.py
   ```
3. Open `Sales_EDA.ipynb` and click **Run All**.

## What Was Done

### Data Cleaning
- Converted numbers and dates to the correct data types.
- Removed extra spaces and made text consistent (for example `NORTH`, `north` and `North` became `North`).
- Fixed category spelling mistakes and filled missing categories from the product name.
- Removed 34 duplicate rows (3,000 rows became 2,966).
- Turned impossible values (quantity of 0 or less, discount outside 0% to 50%, rating outside 1 to 5) into missing values instead of guessing.
- Rebuilt missing Sales with `Quantity x Unit_Price x (1 - Discount)` and calculated Profit Margin %.
- Profit and ratings were not filled in, because they are real business values.

### Data Transformation
New columns added: `Year`, `Month`, `Month_Name`, `Quarter`, `Profit_Status`, `Discount_Amount`, `Gross_Order_Value`, `Customer_Segment`, `Discount_Level`, `Product_Performance`.

### Sales EDA
Total sales, monthly trend, category, region and product sales, profit analysis, sales distribution, and loss-making orders.

### Customer Analysis
Customer revenue, top customers, average spending, repeat customers, customer contribution, and customer segments.

## Key Findings

**Sales**
- Total sales are Rs 12.05 crore and total profit is Rs 1.29 crore (10.7% margin).
- Sales fell 4.6% in 2025 but profit fell 23.5%.
- The West region's profit margin dropped from 13.2% to 7.4%, which is the main reason for the profit decline.
- Technology gives about 79% of sales and profit.
- The top 10 products give about 90% of sales.
- 22.6% of orders (669) lost money, and the loss rate is about the same at every discount level (22% to 23%), so discounts are not the cause.

**Customers**
- The average customer spends about Rs 60 lakh over two years, and all 20 customers are repeat customers.
- No customer gives more than 6.3% of revenue, so the business does not depend on one customer.
- 13 of 20 customers spent less in 2025 than in 2024.
- Ranking customers by profit gives a different top 10 than ranking by sales, so profit is the better measure of value.

## Limitations

- The dataset is an internship practice dataset, so the findings describe this data only.
- There are only 20 customers and 26 products.
- There is no cost data, so the analysis shows where profit fell but cannot explain why.
- 12 orders have no Customer_ID and are left out of the customer analysis.

## Tools

Python, Pandas, NumPy, Matplotlib, Jupyter Notebook, VS Code, Git and GitHub.

## Progress Log

| Day | Work done |
|---|---|
| Day 22 | Data understanding |
| Day 25 | Sales EDA |
| Day 26 | Customer analysis |

*Add a new row here after each day's work.*
