from celery import Celery

from app.config import BROKER_URI

celery = Celery("tasks", broker=BROKER_URI, include=["app.tasks.tasks"])
