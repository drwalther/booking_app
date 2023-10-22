import smtplib
from email.message import EmailMessage

from pydantic import EmailStr

from app.config import settings


def send_message(message: EmailMessage):
    """Send message to email."""
    with smtplib.SMTP_SSL(settings.SMTP_URI, settings.SMTP_PORT) as server:
        server.login(settings.EMAIL_USER, settings.EMAIL_PASS)
        server.send_message(message)


def create_message(email_to: EmailStr, subject: str, content: str):
    email = EmailMessage()
    email["Subject"] = subject
    email["From"] = settings.EMAIL_USER
    email["To"] = email_to
    email.set_content(content, subtype="html")
    return email
