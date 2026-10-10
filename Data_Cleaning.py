import pandas as pd
import numpy as np

# Step 0: Read the messy file
df = pd.read_csv("Retail_Business_Analysis_Messy_3000.csv")
print("Rows and columns before cleaning:", df.shape)

# Step 1: Convert numbers to numbers and the date column to dates
number_cols = ["Quantity", "Unit_Price", "Discount", "Sales",
               "Profit", "Customer_Rating", "Delivery_Days"]
for col in number_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# Step 2: Clean the text columns (remove extra spaces, make spelling consistent)
text_cols = ["Customer_Name", "Segment", "Category", "Sub_Category",
             "Product_Name", "Region", "City", "Payment_Method"]
for col in text_cols:
    df[col] = df[col].str.strip().str.title()   # "  NORTH " becomes "North"

# .title() breaks a few names, so fix them back
df["Payment_Method"] = df["Payment_Method"].replace(
    {"Upi": "UPI", "Cash On Delivery": "Cash on Delivery"})
df["Product_Name"] = df["Product_Name"].replace("Usb Hub", "USB Hub")

# Fix known spelling mistakes in Category
df["Category"] = df["Category"].replace(
    {"Technlogy": "Technology", "Office Suppllies": "Office Supplies"})

# Fix Category using Product_Name: every product belongs to exactly one category,
# so this fills the missing/"Unknown" categories and fixes the few wrong ones
df["Category"] = df["Category"].replace("Unknown", np.nan)
product_category = df.groupby("Product_Name")["Category"].agg(
    lambda s: s.mode()[0] if s.notna().any() else np.nan)
df["Category"] = df["Product_Name"].map(product_category)

# IDs should always be in capital letters
df["Order_ID"] = df["Order_ID"].str.strip().str.upper()
df["Customer_ID"] = df["Customer_ID"].str.strip().str.upper()

# Step 3: Fill empty text values with "Unknown" (we cannot guess these)
for col in ["Customer_Name", "Category", "City", "Payment_Method"]:
    df[col] = df[col].fillna("Unknown")

# Step 4: Remove duplicate rows
print("Duplicate rows found:", df.duplicated().sum())
df = df.drop_duplicates()

# Step 5: Turn impossible values into missing values (NaN)
df.loc[df["Quantity"] <= 0, "Quantity"] = np.nan                    # quantity must be above 0
df.loc[(df["Discount"] < 0) | (df["Discount"] > 0.5), "Discount"] = np.nan   # discount must be 0% to 50%
df.loc[(df["Customer_Rating"] < 1) | (df["Customer_Rating"] > 5), "Customer_Rating"] = np.nan  # rating must be 1 to 5

# Step 6: Fill missing Sales using the formula
formula_sales = (df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])).round(2)
df["Sales"] = df["Sales"].fillna(formula_sales)

# Step 7: Create Profit Margin %
df["Profit_Margin_Pct"] = df["Profit"] / df["Sales"] * 100

# Step 8: Make Quantity a whole number and save the cleaned file
df["Quantity"] = df["Quantity"].round().astype("Int64")
df.to_csv("cleaned_retail_sales.csv", index=False)

print("Rows and columns after cleaning::", df.shape)
print(df.isnull().sum())
