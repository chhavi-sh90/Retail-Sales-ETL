-- 1. Total Revenue
SELECT SUM(total_sales) AS total_revenue
FROM sales;

-- 2. Product-wise Revenue
SELECT product, SUM(total_sales) AS revenue
FROM sales
GROUP BY product;

-- 3. Monthly Revenue
SELECT DATE_TRUNC('month', order_date::date) AS month,
       SUM(total_sales) AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;

-- 4. Customer-wise Revenue
SELECT customer_name, SUM(total_sales) AS revenue
FROM sales
GROUP BY customer_name
ORDER BY revenue DESC;

-- 5. Product-wise Quantity
SELECT product, SUM(quantity) AS total_quantity
FROM sales
GROUP BY product
ORDER BY total_quantity DESC;