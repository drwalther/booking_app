from email.message import EmailMessage

from pydantic import EmailStr

from app.config import settings


def create_booking_confirmation(booking: dict, email_to: EmailStr):
    email = EmailMessage()

    email["Subject"] = "Подтверждение бронирования"
    email["From"] = settings.EMAIL_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Подтверждение бронирования</h1>
            Номер успешно забронирован!
            Период: {booking["check_in_date"]} - {booking["check_out_date"]}
        """,
        subtype="html",
    )
    return email


def create_registration_confirmation(email_to: EmailStr):
    email = EmailMessage()

    email["Subject"] = "Подтверждение регистрации"
    email["From"] = settings.EMAIL_USER
    email["To"] = email_to

    email.set_content(
        """
            <h1>Регистрация прошла успешно</h1>
            Теперь вы можете пользоваться сервисом.
        """,
        subtype="html",
    )
    return email
