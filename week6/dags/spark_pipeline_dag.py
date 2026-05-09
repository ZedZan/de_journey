from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from google.cloud import storage

def download_from_gcs():
    client = storage.Client.from_service_account_json(
        "/opt/airflow/project/gcp-key.json"
    )
    bucket = client.bucket("de-journey-raw")
    blob = bucket.blob("pipeline_output.csv")
    blob.download_to_filename("/tmp/pipeline_output.csv")
    print("Downloaded pipeline_output.csv from GCS")

with DAG(
    dag_id="spark_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:
    gcs_download = PythonOperator(
        task_id="gcs_download",
        python_callable=download_from_gcs
    )
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/airflow/project/week7/de_journey && dbt run --profiles-dir /opt/airflow/project/week7/de_journey --no-version-check"
    )
    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/airflow/project/week7/de_journey && dbt test --profiles-dir /opt/airflow/project/week7/de_journey --no-version-check"
    )
    gcs_download >> dbt_run >> dbt_test