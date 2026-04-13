from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from week3.sales_pipeline import SalesPipeline
from week1.config import Config 
from week5.cloud_sink import CloudSink
from dotenv import load_dotenv
import os

load_dotenv(encoding="utf-8")
def extract():
    config = Config()
    pipe = SalesPipeline(config)
    pipe.connect()
    result = pipe.extract("/opt/airflow/project/week1/data/sales.csv")
    pipe.close()
    return result

def transform():
    config = Config()
    pipe = SalesPipeline(config)
    pipe.connect()
    raw = pipe.extract("/opt/airflow/project/week1/data/sales.csv")
    result = pipe.transform(raw)
    pipe.close()
    return result


def load_postgres():
    config = Config()
    pipe = SalesPipeline(config)
    pipe.connect()
    raw = pipe.extract("/opt/airflow/project/week1/data/sales.csv")
    transformed = pipe.transform(raw)
    result = pipe.load(transformed)
    pipe.close()
    return result

def export_cloud():
        sink = CloudSink(
        bucket_name=os.getenv("GCS_BUCKET"),
        project = os.getenv("GCP_PROJECT"),
        dataset_id = os.getenv("BQ_DATASET"),
        table_id=os.getenv("BQ_TABLE")
        )
        sink.export_to_cloud("/opt/airflow/project/week5/data/pipeline_output.csv")

with DAG(
    dag_id="sales_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    t1 = PythonOperator(task_id="extract", python_callable=extract)
    t2 = PythonOperator(task_id="transform", python_callable=transform)
    t3 = PythonOperator(task_id="load_postgres", python_callable=load_postgres)
    t4 = PythonOperator(task_id="export_cloud", python_callable=export_cloud)

    t1 >> t2 >> t3 >> t4