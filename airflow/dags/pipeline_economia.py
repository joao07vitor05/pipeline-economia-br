from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

sys.path.insert(0, '/opt/airflow/scripts')   # Add scripts folder to path so Airflow can find our modules

from dotenv import load_dotenv
load_dotenv('/opt/airflow/.env')

from main import extract_all, transform_all, validate_all
import transform
import load_to_sql

# Add scripts folder to path so Airflow can find our modules
default_args = {
    'owner': 'João_Vitor',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

#define the DAG
with DAG(
    dag_id='pipeline_economia_br',
    description='Daily pipeline for Brazilian economic indicators',
    schedule_interval='0 8 * * *', # Run daily at 8 am
    start_date=datetime(2025, 1, 1),
    catchup=False, 
    default_args=default_args,
) as dag:
    
    # Task 1: Extract and upload data
    task_extract = PythonOperator(
        task_id='extract_and_upload',
        python_callable=extract_all
    )

    # Task 2: Transform data
    task_transform = PythonOperator(
        task_id='transform',
        python_callable=transform_all,
    )

    # Task 3: Validate data quality
    task_validate = PythonOperator(
        task_id='validate',
        python_callable=validate_all,
    )

    # Task 4: Create unified table
    task_unified = PythonOperator(
        task_id='create_unified_table',
        python_callable=transform.create_unified_table,
    )

    # Task 5: Load data into Azure SQL
    task_load = PythonOperator(
        task_id='load_to_sql',
        python_callable=load_to_sql.load_to_sql,
    )

    # Define executation order
    task_extract >> task_transform >> task_validate >> task_unified >> task_load