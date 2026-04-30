from pyspark.sql import SparkSession

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

df.show()
df.printSchema()

print("Total rows:", df.count())

spark.stop()