from dotenv import load_dotenv
from week5.cloud_sink import CloudSink
from week3.pipeline import Pipeline
from week1.config import Config
import csv
import os
load_dotenv(encoding="utf-8")
if __name__ == "__main__":
    config = Config()
    filepath = "week1/data/sales.csv"
    pipe = Pipeline(config)
    pipe.run()
    raw = pipe.extract(filepath)
    print(f"[1/4] Extracted {len(raw)} rows")
    print(f"[2/4] Loaded to PostgreSQL")
    records =raw
    transformed = pipe.transform(records)

    with open("week5/data/pipeline_output.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=transformed[0].keys())
        writer.writeheader()
        writer.writerows(transformed)

    sink = CloudSink(
        bucket_name=os.getenv("GCS_BUCKET"),
        project = os.getenv("GCP_PROJECT"),
        dataset_id = os.getenv("BQ_DATASET"),
        table_id=os.getenv("BQ_TABLE")
        )
    sink.export_to_cloud("week5/data/pipeline_output.csv")
    print(f"[3/4] Uploaded to GCS")
    print(f"[4/4] Loaded to BigQuery")




