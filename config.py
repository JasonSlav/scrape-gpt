import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "bismillahucl")
DBMS_NAME = os.getenv("DBMS_NAME", "postgresql")
DB_NAME = os.getenv("DB_NAME", "dbname")
DB_USER = os.getenv("DB_USER", "username")
DB_PASS = os.getenv("DB_PASS", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

class Config:
    SECRET_KEY = (f"{SECRET_KEY}")
    SQLALCHEMY_DATABASE_URI = f"{DBMS_NAME}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False