from pyspark.sql import SparkSession
import os

os.environ["HADOOP_HOME"] = "C:/hadoop"

spark = SparkSession.builder \
    .appName("de-journey-week9") \
    .master("local[*]") \
    .config("spark.hadoop.io.nativeio.enabled", "false") \
    .getOrCreate()

df = spark.read.csv(
    "C:/Users/Ziyad/OneDrive/Desktop/de-journey/week9/data/sales.csv",
    header=True,
    inferSchema= True
)

df.show()
df.printSchema()


df.write.parquet("C:/Users/Ziyad/OneDrive/Desktop/de-journey/week9/data/sales.parquet", mode="overwrite")

df_parquet = spark.read.parquet("C:/Users/Ziyad/OneDrive/Desktop/de-journey/week9/data/sales.parquet")
df_parquet.show()
df_parquet.printSchema()

