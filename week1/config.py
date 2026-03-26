import os
from dotenv import load_dotenv

load_dotenv(encoding="utf-8")


class Config:
    def __init__(self):
        self.DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
        self.DB_PORT = os.getenv("DB_PORT", "5433")
        self.DB_NAME = os.getenv("DB_NAME", "dedb")
        self.DB_USER = os.getenv("DB_USER", "deuser")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD", "pass123")
