from airflow.operators.python_operator import PythonOperator
from utils import download_weather_data, process_weather_data, save_weather_data


def download_weather_data_task(dag):
    return PythonOperator(
        task_id='download_weather_data',
        python_callable=download_weather_data,
        dag=dag,
    )


def process_weather_data_task(dag):
    return PythonOperator(
        task_id='process_weather_data',
        python_callable=process_weather_data,
        dag=dag,
    )

def save_weather_data_task(dag):
    return PythonOperator(
        task_id='save_weather_data',
        python_callable=save_weather_data,
        dag=dag,
    )