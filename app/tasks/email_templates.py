from email.message import EmailMessage

from pydantic import EmailStr

from app.tasks.helpers import create_message


def create_booking_confirmation(booking: dict, email_to: EmailStr) -> EmailMessage:
    subject = "Подтверждение бронирования"
    content = f"""
#             <h1>Подтверждение бронирования</h1>
#             Номер успешно забронирован!
#             Период: {booking["check_in_date"]} - {booking["check_out_date"]}
#         """

    message = create_message(email_to, subject, content)
    return message


def create_registration_confirmation(email_to: EmailStr) -> EmailMessage:
    subject = "Подтверждение регистрации"
    content = """
            <h1>Регистрация прошла успешно</h1>
            Теперь вы можете пользоваться сервисом.
        """

    message = create_message(email_to, subject, content)
    return message
