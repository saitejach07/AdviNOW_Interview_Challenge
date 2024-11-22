import os
from dotenv import load_dotenv

load_dotenv()

def get_env(variable_name, default=None):
    value = os.getenv(variable_name, default)
    if value and str(value).lower() in ("true", "false"):
        return str(value).lower() == "true"
    return value

# SQLite Configuration
DB_URL: str = "sqlite:///./app.db"
