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
ON da.date_id = fa.date_id
GROUP BY da.quarter
ORDER BY revenue DESC;



SELECT cus.name, SUM(fa.total_amount) as revenue 
FROM fact_sales as fa
INNER JOIN dim_customer as cus
ON cus.customer_id = fa.customer_id
GROUP BY cus.name
ORDER BY revenue;




WITH customer_revenue AS (
	SELECT cus.name, cus.country, sum(fa.total_amount) AS revenue
  	FROM fact_sales AS fa 
  	INNER JOIN dim_customer as cus
  	ON cus.customer_id = fa.customer_id
  	GROUP BY cus.name, cus.country 
  	HAVING SUM(fa.total_amount) >= 1000
  	ORDER BY revenue DESC
)
SELECT name, country, revenue 
FROM customer_revenue; 



WITH units_per_product AS (
    SELECT pr.name, pr.category, SUM(fa.quantity) as quantity 
  	FROM fact_sales as fa 
  	INNER join dim_products as pr 
  	ON pr.product_id = fa.product_id 
  	GROUP BY pr.name, pr.category
  	ORDER BY quantity DESC
),
ranked_products AS (
    SELECT name, 
  		category,
  		quantity,
  		RANK() OVER (PARTITION BY category ORDER BY quantity DESC) AS rank
  	FROM units_per_product
    
)
SELECT category, name, quantity
FROM ranked_products
WHERE rank = 1;


SELECT pr.name , SUM(fa.total_amount) as revenue, da.date
FROM fact_sales as fa 
INNER JOIN dim_products as pr 
on fa.product_id = pr.product_id
INNER JOIN dim_date as da 
ON fa.date_id = da.date_id
WHERE date = '2024-01-15'
GROUP BY pr.name, da.date
ORDER BY revenue DESC;