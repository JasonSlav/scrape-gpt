import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "bismillahucl")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:0963@127.0.0.1/flask")
    SQLALCHEMY_TRACK_MODIFICATIONS = False