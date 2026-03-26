import csv
import logging
import psycopg2
from week1.config import Config
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
def get_connection(config):
    return psycopg2.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
    )
def run_queries(query, conn, filename):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            results = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            with open(f"week2/results/{filename}", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(columns)
                writer.writerows(results)
            logger.info(f"Saved {len(results)} rows to {filename}")
    except Exception as e:
        logger.warning(f"Error {e}")
def run(config):
    conn = get_connection(config)
    run_queries(
        """SELECT 
    cus.country,
    SUM(fa.total_amount) as revenue
FROM fact_sales as fa
INNER JOIN dim_customer as cus 
ON fa.customer_id = cus.customer_id
GROUP BY cus.country
ORDER BY revenue DESC;""",
        conn,
        "revenue_by_country.csv",
    )
    run_queries(
        """Select SUM(fa.total_amount) as revenue , pr.category
from fact_sales as fa
INNER JOIN dim_products as pr
on fa.product_id = pr.product_id 
GROUP BY pr.category
ORDER BY revenue;
""",
        conn,
        "revenue_by_category.csv",
    )
    run_queries(
        """WITH customer_revenue AS (
    SELECT cus.name, cus.country, sum(fa.total_amount) AS revenue
      FROM fact_sales AS fa 
      INNER JOIN dim_customer as cus
      ON cus.customer_id = fa.customer_id
      GROUP BY cus.name, cus.country 
      HAVING SUM(fa.total_amount) >= 1000
      ORDER BY revenue DESC
)
SELECT name, country, revenue 
FROM customer_revenue; """,
        conn,
        "top_customers.csv",
    )
    conn.close()
if __name__ == "__main__":
    run(Config())