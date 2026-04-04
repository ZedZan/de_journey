from google.cloud import storage
from dotenv import load_dotenv
import os

load_dotenv(encoding="utf-8")
bucket_name = os.getenv("GCS_BUCKET")
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client= storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)


    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )
    print(f"the url gs://{bucket_name}/{destination_blob_name} ")

if __name__ == "__main__" :
    upload_blob(bucket_name, "week5/data/sales_dummy.csv", "sales_dummy.csv")