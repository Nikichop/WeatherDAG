from airflow import DAG
from airflow.utils.dates import days_ago
from tasks import download_weather_data_task, process_weather_data_task, save_weather_data_task

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    'weather_data_pipeline_dag',
    default_args=default_args,
    description='A simple weather data pipeline DAG',
    schedule_interval='0 0 * * *',  # выполняется ежедневно в полночь
)

download_data = download_weather_data_task(dag)
process_data = process_weather_data_task(dag)
save_data = save_weather_data_task(dag)

download_data >> process_data >> save_data
