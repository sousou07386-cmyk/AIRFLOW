from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id= 'hello_airflow',
    start_date=datetime(2026, 8, 27),
    schedule=None,
    catchup=False,
    tags=["Exo1_taskflow"],

) as dag:
    tache1 = BashOperator(
        task_id="tache1",
        bash_commande= "echo'Bonjour depuis Airflow'",
   )
    tache2 = BashOperator(
         task_id="tache2",
        bash_commande= """
            echo"Valeur Tache1 depuis XCOM : {{ti.xcom_pull(task_ids= 'tache1')}}
            
            """,
       )
    tache1 >> tache2