import pandas as pd
import numpy as np

# Read the cleaned file (Order_Date is read as a real date)
df = pd.read_csv("cleaned_retail_sales.csv", parse_dates=["Order_Date"])
print("Rows and columns before transformation:", df.shape)

# Task 1: Date features
df["Year"] = df["Order_Date"].dt.year.astype("Int64")
df["Month"] = df["Order_Date"].dt.month.astype("Int64")
df["Month_Name"] = df["Order_Date"].dt.month_name()
df["Quarter"] = df["Order_Date"].dt.quarter.astype("Int64")

# Task 2: Profit status (Loss / Low Profit / High Profit) and discount amount in rupees
df["Profit_Status"] = np.select(
    [df["Profit"] < 0, df["Profit_Margin_Pct"] < 10, df["Profit_Margin_Pct"] >= 10],
    ["Loss", "Low Profit", "High Profit"],
    default="Unknown")
df["Discount_Amount"] = (df["Quantity"] * df["Unit_Price"] * df["Discount"]).round(2)

# Task 3: Order value
# Remove the leftover duplicate Order_ID row that has a missing Quantity
is_duplicate_id = df["Order_ID"].notna() & df["Order_ID"].duplicated(keep=False)
df = df[~(is_duplicate_id & df["Quantity"].isna())]
# Sales is already the net order value, so add the value before discount
df["Gross_Order_Value"] = (df["Quantity"] * df["Unit_Price"]).round(2)

# Task 4: Customer segment based on each customer's total sales
customer_total = df.groupby("Customer_ID")["Sales"].sum()
low_limit = customer_total.quantile(1/3)    # bottom third of customers
high_limit = customer_total.quantile(2/3)   # top third of customers
segment = np.select(
    [customer_total >= high_limit, customer_total >= low_limit],
    ["High Value", "Medium Value"],
    default="Low Value")
df["Customer_Segment"] = df["Customer_ID"].map(dict(zip(customer_total.index, segment))).fillna("Unknown")

# Task 5: Extra business columns
# Discount level: 0%, up to 15%, above 15%
df["Discount_Level"] = pd.cut(df["Discount"], [-0.001, 0, 0.15, np.inf],
                              labels=["No Discount", "Low Discount", "High Discount"])

# Product performance: rank products by their profit margin % (profit earned per rupee of sales)
# Margin is used instead of total profit, because total profit only shows which products are expensive
product_profit = df.groupby("Product_Name")["Profit"].sum()
product_sales = df["Sales"].where(df["Profit"].notna()).groupby(df["Product_Name"]).sum()
product_margin = product_profit / product_sales * 100
low_m = product_margin.quantile(1/3)
high_m = product_margin.quantile(2/3)
performance = np.select(
    [product_margin >= high_m, product_margin >= low_m],
    ["Top Performer", "Average Performer"],
    default="Under Performer")
df["Product_Performance"] = df["Product_Name"].map(dict(zip(product_margin.index, performance)))

# Save the final file for the dashboard
df.to_csv("transformed_retail_sales.csv", index=False)
print("Rows and columns after transformation:", df.shape)