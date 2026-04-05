from google.cloud import bigquery
from dotenv import load_dotenv
import os


load_dotenv(encoding="utf-8")
project = os.getenv("GCP_PROJECT")
dataset_id = os.getenv("BQ_DATASET")
table_id = os.getenv("BQ_TABLE")
bucket = os.getenv("GCS_BUCKET")
gcs_uri = f"gs://{bucket}/sales_dummy.csv"
table_ref = f"{project}.{dataset_id}.{table_id}"

client = bigquery.Client()
dataset = bigquery.Dataset(f"{project}.{dataset_id}")
dataset.location = "EU"
client.create_dataset(dataset, exists_ok=True)
job_config = bigquery.LoadJobConfig(
    autodetect= True,
    source_format= bigquery.SourceFormat.CSV,
    skip_leading_rows=1
)

job = client.load_table_from_uri(gcs_uri, table_ref, job_config=job_config)
job.result()
table = client.get_table(table_ref)
print(table.num_rows)

