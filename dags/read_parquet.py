# Python lib
import pandas as pd
from datetime import datetime

# Airflow lib
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


# Default settings applied to all tasks
default_args = {
	'owner': 'syamsul',
	'start_date': datetime(2021, 10, 19)
}


def _read_parquet():
    path = "gcs://bucket/your_path/file.parquet"

    df = pd.read_parquet(path,
                 engine='pyarrow',
                 storage_options={"token": "gcp_service_account.json"})

    print(df.head(10))


# Dag
with DAG('read_parquet',
		 schedule_interval="@daily",
		 default_args=default_args,
		  catchup=True 
		 ) as dag:
	

    parquet_to_big_query = PythonOperator(
				task_id='task_read_parquet',
				provide_context=True,
				python_callable=_read_parquet
			)
