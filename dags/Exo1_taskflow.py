from airflow import DAG
from datetime import datetime
from airflow.operators.python import pythonOperator

@DAG(
    dag_id= 'hello_airflow',
    
)

def hello_airflow():
    @task
    def task_a():
        print("Bonjour")
        return "Task C result"

