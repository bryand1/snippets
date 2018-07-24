from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator


default_args = {
    'owner': 'me',
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
    'email': ['bryand1@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'news',
    default_args=default_args,
    schedule_interval=timedelta(days=1))

start = KubernetesPodOperator(
    namespace='default',
    image="bryand1/news:latest",
    cmds=["python", "-u"],
    arguments=["main.py"],
    labels={"app": "news"},
    name="news",
    task_id="news",
    get_logs=True,
    dag=dag
)
