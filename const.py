import os

TOKEN: str = os.environ.get("HOOK_TOKEN")
LOGIN: str = os.environ.get("LOGIN")
PASS: str = os.environ.get("PASS")

DEBUG: bool = os.environ.get('APP_DEBUG', 'true').lower() != 'false'
PORT: str = os.environ.get('APP_PORT', '5000')

LOGGING_LEVEL: str = os.environ.get('LOGGING_LEVEL', 'DEBUG' if DEBUG else 'INFO').upper()
