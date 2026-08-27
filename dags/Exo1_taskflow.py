from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id= 'hello_airflow',
    start_date=datetime(2026, 8, 27),
    schedule=None,
    catchup=False,
    tag=["Exo1_taskflow"],

    
    
) as dag:

    tache1= BashOperator(
        task_id= BashOperator(
            task_id="tach1e",
            bash_commande= "echo'Bonjour depuis Airflow'",
        )