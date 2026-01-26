import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv()

TEMPLATE_DIR = os.path.join(BASE_DIR, os.getenv("TEMPLATE_DIR", "templates"))
STATIC_DIR = os.path.join(BASE_DIR, os.getenv("STATIC_DIR", "static"))
LOG_DIR = os.path.join(BASE_DIR, os.getenv("LOG_DIR", "logs"))

SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key")
