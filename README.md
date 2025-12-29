# 1. Project Overview
- An Airflow project serves as the continuation of the dbt project titled: looker-ecommerce-bigquery-elt-pipeline designed to explore modern ETL/ELT pipeline orchestration, data warehousing and infrastructure management. This project covers the use of Docker for containerization, distro like Ubuntu for cloud computing and DAGs run through python scripts. 

Below shows the high-level flowchart depicting the architecture of the project.
![Project Architecture Flowchart](output_screenshots/looker-ecommerce-dbt-airflow-flowchart.png)

# 2. Tech Stack and Environment

- Programming Languages: Python v3.11
- Pipeline Orchestration: Apache Airflow v2.9.3
- Environment Setup: Docker Compose
- Operator: BashOperator
- IDE: Pycharm 2025.3.1
- Version Control: Git/GitHub
- OS: Windows 11


# 3. Airflow DAGs and Pipeline Structure

## Key Folder structure:

- dags: Contains Airflow DAGs. This project uses dbt_dag.py to trigger dbt runs.
- plugins: Reserved for custom operators, sensors, or hooks (empty in this project).
- dbt_project: placeholder for dbt_project folder (empty).

## DAG Overview
- DAG ID: dbt_run_dag
- Purpose: Automates dbt models execution in this project
- Schedule: Runs daily (@daily) starting Jan 1, 2025.
- Catchup: Disabled (catchup=False) to prevent historical runs.
- Task:
  - dbt_run – Executes a Bash command to navigate to the dbt project folder and run dbt run with the appropriate profiles directory.

## Operators and Hooks
- BashOperator: Runs shell commands inside the Airflow Container.
- No additional hooks or custom operators used.

## Task Dependencies
Single-task DAG: No explicit upstream/downstream dependencies as dbt_run is the only task.

## Error Handling
- Uses Airflow defaults: retries and SLA are not explicitly configured.
- Airflow container logs and DAG monitoring provide task-level visibility.

## Execution Environment
- Docker Compose Services:
  - postgres: Metadata database for Airflow.
  - airflow-webserver: Web UI for DAG management and monitoring.
  - airflow-scheduler: Triggers DAG runs according to schedule.
- Dockerfile: Installs dbt-core and dbt-bigquery inside the Airflow container to enable DAG execution.

Notes:
- The DAG triggers dbt models in the mounted dbt project folder, ensuring modular separation between Airflow orchestration and dbt transformations.
- All configurations are containerized, making the pipeline reproducible and portable.

![Airflow DAG UI](output_screenshots/Airflow%20DAG%20UI.png)