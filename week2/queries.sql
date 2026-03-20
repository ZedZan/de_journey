SELECT 
    cus.country,
    SUM(fa.total_amount) as revenue
FROM fact_sales as fa
INNER JOIN dim_customer as cus 
ON fa.customer_id = cus.customer_id
GROUP BY cus.country
ORDER BY revenue DESC;



Select SUM(fa.total_amount) as revenue , pr.category
from fact_sales as fa
INNER JOIN dim_products as pr
on fa.product_id = pr.product_id 
GROUP BY pr.category
ORDER BY revenue;



SELECT SUM(fa.quantity) as total_units, pr.name
FROM fact_sales as fa
INNER JOIN dim_products as pr
ON pr.product_id = fa.product_id
GROUP BY pr.name
ORDER BY total_units DESC;


SELECT SUM(fa.total_amount) as revenue, da.quarter
FROM fact_sales as fa
INNER JOIN dim_date as da
ON da.date_id = fa.dat_id
GROUP BY da.quarter
ORDER BY revenue DESC;



SELECT cus.name, SUM(fa.total_amount) as revenue 
FROM fact_sales as fa
INNER JOIN dim_customer as cus
ON cus.customer_id = fa.customer_id
GROUP BY cus.name
ORDER BY revenue;
