import os
from datetime import datetime
from google.cloud import storage
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, current_timestamp

# -----------------------------
# 1. Spark session with GCS connector
# -----------------------------
os.environ["HADOOP_HOME"] = "C:/hadoop"
os.environ["PYSPARK_PYTHON"] = r"C:\Users\Ziyad\AppData\Local\Programs\Python\Python311\python.exe"

spark = SparkSession.builder \
    .appName("de-journey-week9-gcs-pipeline") \
    .master("local[*]") \
    .getOrCreate()

# -----------------------------
# 2. Download CSV from GCS to local temp file
# -----------------------------
bucket_name = "de-journey-raw"
source_blob = "pipeline_output.csv"
local_temp = "temp_pipeline_output.csv"

client = storage.Client.from_service_account_json(
    "C:/Users/Ziyad/OneDrive/Desktop/de-journey/gcp-key.json"
)

bucket = client.bucket(bucket_name)
blob = bucket.blob(source_blob)
blob.download_to_filename(local_temp)

print("Downloaded from GCS →", local_temp)

# -----------------------------
# 3. Read into Spark
# -----------------------------
df = spark.read.csv(local_temp, header=True, inferSchema=True)

print("=== Loaded CSV into Spark ===")
df.show()

# -----------------------------
# 4. Simple transformation
#    - Filter numeric column > threshold
#    - Add processed_at timestamp
# -----------------------------
threshold = 4000  # example threshold

df_transformed = df.filter(col("sales") > threshold) \
                   .withColumn("processed_at", current_timestamp())

print("=== After Transformation ===")
df_transformed.show()

# -----------------------------
# 5. Write Parquet locally
# -----------------------------
local_parquet_path = "output_parquet"

df_transformed.write.mode("overwrite").parquet(local_parquet_path)

print("Wrote Parquet locally →", local_parquet_path)

# -----------------------------
# 6. Upload Parquet folder back to GCS
# -----------------------------
gcs_output_path = "spark/output.parquet"

for root, dirs, files in os.walk(local_parquet_path):
    for file in files:
        local_file = os.path.join(root, file)
        relative_path = os.path.relpath(local_file, local_parquet_path)
        gcs_blob_path = f"{gcs_output_path}/{relative_path}"

        blob = bucket.blob(gcs_blob_path)
        blob.upload_from_filename(local_file)

        print("Uploaded:", gcs_blob_path)

print("=== Upload to GCS complete ===")