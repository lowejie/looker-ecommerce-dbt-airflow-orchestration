from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define the DAG
with DAG(
    dag_id="dbt_run_dag",                               # Unique identifier for the DAG
    start_date=datetime(2025, 1, 1),   # Start date for scheduling
    schedule="@daily",                                  # Run once per day
    catchup=False,                                      # Do not backfill missed runs
) as dag:

    # Task: Run dbt models
    run_dbt = BashOperator(
        task_id="dbt_run",                              # Unique task id
    # Command to execute in container, navigate to dbt project folder and run all dbt models using specified profiles directory
        bash_command="""
        cd /opt/airflow/looker_ecommerce_bigquery_elt_pipeline && \
        dbt run --profiles-dir /home/***/.dbt
        """
    )
