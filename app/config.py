import os

from dotenv import load_dotenv

load_dotenv()

DB_URI = os.getenv("DB_URI")
TEST_DB_URI = os.getenv("TEST_DB_URI")

# Development, testing or production mode
MODE = os.getenv("MODE")

# JWT token
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

# Redis as a broker for Celery
BROKER_URI = os.getenv("BROKER_URI")

# SMTP config
SMTP_URI = os.getenv("SMTP_URI")
SMTP_PORT = os.getenv("SMTP_PORT")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_USER")
