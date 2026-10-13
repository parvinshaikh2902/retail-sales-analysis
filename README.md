# Retail Sales Analysis (Internship Mini Project)

Analysis of a retail sales dataset (3,000 orders, Jan 2024 to Dec 2025) using Python, Pandas and SQL (MySQL).

**Questions answered:** What is happening with the company's sales? Who are its most valuable customers?

## Files

- `Retail_Business_Analysis_Messy_3000.csv`: raw data
- `Data_Cleaning.py`: cleans the raw data
- `Data_transformation.py`: adds new analysis columns
- `Sales_EDA.ipynb`: sales, customer and product analysis
- `Retail_SQL_Analysis.sql`: the same analysis in SQL (21 queries)
- `MiniProject.py`: data understanding

## How to Run

1. `pip install pandas numpy matplotlib jupyter`
2. Run `Data_Cleaning.py`, then `Data_transformation.py`
3. Open `Sales_EDA.ipynb` and click Run All
4. For SQL: load `transformed_retail_sales.csv` into a MySQL 8.0 table named `sales` (database `retail_db`) and run `Retail_SQL_Analysis.sql` in MySQL Workbench

## Key Findings

- Sales Rs 12.05 crore, profit Rs 1.29 crore (10.7% margin).
- In 2025 sales fell 4.6% but profit fell 23.5%. The West region's margin dropped from 13.2% to 7.4%.
- Technology gives 79% of sales and profit. The top 10 products give 90% of sales.
- 22.6% of orders lost money, at every discount level equally, so discounts are not the cause.
- Laser Printer sells a lot but has a low margin (8.1%). Smartphone sales fell steadily.
- 20 customers, no one above 6.3% of revenue. 13 of 20 spent less in 2025.
- The SQL queries give the same results as the Python analysis.

## Limitations

Practice dataset with 20 customers and no cost data, so the analysis shows where profit fell but not why.

## Progress

Day 22 Data understanding | Day 25 Sales EDA | Day 26 Customer analysis | Day 27 Product analysis | Day 28 SQL analysis
