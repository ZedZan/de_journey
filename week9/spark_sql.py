from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

spark = SparkSession.builder \
    .appName("de-journey-week9") \
    .master("local[*]") \
    .getOrCreate()

data = [
    (1, "Alice", "FR", 100.0),
    (2, "Bob", "DE", 200.0),
    (3, "Alice", "FR", 150.0),
    (4, "Charlie", "FR", 300.0),
    (5, "Bob", "DE", 50.0),
    (6, "Charlie", "DE", 400.0),
]
columns = ["id", "name", "country", "amount"]

df = spark.createDataFrame(data, columns)
df.createOrReplaceTempView("sales")

grouped = df.groupBy("country").agg(
    spark_sum("amount").alias("total_amount")
)
filtered = grouped.filter(col("total_amount") > 300)
sorted_df = filtered.orderBy(col("total_amount").desc())
sorted_df.show()
# result = spark.sql(
#     """
#         SELECT country, SUM(amount) as total_amount
#         FROM sales
#         GROUP BY country
#         HAVING SUM(amount) > 300
#         ORDER BY total_amount DESC
#     """
# )
# result.show()
spark.stop()