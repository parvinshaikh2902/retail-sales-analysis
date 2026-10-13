create database retail_db;
use retail_db;
select count(*) from sales;
select sum(sales)as Total_sale from sales; -- total sales 
select sum(profit)as Total_profit from sales; -- total profit
select count(*)as Total_order from sales;  -- Total orders
select count(distinct Customer_ID)as Total_customers from sales;  -- Total customers
select avg(sales)as average_sale from sales;

-- sales by category
select Category,round(sum(sales),0) as Total_sales from sales group by Category order by Total_sales desc;
-- sales by region
select Region,round(sum(sales),0) as Total_sales from sales group by Region order by Total_sales desc;
-- Profit by category
select Category,round(sum(Profit),0)as total_profit from sales group by Category order by total_profit desc; 
 -- Profit By region
 select Region,round(sum(Profit),0)as total_profit from sales group by Region order by total_profit desc; 
-- Sales by month
select `Year`, Month_Name, ROUND(SUM(Sales), 0) AS total_sales from sales where`Year` is not null
group by `Year`, `Month`, Month_Name order by `Year`, `Month`;

-- top 10 customers by sales
select Customer_ID,round(sum(sales),0)as Total_Sales from sales group by Customer_ID 
order by Total_Sales desc limit 10; 

-- Customers who spent less in 2025 than in 2024
select Customer_ID, round(sum(case when `Year` = 2024 then Sales end), 0) as sales_2024,
round(sum(case when`Year` = 2025 then Sales end), 0) as sales_2025 from sales
group by Customer_ID having sales_2025 < sales_2024 order by sales_2024 - sales_2025 desc limit 10;

-- Average customer Spending
select round(sum(sales)/count(distinct Customer_ID),0) as avg_customer_spending from sales
 where Customer_ID is not null;
 
 -- top 10 products by sales
 select Product_name,round(sum(sales),0)as Total_sales from sales group by Product_name 
 order by Total_sales desc limit 10;
 
 -- Bottom 10 products by sales
  select Product_name,round(sum(sales),0)as Total_sales from sales group by Product_name 
  order by Total_sales limit 10
  
--  Most profitable products
select Product_Name, round(sum(Profit), 0) AS total_profit from sales group by Product_Name
order by total_profit desc limit 10;

-- Customer ranking
with customer_sales as (select customer_id, sum(sales) as total_sales from sales
 where customer_id is not null group by customer_id) 
select customer_id, round(total_sales, 0) as total_sales, rank() over (order by total_sales desc) as sales_rank, round(total_sales * 100.0 / sum(total_sales) 
over (), 1) as share_pct from customer_sales order by sales_rank;

-- Product ranking within category
 with product_sales as (select category, product_name, sum(sales) as total_sales from sales 
 group by category, product_name)
 select category, product_name, round(total_sales, 0) as total_sales, rank() over (partition by category order by total_sales desc) as rank_in_category
 from product_sales order by category, rank_in_category;
 
 -- Category ranking
 select category, round(sum(sales), 0) as total_sales, rank() over (order by sum(sales) desc) as sales_rank, 
 round(sum(profit), 0) as total_profit, rank() over (order by sum(profit) desc) as profit_rank from sales group by category;



 
