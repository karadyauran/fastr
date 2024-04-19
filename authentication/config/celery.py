from celery import Celery

app = Celery('config')
app.autodiscover_tasks()
