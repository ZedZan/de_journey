from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id = "dbt_pipeline",
    start_date = datetime(2026,1,1),
    schedule_interval = "@daily",
    catchup = False,
) as dag:
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/airflow/project/week7/de_journey && dbt run --profiles-dir /opt/airflow/project/week7/de_journey --no-version-check"
    )
    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/airflow/project/week7/de_journey && dbt test --profiles-dir /opt/airflow/project/week7/de_journey --no-version-check"
    )
    dbt_snapshot = BashOperator(
        task_id ="dbt_snapshot",
        bash_command = "cd /opt/airflow/project/week7/de_journey && dbt snapshot --profiles-dir /opt/airflow/project/week7/de_journey --no-version-check"
    )
    dbt_source_freshness = BashOperator(
        task_id="dbt_source_freshness",
        bash_command="cd /opt/airflow/project/week7/de_journey && dbt source freshness --profiles-dir /opt/airflow/project/week7/de_journey --no-version-check"
    )
    dbt_snapshot >> dbt_run >> dbt_test >> dbt_source_freshness