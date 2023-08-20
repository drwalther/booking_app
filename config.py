import os

from dotenv import load_dotenv

load_dotenv()

DB_URI = os.getenv("DB_URI")
# JWT token
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
