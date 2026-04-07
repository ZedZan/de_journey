from google.cloud import storage
from pathlib import Path
from google.cloud import bigquery

class CloudSink :
    def __init__(self, bucket_name, project, dataset_id, table_id):
        self.bucket_name = bucket_name
        self.project = project
        self.dataset_id = dataset_id
        self.table_id = table_id
    
    def export_to_cloud(self, file_path):
        storage_client= storage.Client()
        bucket = storage_client.bucket(self.bucket_name)
        blob_name = Path(file_path).name
        blob = bucket.blob(blob_name)


        blob.upload_from_filename(file_path)

        print(
            f"File {file_path} uploaded to gs://{self.bucket_name}/{blob_name}."
        )
        client = bigquery.Client()
        dataset = bigquery.Dataset(f"{self.project}.{self.dataset_id}")
        dataset.location = "EU"
        client.create_dataset(dataset, exists_ok=True)
        job_config = bigquery.LoadJobConfig(
            autodetect= True,
            source_format= bigquery.SourceFormat.CSV,
            skip_leading_rows=1
        )
        gcs_uri = f"gs://{self.bucket_name}/{blob_name}"
        table_ref = f"{self.project}.{self.dataset_id}.{self.table_id}"
        job = client.load_table_from_uri(gcs_uri, table_ref, job_config=job_config)
        job.result()
        table = client.get_table(table_ref)
        print(table.num_rows)


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv(encoding="utf-8")
    sink = CloudSink(
        bucket_name=os.getenv("GCS_BUCKET"),
        project = os.getenv("GCP_PROJECT"),
        dataset_id = os.getenv("BQ_DATASET"),
        table_id=os.getenv("BQ_TABLE")
    )

    sink.export_to_cloud("week5/data/sales_dummy.csv")