import smtplib
from email.message import EmailMessage

from app.config import settings


def send_message(message: EmailMessage):
    with smtplib.SMTP_SSL(settings.SMTP_URI, settings.SMTP_PORT) as server:
        server.login(settings.EMAIL_USER, settings.EMAIL_PASS)
        server.send_message(message)
