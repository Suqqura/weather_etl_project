from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from weather_project.scripts.fetch_weather_data import fetch_weather_data
from weather_project.scripts.transform_weather_data import transform_weather_data

# DAG default args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now() - timedelta(minutes=10),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG
dag = DAG(
    'weather_etl',
    default_args=default_args,
    description='A simple weather ETL DAG',
    schedule_interval='@hourly',  
    catchup=False, 
)

# tasks
fetch_task = PythonOperator(
    task_id='fetch_weather_data',
    python_callable=fetch_weather_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_weather_data',
    python_callable=transform_weather_data,
    dag=dag,
)

# task order
fetch_task >> transform_task
