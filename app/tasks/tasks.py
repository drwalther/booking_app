from pydantic import EmailStr

from app.tasks.celery import celery
from app.tasks.email_templates import create_booking_confirmation
from app.tasks.helpers import send_message


@celery.task
def send_booking_confirmation_email(booking: dict, email: EmailStr):
    message = create_booking_confirmation(booking, email)
    send_message(message)
