from celery import Celery

from app.config import settings

celery = Celery("tasks", broker=settings.REDIS_URI, include=["app.tasks.tasks"])
