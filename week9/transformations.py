from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

spark = SparkSession.builder \
    .appName("de-journey-week9") \
    .master("local[*]") \
    .getOrCreate()

data = [
    (1, "Alice", 100.0),
    (2, "Bob", 200.0),
    (3, "Alice", 150.0),
    (4, "Charlie", 300.0),
]

columns = ["id", "name", "amount"]

df = spark.createDataFrame(data, columns)

filtered = df.filter(col("amount") > 150)

with_tax = filtered.withColumn("amount_with_tax", col("amount") *1.2)

grouped = with_tax.groupBy("name").agg(
    spark_sum("amount_with_tax").alias("total_amount_with_tax")
)

sorted_df = grouped.orderBy(col("total_amount_with_tax").desc())

sorted_df.show()

spark.stop()