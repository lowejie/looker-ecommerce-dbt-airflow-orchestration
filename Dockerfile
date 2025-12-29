FROM apache/airflow:2.9.3

# Switch to root for system-level installs
USER root

# Optional: install git if not present
RUN apt-get update && apt-get install -y git && apt-get clean

# Switch back to airflow for pip install
USER airflow

# Install dbt-core and BigQuery adapter
RUN pip install --no-cache-dir dbt-core dbt-bigquery

